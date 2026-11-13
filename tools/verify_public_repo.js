await page.goto("https://github.com/yd7148/8042-AE-AfterEffect-Visual-Effects-Animation-Course")
await page.waitForLoadState("domcontentloaded")
await page.waitForTimeout(1500)

const home = {
  url: page.url(),
  title: await page.title(),
  visibility: await page.getByText("Public", { exact: true }).count(),
  issuesLink: await page.getByRole("link", { name: /Issues/ }).count(),
  heading: await page.getByRole("heading", { name: /8042 AE After Effects/ }).count(),
  mermaidSource: await page.locator("pre.mermaid, .js-render-target, [data-snippet-clipboard-copy-content*='flowchart']").count(),
  mermaidRendered: await page.locator("svg[id^='mermaid-'], .mermaid svg, svg[aria-roledescription='flowchart-v2']").count(),
}

await page.goto("https://github.com/yd7148/8042-AE-AfterEffect-Visual-Effects-Animation-Course/blob/main/classes/2026-04-18-Class01/sources/original-notes.md")
await page.waitForLoadState("domcontentloaded")
await page.waitForTimeout(1000)
const note = {
  heading: await page.getByRole("heading", { name: /原始增量筆記/ }).count(),
  renderedImages: await page.locator("article img").count(),
  anonymousTeacherText: await page.getByText(/教師：不公開/).count(),
}

await page.goto("https://github.com/yd7148/8042-AE-AfterEffect-Visual-Effects-Animation-Course/tree/main/classes/2026-06-13-Class08/aep")
await page.waitForLoadState("domcontentloaded")
const aep = {
  glowLink: await page.locator("a[href*='GLOW%20LIGHT.aep'], a[href*='GLOW-LIGHT.aep']").count(),
  manifestLink: await page.locator("a[href$='/manifest.json']").count(),
}

return {
  home,
  note,
  aep,
}
