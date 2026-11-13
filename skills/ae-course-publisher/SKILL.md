---
name: ae-course-publisher
description: Organize an After Effects course archive into a privacy-safe public GitHub learning repository. Use when splitting cumulative class notes, mapping note images to their Word/Markdown sources, indexing YouTube lessons and livestreams, selecting AEP practice files, validating links and file sizes, or publishing and verifying the 8042 AE course repository.
---

# AE Course Publisher

Publish from preserved local sources. Never modify the source archive.

## Required workflow

1. Read the repository `README.md`, `docs/TODO.md`, and `docs/ASSET_AND_LICENSE_POLICY.md`.
2. Inventory source dates, cumulative note headings, image references, YouTube URLs, AEPs, Auto-Save files, installers, archives, and videos.
3. Confirm privacy settings before publication. For this project use author `4pins`; redact teacher identity; omit the training organization.
4. Split notes by explicit date or newly introduced topic boundary. Do not assume that later cumulative notes preserve chronological section order.
5. Copy only images referenced inside the selected increment. Record source Markdown, source line, original relative path, destination, byte size, and SHA-256 in `source-map.json`.
6. Keep a traceable `sources/original-notes.md`, then write a separate beginner tutorial with learning goals, ordered actions, reference-video purpose, and common mistakes.
7. Preserve practice-process AEPs, but exclude Auto-Save, AME temporary projects, cross-class duplicates, videos, ZIPs, and installers. Mark external dependencies as unverified until every AEP is opened in After Effects.
8. Run the repository import and validation commands in [pipeline.md](references/pipeline.md).
9. Review `git diff`, commit, push, then verify the public GitHub page, images, Mermaid, downloadable AEPs, Issues state, and local/remote commit equality.
10. Update the Markdown progress log with an accurate Mermaid status diagram. Never mark a browser click, push, or readable file as the end result without fresh verification.

## Publication rules

- MIT covers original repository text, diagrams, and scripts only.
- Treat third-party video, audio, fonts, trademarks, images, plugins, models, and teacher materials as separately licensed.
- Link to YouTube; do not commit downloaded video backups.
- Keep video IDs stable and verify both title and playlist order.
- Stop before publishing if a source contains personal data not covered by the redaction policy.

## Completion evidence

Report validator counts, selected AEP count/bytes, `git status`, local and remote commit IDs, public URL checks, and any remaining manual AEP dependency audit.
