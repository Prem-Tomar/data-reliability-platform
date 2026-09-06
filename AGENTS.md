# Repository workflow

- Use a task branch for every change. Open a pull request targeting `master`.
- Never commit directly to `master` or push changes directly to it. Changes reach `master` only by merging a pull request.
- Never force-push any branch, including with `--force-with-lease`, a forced refspec, or an equivalent API operation. The force-push exception is reserved for the human owner, Prem-Tomar. An agent must not use that exception even when authenticated as the owner.
- After a branch is published, add corrective commits instead of rewriting its history.
- Do not bypass, weaken or remove repository protections to complete a task.
- Do not merge a pull request unless the user authorizes the merge. Report its URL and validation results when ready for review.
- Keep inherited local reference files excluded from public commits according to `.gitignore`.
- Keep learning concepts and languages primary. Tie changes to the roadmap and provide appropriate project evidence.
