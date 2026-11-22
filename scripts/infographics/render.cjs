// Renders SVG files to PNG with Playwright's Chromium, drawing each SVG in an
// <img> exactly as a browser shows it on the blog.
//
// Usage: node render.cjs <css-width> <device-scale> <in.svg> <out.png> [<in.svg> <out.png> ...]
const { readFileSync } = require('node:fs')
const { chromium } = require('playwright')

const [width, scale, ...files] = process.argv.slice(2)
if (!width || !scale || files.length === 0 || files.length % 2) {
  console.error('Usage: node render.cjs <css-width> <device-scale> <in.svg> <out.png> [...]')
  process.exit(1)
}

(async () => {
const browser = await chromium.launch()
const page = await browser.newPage({ viewport: { width: Number(width), height: 400 }, deviceScaleFactor: Number(scale) })
for (let i = 0; i < files.length; i += 2) {
  const data = readFileSync(files[i]).toString('base64')
  await page.setContent(
    `<body style="margin:0"><img id="svg" src="data:image/svg+xml;base64,${data}" style="display:block;width:${width}px"></body>`)
  await page.waitForFunction(() => {
    const img = document.getElementById('svg')
    return img.complete && img.naturalWidth > 0
  })
  await page.waitForTimeout(150) // let the embedded web fonts settle
  await page.locator('#svg').screenshot({ path: files[i + 1] })
}
await browser.close()
})().catch((error) => {
  console.error(error)
  process.exit(1)
})
