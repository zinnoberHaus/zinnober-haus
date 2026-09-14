"""Validate registry consistency and local coordination artifacts; not product readiness."""
import json
import tomllib
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def read(name):
    return json.loads((ROOT / 'registry' / name).read_text())

def require(condition, message):
    if not condition:
        raise ValueError(message)

repos = read('repos.json')
require(repos['owner'] == 'zinnoberHaus', 'Unexpected owner')
names = {r['name'] for r in repos['repositories']}
require(len(names) == len(repos['repositories']), 'Duplicate repositories')
require(not names.intersection(repos['excluded']), 'Excluded repository registered')
services = read('services.json')['services']
service_ids = {s['id'] for s in services}
require(len(service_ids) == len(services), 'Duplicate service IDs')
for repo in repos['repositories']:
    require(repo['url'] == f"https://github.com/{repos['owner']}/{repo['name']}", 'Repository URL mismatch')
    require(repo['status'] in {'planning','active','alpha','beta','stable'}, 'Unknown maturity')
    require(repo['hosting_service'] in service_ids, 'Missing hosting service')
    require(repo['issues_url'] == repo['url'] + '/issues', 'Issue URL mismatch')
for service in services:
    require((ROOT / service['runbook']).is_file(), f"Missing service runbook: {service['id']}")
    require(service['status'] in {'active','prepared','awaiting-authentication','not-provisioned'}, 'Unknown service status')
roles = read('agents.json')
require(roles['owner'] == repos['owner'], 'Agent owner mismatch')
role_names = {r['name'] for r in roles['agents']}
require(len(role_names) == len(roles['agents']), 'Duplicate agent names')
paths = set()
for role in roles['agents']:
    path = ROOT / role['config_path']
    config = tomllib.loads(path.read_text())
    require(config['name'] == role['name'], 'Role name mismatch')
    for field in ['description', 'developer_instructions']:
        require(isinstance(config.get(field), str) and bool(config[field].strip()), f'Missing role {field}')
    require(set(role['scope_repositories']) <= names, 'Unknown agent repository scope')
    require(set(role['handoff']) <= role_names, 'Unknown agent handoff')
    paths.add(path.resolve())
require(paths == {p.resolve() for p in (ROOT / '.codex/agents').glob('*.toml')}, 'Unregistered or missing role config')
config = tomllib.loads((ROOT / '.codex/config.toml').read_text())
require(config['agents']['enabled'] is True, 'Agents disabled')
require(1 <= config['agents']['max_concurrent_threads_per_session'] <= 3, 'Unexpected concurrency')
tickets = read('ticketing.json')
require(tickets['owner'] == repos['owner'], 'Ticketing owner mismatch')
require(len({x['name'] for x in tickets['labels']}) == len(tickets['labels']), 'Duplicate labels')
for path in ['AGENTS.md','README.md','CONTRIBUTING.md','SECURITY.md','GOVERNANCE.md','CODE_OF_CONDUCT.md','docs/operations/workflow.md','docs/operations/agent-assignments.md','docs/research/zettel.md','docs/research/carthouse.md','docs/research/open-source-strategy.md','docs/research/oss-operations-2026-09.md','docs/research/hosting-docs-2026-09.md']:
    require((ROOT / path).is_file(), f'Missing {path}')
print(f'Validated {len(names)} repositories, {len(role_names)} agents, {len(services)} services and ticketing definitions. Product readiness is not tested.')
