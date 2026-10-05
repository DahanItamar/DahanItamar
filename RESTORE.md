# Restore the previous profile

The redesign appends new commits. It does not rewrite or delete Git history.

The original README is preserved in two places:

- [`archive/README-2026-10-06-before-redesign.md`](archive/README-2026-10-06-before-redesign.md): an exact file copy.
- Git tag `profile-before-systems-redesign-2026-10-06`, pointing to commit `6a1af52dea27fa28f430be8b79e42772905214a7`.

The first redesign preview is also retained in [`archive/README-2026-10-06-first-preview.md`](archive/README-2026-10-06-first-preview.md), matching the README at commit `a02d2ff`. The poster revision adds another commit without removing either earlier version.

To restore the original profile after merging the redesign, create a new commit:

```sh
git switch main
git pull --ff-only
git restore --source=profile-before-systems-redesign-2026-10-06 -- README.md
git add README.md
git commit -m "docs: restore the previous profile README"
git push origin main
```

This retains both versions and every commit between them. Do not use `git reset --hard` or force-push to restore a README.

Alternatively, copy the archived file's contents into `README.md` in GitHub's editor and commit the change.

To compare versions:

```sh
git diff profile-before-systems-redesign-2026-10-06..main -- README.md
```
