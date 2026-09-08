# Agent team

| Role | Deliverable | Boundary |
| --- | --- | --- |
| Coordinator | Scoped assignments, integrated decisions, portfolio status | Owns registry; resolves conflicts |
| Product researcher | Primary-source capability matrix and user outcomes | No unsupported parity claims |
| Architect | ADRs, interfaces and migration strategy | Compare existing OSS before creating infrastructure |
| Implementer | Product code and relevant tests | Work only in assigned paths |
| Security reviewer | Threat model and verified remediation | No compliance certification claims |
| Release verifier | Requirement-by-requirement evidence | Independently inspect actual behavior |

Every assignment states target repository, owned paths, expected artifact, acceptance criteria and forbidden mutations. The coordinator can run independent roles in parallel and must review their output.

## Configured Codex team

The primary session coordinates four project agents in `.codex/agents`: `product_researcher`, `architect`, `implementer` and `verifier`. `.codex/config.toml` enables delegation with up to three concurrent subagents. Models and reasoning effort inherit the caller's selection. Agent files do not change account credentials or grant additional permissions.

Open Codex in this trusted repository to use the configuration. Product work should use a product checkout as the working directory and the shared roles copied with the setup below. Agent configuration discovery depends on the client; roles remain usable as explicit task instructions in clients without this support.

Example assignment:

> Use product_researcher to examine Zettel issue 1 and return missing capability scenarios. In parallel, use architect to assess the shared issue/document permission model. Both return findings without edits. Integrate their results into a scoped implementation issue before assigning implementer. Ask verifier to check the resulting change against the issue criteria.

Zettel and Carthouse include reviewed copies of these roles. To install the same configuration in a future fresh sibling product checkout, copy `.codex` from this repository after reviewing it. Do not overwrite an existing `.codex` directory: reconcile product-specific settings in a PR. The shared skills remain in `.agents/skills` here and can be read from the orchestration checkout.

Configuration reference checked 2026-09-08: [official OpenAI subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents). Standalone project agent TOML files declare name, description and developer instructions. Settings and availability can vary by client version.

## Validation evidence

The installed Codex CLI 0.153.4 accepted the project config through `config/read` in an isolated temporary trusted configuration home. Repository validation parses all role TOML files and checks their required fields. This verifies configuration loading and structure; it is not a live model execution test of each role. The standalone CLI's existing user home currently marks this checkout untrusted, so it disables project settings until the user trusts the reviewed project through the client. No user-wide trust settings were changed.
