# Pipeline commands

Run from the repository root. Replace `<SOURCE>` with the preserved course archive.

```powershell
py -3 tools/import_course_notes.py "<SOURCE>" "."
py -3 tools/import_aep_examples.py "<SOURCE>" "."
py -3 tools/validate_repo.py "."
git diff --check
git status --short
```

Before commit, search for forbidden identity and binary types:

```powershell
rg -n "教師:|教師：|開課單位|訓練單位" README.md NOTICE.md docs classes
Get-ChildItem -Recurse -File | Where-Object { $_.Extension -in '.mp4','.avi','.exe','.zip' }
```

After push, compare `git rev-parse HEAD` with `git ls-remote origin refs/heads/main`, then inspect the GitHub HTML/API response and several raw image/AEP URLs.
