# Operating setup verification — 2026-09-14

The public project hub and documentation are live at https://zinnoberhaus.github.io/zinnober-haus/. Initial deployment [34893837112](https://github.com/zinnoberHaus/zinnober-haus/actions/runs/34893837112) published commit `4f0459ef85a6ef9c5f0b2de56a99f1bc64e13438` successfully.

## Direct evidence

- Registry validation covers three repositories, nine role definitions and five service records, with owner/scope/path/handoff consistency checks.
- Five isolated setup tests cover immutable exclusions, private Project preservation, missing Project handling, incompatible fields and unchanged label reconciliation.
- Static builds passed for both the GitHub Pages subpath and an alternate root deployment. Local navigation/asset links and fragment anchors were checked across all built HTML pages; required routes and Pagefind output exist.
- A fresh headless Chrome session visited the live public site without authentication, followed both project routes, searched the documentation, and checked desktop and 390px mobile navigation. No page errors or horizontal mobile overflow were observed. This is a focused browser check, not a full accessibility audit.
- The three setup PRs merged after CI: [umbrella #3](https://github.com/zinnoberHaus/zinnober-haus/pull/3), [Zettel #7](https://github.com/zinnoberHaus/zettel/pull/7), [Carthouse #7](https://github.com/zinnoberHaus/carthouse/pull/7).
- Repository issue labels were reconciled; shared forms and issue lifecycle workflows are on all three default branches. Operational agent files are present in the appropriate product scopes. Agents run on coordinator assignment; deterministic workflows handle intake and closed-issue labels.

## Outstanding external setup

The portfolio Project cannot be created until the zinnoberHaus GitHub credential has `project` scope. The dry-run plan, guarded setup script and acceptance criteria are prepared. This remains a real incomplete item; repository Issues are already usable.

Vercel and Mintlify are evaluated alternatives, not configured services. No resources were created under the connected Microyee Vercel team, no paid plan was purchased and no domain was attached. Product repositories remain in planning; this operating setup does not establish working Zettel or Carthouse applications.
