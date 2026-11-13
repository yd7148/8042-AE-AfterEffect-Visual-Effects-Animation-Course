const base = "https://github.com/yd7148/8042-AE-AfterEffect-Visual-Effects-Animation-Course"

await page.goto(`${base}/blob/main/docs/LEARNING_ROUTE_OPTIONS.md`)
await page.waitForLoadState("domcontentloaded")
await page.waitForTimeout(1500)
const routes = {
  title: await page.getByRole("heading", { name: /學習路線圖/ }).count(),
  versionA: await page.getByRole("heading", { name: /版本 A/ }).count(),
  versionB: await page.getByRole("heading", { name: /版本 B/ }).count(),
  versionC: await page.getByRole("heading", { name: /版本 C/ }).count(),
  mermaidTargets: await page.locator(".js-render-target, pre.mermaid, [data-snippet-clipboard-copy-content*='flowchart']").count(),
}

await page.goto(`${base}/blob/main/skills/ae-course-repo-sync/SKILL.md`)
await page.waitForLoadState("domcontentloaded")
const skill = {
  heading: await page.getByRole("heading", { name: "AE Course Repo Sync", exact: true }).count(),
  workflow: await page.getByRole("heading", { name: "Workflow", exact: true }).count(),
  boundaries: await page.getByRole("heading", { name: "Boundaries", exact: true }).count(),
}

return { routes, skill, finalUrl: page.url() }
