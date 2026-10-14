# Create Problem Folder

Create a new CALICO problem folder from scratch.

## Steps

1. Create and switch to a new git branch named after the problem's short name.
2. Copy the `example/` folder to a new directory named after the problem (e.g. `mycelium/`). Use `example/` as the template — not any existing problem directory.
3. Inside the new directory, rename all files that reference the old problem name to use the new one:
   - `templates/` files
   - `submissions/` files
   - Any zip files (delete them)
   - Update `main.py`: change the problem name string and `TestCase` fields to match the new problem
4. Delete stale test data: clear `data/sample/` and `data/secret/` contents.
5. Commit everything on the new branch, then push.

## Notes
- Do not copy from an existing problem like `shadows/` — always use `example/` as the base.
- The branch name should match the problem short name.
