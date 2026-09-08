# Bootstrap status — 2026-09-08

## Established

- Public product repositories: Zettel and Carthouse, with product research, community policies, Apache-2.0 license and planning-artifact CI.
- Portfolio registry, shared agent roles, two validated repository skills and operating workflow.
- Research preserves the full product ambitions and separates proposed capabilities from implemented software.

## Cleanup completed

After the account owner refreshed GitHub authentication with `delete_repo`, all 12 original non-preserved repositories were deleted on 2026-09-08. Before deletion, their Git mirrors were refreshed and every mirror passed `git fsck --full` again. Deletion was restricted to the original inventory under zinnoberHaus; the new product repositories were excluded.

The authenticated post-cleanup inventory contains exactly three public repositories: `zinnober-haus`, `zettel`, and `carthouse`. No operations targeted microyee-ai, mircoyee-ai, or repositories belonging to another owner.

Git backups, the original private inventory, selected issue/pull-request/release metadata and a per-repository deletion log remain outside the public repository. These backups preserve Git history and selected metadata, not all GitHub-hosted state (settings, secrets, packages, release binaries, LFS and discussions are not comprehensively backed up).

## Setup verification

All three repositories have the shared project agent definitions, contribution/security/governance policies, Apache-2.0 licensing and validation workflows. The umbrella also owns the registry, shared skills, role usage instructions and research briefs. Each product has five milestones and five roadmap issues.

GitHub API verification confirms public visibility, issues, squash merging, merged-branch deletion, required `validate` checks on main, private vulnerability reporting and vulnerability alerts. Agent configuration and planning-artifact checks do not establish product functionality.

## Product readiness

Both products remain in planning. Implementation, installable distributions, enterprise validation and feature parity are not complete. Follow the research delivery gates and product issues before making readiness claims.
