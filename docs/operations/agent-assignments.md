# Assigning operational agents

The main Codex session coordinates the roles in [the agent registry](../../registry/agents.json). The maintainer remains accountable for decisions and external actions. A registry entry describes when a role is useful; it does not create a timer, webhook subscription or background worker. Invoke the roles in a trusted checkout through a supported Codex client, or supply their instructions explicitly to a client without custom-agent discovery.

The checked-in TOML files use `name`, `description` and `developer_instructions`; they omit model and permission overrides. Subagents therefore inherit the parent selection and runtime permissions. The existing concurrency setting remains in [.codex/config.toml](../../.codex/config.toml). Role availability is separate from concurrency: the coordinator chooses the roles needed for a task and queues dependent work. Format and inheritance checked 2026-09-14 against [official OpenAI subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents).

## Choose the next role

| Situation | Assign | Expected result | Next step |
| --- | --- | --- | --- |
| New report or unclear ticket | `triage_manager` | Reproduction gaps, duplicates, proposed labels, acceptance criteria | Maintainer or coordinator decides priority and authorizes ticket updates |
| Missing evidence for a product choice | `product_researcher` | Dated sources, alternatives, requirements and uncertainty | `architect` resolves the design decision |
| Architecture or migration decision | `architect` | ADR, interfaces, consequences and verification gates | Assign accepted implementation paths |
| Accepted issue with clear ownership | `implementer` | Working change and relevant checks | `verifier` reviews against the original criteria |
| Documentation or public-site change | `docs_maintainer` | Accurate source changes, build and rendered-route evidence | `verifier` checks the user task; deployment follows task authorization |
| Credentials, authorization, CI, untrusted execution or dependency risk | `security_reviewer` | Evidence-backed findings and remediation | `implementer` fixes; independent reviewer verifies |
| Release candidate | `release_manager` | Candidate manifest, release notes and recovery evidence | `verifier` audits; maintainer directs publication |
| A completion claim or candidate change | `verifier` | Each criterion proven, contradicted or unverified | Resolve gaps before advancing status |
| Registry drift or portfolio review | `portfolio_steward` | Current-state evidence, registry patch and maintenance drafts | Coordinator reconciles ownership and integrates verified changes |

## Assignment contract

Give every agent a bounded work order. Include the original requirement so an agent cannot accidentally narrow it to a convenient implementation detail.

```text
Role: <registry name>
Repository: zinnoberHaus/<registered repository>
Issue / decision: <URL or original requirement>
Source revision / observation time: <commit, PR or date>
Outcome: <what must become true>
Inputs: <files, URLs, evidence and allowed environment>
Owned paths: <exact files or directories; use none for read-only work>
Allowed external actions: <specific actions already authorized, or none>
Forbidden mutations: <task-specific limits in addition to AGENTS.md>
Output: <artifact path or findings returned to the coordinator>
Acceptance criteria: <directly observable outcomes>
Verification: <appropriate commands and runtime checks>
Handoff: <role that consumes the result>
```

An assigned path is a limit, not permission to overwrite another contributor's work. Inspect worktree state first. Separate concurrent write work by paths or worktrees and reconcile shared-file changes through the coordinator. Product implementation stays in the owning product checkout. `portfolio_steward` may read product evidence while owning only umbrella registry and operations changes.

The registry's `suggested_paths` are destinations to consider when preparing a work order, not standing write grants; a suggested directory may not exist until needed. `scope_repositories` names allowed assignment repositories. Its subset must remain consistent with [repos.json](../../registry/repos.json), and both excluded spelling variants remain protected. Do not copy private security findings into a public operations report.

## Practical work orders

Use these as starting prompts, replacing revision, issue and output placeholders with real values before assignment.

**Triage an inbox.** "Use `triage_manager` to read open issues in `zinnoberHaus/zettel`. Return duplicates, missing reproduction steps, proposed labels and the next action for each issue. No file edits or GitHub mutations. Keep potential undisclosed vulnerability details out of the public summary."

**Update documentation after a change.** "Use `docs_maintainer` for the accepted PR in `zinnoberHaus/carthouse`. Own only the specific affected documentation files. Verify the documented commands against the candidate commit, build the site and inspect those routes. Return discrepancies that require implementation changes. No deployment or public messages are authorized by this documentation assignment."

**Review a release candidate.** "Use `release_manager` for the specified product commit and intended version. Read the release-readiness skill and prepare the candidate evidence and draft notes in the assigned release document. Do not publish or tag. Then use `verifier` to independently audit the original release criteria. Return every missing requirement as unverified or contradicted, with evidence."

**Review portfolio drift.** "Use `portfolio_steward` to compare registered repository, documentation and hosting links with current public state. Own only the named registry files and a dated operations report. Propose maintenance issues as drafts. Keep service state and product maturity distinct, and leave unverified URLs unverified."

**Review a sensitive change.** "Use `security_reviewer` to inspect the assigned CI or authorization change at its exact commit. Use only the named isolated test environment. Return confirmed findings, plausible risks and untested areas. Do not edit implementation, disclose vulnerabilities or use production credentials."

## Suggested operating rhythm

The maintainer can request inbox triage on working days, a weekly portfolio and documentation review, and a release review for each candidate. These are suggested human-initiated practices. No such agent schedule is installed by these role files. Deterministic CI checks can run on their documented repository events without implying an agent is continuously monitoring the project.

Every run returns its source revision or observation time, changed paths, commands and outcomes, acceptance-criteria status, remaining risks and next handoff. Record only useful durable decisions and sanitized evidence in version control; do not commit raw private issue exports, credentials or backup contents. Never treat the presence of a role file or a passing structural configuration check as evidence that its task ran successfully.

External actions follow the current task's authorization: commenting, publishing, tagging, deployment, access changes and spending need the corresponding authorized scope. Existing authorization remains valid; do not request it again solely because a new role is involved. Agents never perform recurring repository cleanup. The coordinator reviews the returned evidence and reports the actual completed state to the user.
