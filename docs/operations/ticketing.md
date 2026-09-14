# Tickets and portfolio planning

GitHub Issues is the source of truth. File product work in Zettel or Carthouse; file shared infrastructure, governance and cross-project decisions in zinnober-haus. Link dependencies between issues instead of copying the same task into several systems.

## Intake and lifecycle

Use the bug or proposal form. Each accepted ticket needs a user outcome, acceptance criteria, scope, dependencies and evidence of how to verify it. The triage manager proposes classification; the maintainer decides priority and scope.

Choose one `type:*`, one `priority:*` and at most one active `status:*` label. New tickets start at `status:triage`. The working sequence is triage → ready → in-progress → review → closed. Use blocked with a named dependency and next action. Closed issues use GitHub's completed/not-planned reason and no active status label.

P0 means active outage or critical security impact, not general urgency. Report sensitive security problems through private vulnerability reporting. P1 supports the next committed outcome; P2 is normal planned work; P3 is optional. A `good first issue` must include a reproducible setup, bounded change and maintainer support.

A milestone is a release or outcome gate. A ticket is a verifiable slice of that work. Existing foundation/parity tickets are epics: split them before implementation and retain links so the full scope stays visible. Do not invent delivery dates before work is scoped.

## Portfolio Project

The planned user-owned **Zinnober Haus Portfolio** Project collects issues across all three registered repositories. It uses the built-in Status field, plus Priority, Workstream and Target date. GitHub labels remain the portable lifecycle record; Project fields are planning views and must be reconciled during triage.

Suggested views: intake table, active-work board, blockers, per-product backlog and milestone roadmap. Views are configured in the GitHub UI after Project creation; CLI creation alone does not prove the views exist. GitHub's Free plan limits native auto-add workflows, so `scripts/github_setup.py project --apply` explicitly adds missing open issues across registered repositories without relying on a rule for every repository.

```sh
python3 scripts/github_setup.py labels            # show the intended label changes
python3 scripts/github_setup.py labels --apply    # reconcile the shared label definitions
python3 scripts/github_setup.py project           # show the board specification
python3 scripts/github_setup.py project --apply   # create/reuse the board, add fields and open issues
```

Project setup needs GitHub OAuth `project` scope. If missing, complete `gh auth refresh -h github.com -s project` in your terminal. The script stops at authentication failure; it does not change accounts or request other scopes. It records the actual Project URL/number in registry/ticketing.json for review after success. Reruns preserve existing project items and custom fields.

## Maintainer cadence

Twice weekly: review new reports, duplicates and blockers; classify ready tickets and answer actionable contributor questions. Weekly: compare active work to milestones, examine oldest waiting PRs and assign bounded agent tasks. Monthly: review dependencies, recovery/release evidence, security reports and registry accuracy. These are working targets, not promised public response SLAs.

Useful measures are time to first maintainer response, PR review wait, issue age by state, escaped defects and repeat contributors. Counts of commits, stars or automated comments do not establish project health.
