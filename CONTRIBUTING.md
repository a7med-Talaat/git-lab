# Contributing Guidelines

Thank you for contributing to this project! To maintain a clean and collaborative repository, please follow these guidelines.

---

## 1. Branch Naming Conventions

All branches should use clear, lowercase prefixes indicating the purpose of the work:

* eature/<feature-name>: New features or capabilities (e.g., eature/user-auth, eature/improve-docs)
* ix/<bug-name>: Bug fixes and issue patches (e.g., ix/null-pointer-exception)
* docs/<topic>: Documentation updates only (e.g., docs/api-endpoints)
* efactor/<module>: Code restructuring without changing behavior (e.g., efactor/database-queries)
* 	est/<drill-name>: Temporary testing or recovery drills (e.g., 	est/undo-drill)

---

## 2. Commit Message Conventions

We follow the **Conventional Commits** specification:

`
<type>(<optional scope>): <short description in imperative mood>

[optional body explaining 'why' rather than 'what']

[optional footer referencing issue numbers, e.g., Closes #12]
`

### Allowed Types:
* eat: A new user-facing feature
* ix: A bug fix
* docs: Documentation changes
* style: Code style, formatting, missing semi-colons (no production code change)
* efactor: Refactoring code that neither fixes a bug nor adds a feature
* 	est: Adding or correcting unit/integration tests
* chore: Build tasks, dependency updates, or auxiliary configuration

---

## 3. Pull Request (PR) & Review Etiquette

* **Keep PRs Small & Focused:** Avoid combining multiple unrelated changes into a single pull request.
* **Provide Context:** Include a descriptive summary of what changed and steps to verify/test the changes.
* **Constructive Feedback:** When reviewing code, explain the rationale behind suggestions and offer actionable alternatives.
* **Self-Review:** Perform an initial self-review before requesting reviews from peers.
* **Merge Strategy:** Prefer rebasing or squash-and-merge for clean linear history when appropriate.
