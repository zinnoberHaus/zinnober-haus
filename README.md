# Zinnober Haus

An open-source software studio building enterprise work management and AI-native data infrastructure.

This repository is the orchestration and policy home. Product code belongs in the product repositories.

| Repository | Purpose | Status |
| --- | --- | --- |
| [zettel](https://github.com/zinnoberHaus/zettel) | Self-hosted work management combining Linear's breadth with Coda-style documents, tables and automation | Planning |
| [carthouse](https://github.com/zinnoberHaus/carthouse) | AI-native data engineering, warehouse access and DAG orchestration | Planning |

Start with [AGENTS.md](AGENTS.md), the [registry](registry/repos.json), [research](docs/research), and [operating workflow](docs/operations/workflow.md).

## Local checks

Requires Python 3.10 or later. Run `python3 scripts/validate.py`.

## Principles

- Core product capabilities remain open source and self-hostable.
- Enterprise readiness is demonstrated by security, deployment and recovery evidence.
- Planning repositories are not advertised as functioning products.
- AI proposes changes; permissions, validation and human approval govern execution.

Product research and milestones describe the full ambition; initial milestones do not imply full feature parity.
