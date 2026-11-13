# Project runbook

## Repository

- Local root: `D:\80-Opnecode\Projects\202604-AE\8042-AE-AfterEffect-Visual-Effects-Animation-Course`
- Remote: `https://github.com/yd7148/8042-AE-AfterEffect-Visual-Effects-Animation-Course`
- Default branch: `main`

## Validation

```powershell
py -3 tools/validate_repo.py .
py -3 C:\Users\N000149839\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills\ae-course-publisher
py -3 C:\Users\N000149839\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills\ae-course-repo-sync
git diff --check
```

## Push verification

```powershell
git push origin main
$localCommit = git rev-parse HEAD
$remoteCommit = (git ls-remote origin refs/heads/main).Split("`t")[0]
$localCommit -eq $remoteCommit
gh api repos/yd7148/8042-AE-AfterEffect-Visual-Effects-Animation-Course --jq '{private:.private,has_issues:.has_issues,default_branch:.default_branch}'
```

Use Browser Control for the final visible GitHub inspection when Markdown, Mermaid, or images changed.
