---
name: ae-course-repo-sync
description: Safely update, validate, commit, push, and publicly verify the 8042 After Effects course repository. Use when local course notes, diagrams, links, AEP manifests, automation tools, or Skill files need to be synchronized to GitHub without losing provenance or overstating verification.
---

# AE Course Repo Sync

Synchronize the local course repository with GitHub while preserving user files and validation evidence.

## Workflow

1. Confirm the working directory and read `git status --short --branch` before editing.
2. Preserve unrelated local changes. Never reset, discard, or overwrite them.
3. Make the requested edits and update project status documents when appropriate.
4. Run `py -3 tools/validate_repo.py .`, relevant Skill validators, and `git diff --check`.
5. Review `git diff --stat` and staged files. Exclude videos, installers, archives, Auto-Save projects, secrets, and oversized files.
6. Commit with an accurate message and push the current branch to its configured upstream.
7. Compare local `HEAD` with the remote branch commit.
8. Verify the public GitHub page, affected Markdown/images/downloads, visibility, and Issues state. A successful push alone is not publication proof.
9. Report commit ID, validator results, public checks, and unresolved manual checks.

## Boundaries

- Update-and-push authorization does not permit unrelated settings changes or destructive history edits.
- Do not force-push, delete branches, or remove user changes unless explicitly requested.
- If Mermaid source is recognized but its dynamic SVG cannot be observed, report that distinction honestly.

For project paths and commands, read [project-runbook.md](references/project-runbook.md).
