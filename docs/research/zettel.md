# Zettel: product and enterprise research

Research snapshot: 2026-09-08. Status: proposed product specification, not implemented capability. Primary sources below were checked during this research. Competitors change continuously; refresh the parity inventory before every major release.

## Product decision

Build an independently implemented, openly licensed work operating system: Linear-quality product execution combined with Coda-style programmable documents and tables, deployable on a customer's infrastructure. The enterprise buyer is the engineering/product organization whose security or procurement requirements prevent adopting another hosted work system. The initial hypothesis is that linking structured work and executable specifications is more valuable than another issue tracker; validate this with design partners before treating it as established demand.

The full ambition remains all Linear feature families plus document/table workflows. A phased release is an implementation sequence, not a redefinition of parity. Do not describe the initial repository, prototype, or first issue CRUD implementation as a finished alternative.

## Evidence and competitive position

| Product | Verified observation | Implication for Zettel |
| --- | --- | --- |
| Linear | Its current feature overview covers planning, issue execution, AI/agents, analytics, mobile, customer requests, and workplace intake. Its conceptual model connects issues, teams, cycles, projects, initiatives, and views. [Features](https://linear.app/features), [concepts](https://linear.app/docs/conceptual-model) | A board and issues API are a small subset. Maintain an explicit, versioned parity ledger. |
| Coda | Tables support structured, connected data and multiple presentations. Packs add synced data, action buttons, column types, and formulas; some tables support two-way sync. [Tables](https://help.coda.io/hc/en-us/articles/39555768266893-Overview-Tables), [Packs](https://help.coda.io/hc/en-us/articles/39555769996429-Overview-Use-Packs-in-Coda), [sync tables](https://help.coda.io/hc/en-us/articles/39555773352461-Sync-data-with-Pack-tables) | The document engine must share a data model with work objects and expose controlled computation/integration primitives. Rich text alone does not meet the brief. |
| Plane | Community is AGPL-3.0; the vendor distinguishes it from closed-source Commercial and an air-gapped edition. Community already offers issues, cycles, documents, multiple views, APIs, and webhooks. [Editions](https://developers.plane.so/self-hosting/editions-and-versions), [community features](https://plane.so/open-source) | Self-hosted issue tracking is an existing category. Differentiate through a unified programmable workspace and openly available enterprise controls. Compare editions individually; do not imply every marketed feature is open source. |
| Grist | Its Apache-2.0 community edition can be self-hosted, and a desktop distribution can work without internet. Its full edition has additional licensed enterprise functionality. [Self-managed documentation](https://support.getgrist.com/self-managed/) | Portable structured documents are feasible. Study access control and installation ergonomics; do not confuse source availability of proprietary editions with open-source rights. |

Recommendation: keep SSO, provisioning, audit export, backup/restore, and deployment tooling in the open distribution. Monetize optional managed hosting, support, migration, training, and contracted operational guarantees. This is a proposed business model, not a demonstrated source of revenue.

## Full parity ledger to create in the product repository

Every row needs a source URL and review date, acceptance scenario, issue owner, implementation status, and evidence link. Status vocabulary: researched, specified, implementing, verified, deferred. Deferred features remain visible scope. The following is a starting taxonomy, not an exhaustive audited claim of today's entire Linear feature set.

| Family | Required capability envelope | Release evidence |
| --- | --- | --- |
| Work model | Workspaces, teams/subteams, members, roles, issues/subissues, relationships/dependencies, labels, estimates, priorities, dates, custom fields, templates, attachments, comments/reactions, activity and history | Cross-team work lifecycle, concurrent edits, permission boundaries, and round-trip export |
| Execution | Configurable workflows, backlog, recurring cycles and rollover, triage, duplicates, snooze, routing rules, bulk actions, keyboard workflows, inbox and notifications | Scheduled rollover and triage scenarios with retries and time-zone boundaries |
| Planning | Projects, milestones, dependencies, initiatives/subinitiatives, ownership, roadmaps, progress/health updates, portfolio views | Issue-to-project-to-initiative rollup under restricted visibility |
| Views and analytics | Search, saved filtered/grouped views, lists/boards/timelines, dashboards, delivery analytics and reports | Permission-filtered results plus deterministic metric fixtures |
| Customer and integration workflows | Requests, customer context, intake forms/Asks equivalents, email/Slack workflows, GitHub/GitLab links, APIs, webhooks, importers and export | Import reconciliation; signed webhook delivery, retries and deduplication |
| Clients and collaboration | Fast web experience, mobile access, desktop distribution, realtime collaboration, mentions, document history and conflict handling | Multi-client edits and supported offline/reconnect behavior; client-specific feature ledger |
| AI and agents | Search/summary/triage assistance, agent identities, assignment, tool access, execution history and coding-workflow integration where applicable | Explicit permissions, configurable provider, tenant isolation, disabled-AI mode and auditable actions |
| Enterprise | SAML/OIDC, SCIM, granular permissions, guests, session policy, audit, retention, legal export, integration governance and operational controls | IdP lifecycle tests, tenant isolation, restore exercise, security review |
| Programmable docs | Nested pages, collaborative rich text, relational tables, linked views, formulas, buttons, forms, automations, packs/connectors, reusable templates and cross-document references | One specification drives a real work table; permissions survive formulas, embeds, search, exports and sync |

Linear's [cycles](https://linear.app/docs/use-cycles), [triage](https://linear.app/docs/triage), and [initiatives](https://linear.app/docs/initiatives?noRedirect=1) document behavioral details that must become executable tests, not merely matching feature names. For Coda-style automation, model scheduled, row-change, form and webhook triggers with explicit execution history and retry behavior. [Coda automations](https://help.coda.io/hc/en-us/articles/39555778179853-Automations-in-Coda)

## Architecture proposal

Start with a modular monolith and worker, a browser client, durable relational storage, and object storage for attachments. Keep work, documents/tables, identity/policy, integrations, automation, and search as explicit modules. Avoid separate microservices until scaling or trust boundaries justify them. Do not require a proprietary cloud to boot, authenticate, search, or perform routine work.

Use first-class work records with a shared table/view abstraction: a document embeds a live view of issues, not a second copied issue database. Preserve stable object identifiers, revision history, schema evolution, and import origin IDs. Define a common authorization policy used by APIs, search, document embeds, formulas, exports, notifications and background jobs. Derived values must not reveal restricted input data.

Formula execution needs a restricted expression language, typed errors, dependency tracking, cycle detection, resource budgets and deterministic recalculation. Never execute arbitrary user expressions in the application process. Connectors need per-installation credentials, explicit network scopes, isolation, idempotency keys and revocation. Two-way sync needs conflict ownership rules, origin tagging and loop prevention before expansion to many connectors.

AI is an optional adapter. Admins choose providers and outbound data policy, or disable it entirely. Agent identities receive bounded permissions; sensitive actions use the same authorization and audit paths as humans. Cross-tenant retrieval and prompt-driven privilege escalation are release blockers.

## Enterprise and installation contract

Linear documents shared security responsibility, SCIM, and enterprise audit logs; these demonstrate buyer expectations rather than certifications transferable to Zettel. [Security](https://linear.app/docs/security), [SCIM](https://linear.app/docs/scim), [audit log](https://linear.app/docs/audit-log)

Proposed acceptance gates:

- A fresh host starts a pinned container release using documented commands, generated secrets and an initial-admin setup flow. Document prerequisites and measured hardware use. A download must lead to a working application, not merely source files.
- A production guide covers TLS, database/object backups, mail, secrets rotation, external identity, observability, upgrades and supported versions. Provide Kubernetes packaging once its installation and rollback are exercised in CI.
- Enforce tenant/resource authorization server-side, including attachment URLs and jobs. Test account deprovisioning, revoked sessions/tokens, changed team membership and guest access.
- Emit append-only security events with actor, scope, action, object, timestamp and correlation ID; support customer-controlled retention and export to external storage/SIEM.
- Ship a release manifest, checksums, SBOM, dependency/license checks, signed provenance, migration notes and vulnerability reporting process. Never claim SOC 2, HIPAA or other compliance based only on features or competitors' credentials.
- Exercise backup restoration onto a clean environment and an upgrade from the previous supported version. Database rollback may require restore or a forward fix; do not promise automatic rollback without testing it.
- Test a network-restricted deployment with optional integrations and telemetry disabled. Publish which optional capabilities require external services.

## License and contribution recommendation

Apache-2.0 is the proposed default for enterprise adoption and permissive integration; its text includes patent provisions and redistribution conditions. Use the actual license text and preserve required notices. [Apache license](https://www.apache.org/licenses/LICENSE-2.0)

AGPL-3.0 is a different strategic option if network copyleft is preferred, but do not import Plane implementation code into a permissively licensed project without a license compatibility decision. Build original implementations against documented behavior. Repository licensing is separate from names, logos, and trademarks. Keep dependency notices and record licenses at the exact pinned version. Confirm the portfolio-wide license choice before representing it as settled policy.

## Delivery sequence and completion gates

1. **Foundation and discovery:** validate three to five enterprise design partners, inventory Linear/Coda scenarios, record license/architecture decisions, publish threat model and contribution/release conventions. Exit: a prioritized ledger with no silently dropped feature families.
2. **Usable first release:** secure workspace/team identity, issue lifecycle, projects, cycles, search, docs with linked work tables, comments, import/export and a reproducible self-hosted package. Exit: a new user installs it and completes a real planning-to-delivery workflow with data surviving restart and restore.
3. **Enterprise pilot:** SSO/SCIM, granular authorization, audit export, operational docs, tested upgrades, integration governance and measured workload profiles. Exit: independent tenant-isolation checks and a pilot running on customer-controlled infrastructure. No general enterprise-ready claim before these checks.
4. **Programmable workspace:** relational tables, formulas, forms/buttons, automation runtime, connectors and collaboration/history. Exit: multi-user document-driven workflows with permission-safe computation and retry-safe external writes.
5. **Full parity program:** advanced planning/analytics/customer intake, mobile/desktop polish, broad integrations and optional agents. Exit: every baseline-ledger scenario verified or explicitly identified as still missing; full parity cannot be claimed while rows remain deferred.

Set dates after staffing, discovery and architecture spikes. A complete product of this scope is a sustained program; initial repository setup is the starting point.
