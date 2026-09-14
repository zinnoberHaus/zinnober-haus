import { readdir, readFile, writeFile, mkdir, rm } from 'node:fs/promises';
import { dirname, resolve, relative, extname } from 'node:path';
import { fileURLToPath } from 'node:url';
const root = resolve(dirname(fileURLToPath(import.meta.url)), '../..');
const output = resolve(root, 'site/src/content/docs');
const base = (process.env.SITE_BASE || '/zinnober-haus').replace(/\/$/, '');
const sources = new Map();
for (const category of ['operations', 'research']) {
  for (const name of await readdir(resolve(root, 'docs', category))) {
    if (extname(name) === '.md') sources.set(`docs/${category}/${name}`, `handbook/${category}/${name}`);
  }
}
for (const name of ['CONTRIBUTING', 'GOVERNANCE', 'SECURITY', 'CODE_OF_CONDUCT']) {
  sources.set(`${name}.md`, `handbook/community/${name.toLowerCase().replaceAll('_', '-')}.md`);
}
for (const dir of ['handbook', 'projects']) await rm(resolve(output, dir), { recursive: true, force: true });
for (const [source, destination] of sources) {
  let text = await readFile(resolve(root, source), 'utf8');
  const title = text.match(/^# (.+)$/m)?.[1] || source;
  text = text.replace(/^# .+\n/, '');
  // Keep original relative links useful after moving content into the documentation site.
  text = text.replace(/(?<!!)\[([^\]]+)\]\(([^\s)]+)\)/g, (all, label, href) => {
    if (/^(https?:|mailto:|#)/.test(href)) return all;
    const [path, fragment] = href.split('#');
    const target = relative(root, resolve(root, dirname(source), path));
    const doc = sources.get(target);
    const url = doc ? `${base}/${doc.replace(/\.md$/, '')}/${fragment ? `#${fragment}` : ''}` : `https://github.com/zinnoberHaus/zinnober-haus/blob/main/${target}${fragment ? `#${fragment}` : ''}`;
    return `[${label}](${url})`;
  });
  const dest = resolve(output, destination);
  await mkdir(dirname(dest), { recursive: true });
  await writeFile(dest, `---\ntitle: ${JSON.stringify(title)}\neditUrl: ${JSON.stringify(`https://github.com/zinnoberHaus/zinnober-haus/edit/main/${source}`)}\n---\n${text}`);
}
const registry = JSON.parse(await readFile(resolve(root, 'registry/repos.json'), 'utf8'));
for (const repo of registry.repositories.filter(r => r.name !== 'zinnober-haus')) {
  await mkdir(resolve(output, 'projects'), { recursive: true });
  const body = `---\ntitle: ${JSON.stringify(repo.name === 'zettel' ? 'Zettel' : 'Carthouse')}\n---\n\n${repo.purpose}.\n\n**Maturity: ${repo.status}.** There is no downloadable application release yet.\n\n- [Source and contribution guide](${repo.url})\n- [Open tickets](${repo.url}/issues)\n- [Milestones](${repo.url}/milestones)\n- [Product research](${base}/handbook/research/${repo.name}/)\n\nStart with a scoped issue and its acceptance criteria. Full product requirements remain tracked in the research and milestones; current repository checks verify planning artifacts only.\n`;
  await writeFile(resolve(output, `projects/${repo.name}.md`), body);
}
console.log(`Generated ${sources.size} handbook pages and ${registry.repositories.length - 1} project pages from repository sources.`);
