# Git & GitHub Training Lab (`git-lab`)

**Student:** Ahmed Talaat  
**Repository:** [https://github.com/a7med-Talaat/git-lab](https://github.com/a7med-Talaat/git-lab)

This repository contains the practical deliverables, code files, and verification records for the **Git & GitHub Training** curriculum.

---

## 📁 Repository Structure

* [`app.py`](app.py): Core Python CLI utility demonstrating local workflow, argument parsing, and conflict resolution.
* [`notes.md`](notes.md): Technical notes covering Git architecture, the 3 areas, and object model internals.
* [`auth.py`](auth.py): User authentication module developed on `feature/login` and merged via Fast-Forward.
* [`ui.py`](ui.py) & [`api.py`](api.py): Modules developed on parallel branches and integrated via a 3-way merge.
* [`export.py`](export.py): Utility rebased onto `main` to maintain a clean linear commit graph.
* [`.gitignore`](.gitignore): Configuration excluding secrets (`.env`), Python caches, and temporary logs.
* [`CONTRIBUTING.md`](CONTRIBUTING.md): Project contribution guidelines, branch naming conventions, and PR etiquette.
* [`REPORT.md`](REPORT.md): Complete technical report documenting Part 0 conceptual questions, Task 1, Task 2, and Task 3 outputs.

---

## 🔍 Key Git Verification Highlights

1. **Internals & Plumbing:**
   * Blob, Tree, and Commit SHA-1 hashes verified using `git cat-file -p`, `git cat-file -t`, and `git ls-files -s`.
2. **Undoing & Recovery:**
   * Commit amendment demonstrated using `git commit --amend`.
   * Unstaging demonstrated using `git restore --staged`.
   * Dropped commit recovered from a hard reset using `git reflog`.
3. **Branch Strategies & Conflict Resolution:**
   * Fast-forward merge (`feature/login`).
   * 3-Way merge commit (`feature/ui` & `feature/api`).
   * Intentional merge conflict reproduced, conflict markers resolved, and cleanly committed.
   * Feature branch rebased onto `main` for linear history.
4. **Releases & Tags:**
   * Lightweight tag `v0.1` and annotated tag `v1.0`.

---

## 📜 Full Report

For complete terminal logs, diff outputs, architecture breakdowns, and PR simulation records, see [**REPORT.md**](REPORT.md).
