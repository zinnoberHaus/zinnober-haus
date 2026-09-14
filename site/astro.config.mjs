import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
export default defineConfig({
  site: process.env.SITE_URL || 'https://zinnoberhaus.github.io',
  base: process.env.SITE_BASE || '/zinnober-haus',
  trailingSlash: 'always',
  integrations: [starlight({
    title: 'Zinnober Haus',
    description: 'Open-source projects, shared working practices, and the people and agents building them.',
    social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/zinnoberHaus/zinnober-haus' }],
    customCss: ['./src/styles/custom.css'],
    sidebar: [
      { label: 'Start here', link: '/' },
      { label: 'Projects', items: [{ autogenerate: { directory: 'projects' } }] },
      { label: 'How we work', items: [{ autogenerate: { directory: 'handbook/operations' } }] },
      { label: 'Research', items: [{ autogenerate: { directory: 'handbook/research' } }], collapsed: true },
      { label: 'Community', items: [{ autogenerate: { directory: 'handbook/community' } }], collapsed: true },
    ],
  })],
});
