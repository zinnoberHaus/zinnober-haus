import { chromium } from '@playwright/test';
const origin = process.env.SMOKE_ORIGIN || 'http://127.0.0.1:4321';
const base = (process.env.SITE_BASE || '/zinnober-haus').replace(/\/$/, '');
const browser = await chromium.launch({ channel: 'chrome', headless: true });
try {
const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
const errors=[];
page.on('pageerror', error => errors.push(error.message));
await page.goto(origin + base + '/');
await page.getByRole('heading', { level: 1, name: 'Software built in the open.' }).waitFor();
await page.screenshot({path:'/tmp/zinnober-haus-desktop.png', fullPage:true});
await page.getByRole('link', {name:'Explore Zettel', exact:true}).click();
await page.getByRole('heading', {level:1,name:'Zettel',exact:true}).waitFor();
await page.getByRole('button', {name:/Search/}).click();
await page.getByRole('textbox', {name:'Search', exact:true}).fill('ticketing');
await page.locator('.pagefind-ui__result-link').first().waitFor();
await page.keyboard.press('Escape');
await page.setViewportSize({width:390,height:844});
await page.goto(origin + base + '/');
await page.screenshot({path:'/tmp/zinnober-haus-mobile.png', fullPage:true});
if (await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1)) throw new Error('Horizontal overflow on mobile');
await page.getByRole('link', {name:'Explore Carthouse',exact:true}).click();
await page.getByRole('heading', {level:1,name:'Carthouse',exact:true}).waitFor();
if(errors.length) throw new Error(errors.join('\n'));
} finally { await browser.close(); }
console.log('Desktop/mobile navigation, project routes, search and browser errors checked.');
