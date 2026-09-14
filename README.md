# Zinnober Haus

An open-source software studio building enterprise work management and AI-native data infrastructure.

This repository is the orchestration and policy home. Product code belongs in the product repositories.

| Repository | Purpose | Status |
| --- | --- | --- |
| [zettel](https://github.com/zinnoberHaus/zettel) | Self-hosted work management combining Linear's breadth with Coda-style documents, tables and automation | Planning |
| [carthouse](https://github.com/zinnoberHaus/carthouse) | AI-native data engineering, warehouse access and DAG orchestration | Planning |

Start with the [public handbook](https://zinnoberhaus.github.io/zinnober-haus/), [ticketing guide](docs/operations/ticketing.md), [agent assignments](docs/operations/agent-assignments.md), and [research findings](docs/research/oss-operations-2026-09.md).

The registry covers [repositories](registry/repos.json), [agents](registry/agents.json), [services](registry/services.json), and [ticket conventions](registry/ticketing.json). GitHub Issues owns the work; the handbook is generated from the checked-in docs and registry.

The executable Codex team is configured in [.codex](.codex); see [agent usage](agents/README.md) for assignments and product setup.

## Local checks

Requires Python 3.11+ and Node 24.11.1+ (see `.nvmrc`).

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests
npm ci --prefix site
npm run build --prefix site
python3 scripts/check_site.py
```

Run `python3 scripts/github_setup.py labels` or `project` to inspect the configuration plan; add `--apply` for authorized setup. GitHub Projects requires the `project` OAuth scope. See [hosting and documentation](docs/operations/hosting-and-docs.md) for local preview and deployment.

## Principles

- Core product capabilities remain open source and self-hostable.
- Enterprise readiness is demonstrated by security, deployment and recovery evidence.
- Planning repositories are not advertised as functioning products.
- AI proposes changes; permissions, validation and human approval govern execution.

Product research and milestones describe the full ambition; initial milestones do not imply full feature parity.
