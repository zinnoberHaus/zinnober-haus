---
name: publish-handbook
description: Build, verify and publish the Zinnober Haus public project hub and handbook from canonical docs and registries.
---

Read docs/operations/hosting-and-docs.md and registry/services.json. Edit canonical docs/ sources and registry/repos.json; site/src/content/docs/handbook and projects are generated. Keep product installation claims tied to released behavior.

Use the Node version in .nvmrc. Run npm ci --prefix site, npm run build --prefix site and python3 scripts/check_site.py. Check affected routes in a browser; for broad layout/navigation changes use site/scripts/smoke.mjs with a running preview and installed Chrome. Search needs the built Pagefind assets.

GitHub Pages uses /zinnober-haus; a different host root needs SITE_BASE=/ and the actual SITE_URL. Build and check that configuration separately. Publishing proceeds through a reviewed PR and the Pages workflow on main when the task authorizes publication. Verify the anonymous live URL and deployment status before recording the service as active. A successful local build is not a live deployment.

Never link the site to the connected Microyee Vercel team without explicit authorization for that scope. Resolve custom-domain ownership and paid plans before making those external changes.
