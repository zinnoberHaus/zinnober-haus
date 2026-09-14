"""Reconcile the registered portfolio's GitHub labels and Project; dry-run by default."""
import argparse
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def gh(*args):
    result = subprocess.run(['gh', *map(str, args)], capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    return json.loads(result.stdout) if result.stdout.strip() else None


def load_targets():
    repos = json.loads((ROOT / 'registry/repos.json').read_text())
    spec = json.loads((ROOT / 'registry/ticketing.json').read_text())
    owner = repos['owner']
    if owner != 'zinnoberHaus' or spec['owner'] != owner:
        raise ValueError('Unexpected owner; only zinnoberHaus is authorized.')
    excluded = {'microyee-ai', 'mircoyee-ai'} | {name.casefold() for name in repos['excluded']}
    names = [r['name'] for r in repos['repositories']]
    if len(set(names)) != len(names):
        raise ValueError('Duplicate repository names.')
    for repo in repos['repositories']:
        name = repo['name']
        if name.casefold() in excluded or '/' in name or repo['url'] != f'https://github.com/{owner}/{name}':
            raise ValueError(f'Invalid or excluded repository: {name}')
    return owner, names, spec


def labels(owner, names, spec):
    for name in names:
        current = gh('api', '--paginate', '--slurp', f'repos/{owner}/{name}/labels?per_page=100')
        existing = {item['name']: item for page in current for item in page}
        for label in spec['labels']:
            old = existing.get(label['name'])
            if old and all(old.get(key) == label[key] for key in ('color', 'description')):
                continue
            gh('label', 'create', label['name'], '--repo', f'{owner}/{name}', '--color', label['color'], '--description', label['description'], '--force')
            print(f"Reconciled {name}: {label['name']}")


def project(owner, names, spec):
    wanted = spec['project']
    # This read requires project access and happens before any mutation.
    result = gh('project', 'list', '--owner', owner, '--limit', '1000', '--format', 'json')
    projects = result['projects']
    if len(projects) >= 1000:
        raise RuntimeError('Project inventory may be incomplete; narrow manually before continuing.')
    matches = [p for p in projects if p['number'] == wanted['number']] if wanted.get('number') else [p for p in projects if p['title'] == wanted['title']]
    if len(matches) > 1:
        raise RuntimeError('Multiple matching Projects; record the intended number in the registry.')
    if wanted.get('number') and not matches:
        raise RuntimeError('Registered Project is missing or closed; do not silently replace it.')
    board = matches[0] if matches else gh('project', 'create', '--owner', owner, '--title', wanted['title'], '--format', 'json')
    if matches and not board.get('public', False):
        raise RuntimeError('Existing Project is private; refusing to change its visibility.')
    number = board['number']
    wanted.update(number=number, url=board['url'], state='configuring')
    registry_path = ROOT / 'registry/ticketing.json'
    registry_path.write_text(json.dumps(spec, indent=2) + '\n')
    gh('project', 'edit', number, '--owner', owner, '--visibility', 'PUBLIC', '--description', 'Shared planning for Zettel, Carthouse and Zinnober Haus operations. Issues remain the source of truth.')
    query = 'query($owner:String!,$number:Int!){user(login:$owner){projectV2(number:$number){fields(first:100){nodes{... on ProjectV2FieldCommon{id name dataType} ... on ProjectV2SingleSelectField{options{id name}}}pageInfo{hasNextPage}}}}}'
    response = gh('api', 'graphql', '-f', f'query={query}', '-f', f'owner={owner}', '-F', f'number={number}')
    field_data = response['data']['user']['projectV2']['fields']
    if field_data['pageInfo']['hasNextPage']:
        raise RuntimeError('Field inventory exceeds page size; inspect manually before continuing.')
    fields = field_data['nodes']
    existing = {f['name']: f for f in fields}
    for field in wanted['fields']:
        if field['name'] in existing:
            current = existing[field['name']]
            if current['dataType'] != field['type'] or not set(field.get('options', [])) <= {o['name'] for o in current.get('options', [])}:
                raise RuntimeError(f"Project field drift for {field['name']}; review type/options manually. Values preserved.")
            continue  # Never replace existing field options or values.
        args = ['project', 'field-create', number, '--owner', owner, '--name', field['name'], '--data-type', field['type'], '--format', 'json']
        if 'options' in field:
            args += ['--single-select-options', ','.join(field['options'])]
        gh(*args)
    for name in names:
        gh('project', 'link', number, '--owner', owner, '--repo', f'{owner}/{name}')
        pages = gh('api', '--paginate', '--slurp', f'repos/{owner}/{name}/issues?state=open&per_page=100')
        for issue in (i for page in pages for i in page if 'pull_request' not in i):
            # GitHub returns the existing Project item when an issue is already present.
            gh('project', 'item-add', number, '--owner', owner, '--url', issue['html_url'], '--format', 'json')
    wanted['state'] = 'active'
    registry_path.write_text(json.dumps(spec, indent=2) + '\n')
    print(f"Project ready: {board['url']}. Configure desired views in the GitHub UI.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['labels', 'project'])
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    owner, names, spec = load_targets()
    if not args.apply:
        print(json.dumps({'operation': args.operation, 'owner': owner, 'repositories': names, 'changes': spec[args.operation if args.operation == 'labels' else 'project']}, indent=2))
        return
    if gh('api', 'user')['login'] != owner:
        raise RuntimeError('Active GitHub account is not zinnoberHaus; no changes made.')
    (labels if args.operation == 'labels' else project)(owner, names, spec)


if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, ValueError, KeyError) as error:
        raise SystemExit(f'Setup stopped: {error}')
