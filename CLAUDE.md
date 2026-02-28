# CLAUDE.md — CheeseHacks2026

This file provides guidance for AI assistants (Claude Code and others) working in this repository.

---

## Project Overview

**CheeseHacks2026** is a hackathon project repository, currently in the initial setup stage. As of the last update, no application code, dependencies, or infrastructure has been committed. The project is ready for development to begin.

- **Author / Owner:** RohanDasguptaUW (rohandasgupta024@gmail.com)
- **Repository:** RohanDasguptaUW/CheeseHacks2026
- **Primary branch:** `master`

---

## Repository State

> **Note:** This CLAUDE.md was generated when the repository contained only a README placeholder. Update this file as the project evolves — add tech stack details, build commands, conventions, and architectural decisions as they are established.

Current contents:
```
CheeseHacks2026/
├── .git/
├── CLAUDE.md          ← this file
└── README.md          ← title only
```

---

## Git Workflow

### Branching
- Primary branch: `master`
- Feature/task branches follow the pattern: `<username>/<short-description>` or `claude/<task-id>` for AI-generated branches
- Never commit directly to `master` for non-trivial changes; open a PR

### Commits
- Write clear, imperative-mood commit messages: `Add login page`, `Fix typo in README`
- Keep commits focused and atomic — one logical change per commit
- Reference issue numbers in commit messages when applicable: `Fix auth bug (#42)`

### Pushing
- Use `git push -u origin <branch-name>` for new branches
- Do not force-push to `master`

---

## Development Setup

> **This section should be updated** once the tech stack and project structure are decided. Below are placeholders.

### Prerequisites
- (To be defined — e.g., Node.js >= 20, Python >= 3.11, Docker, etc.)

### Installation
```bash
# Clone the repo
git clone https://github.com/RohanDasguptaUW/CheeseHacks2026.git
cd CheeseHacks2026

# Install dependencies (update once tech stack is chosen)
# npm install        # for Node.js
# pip install -r requirements.txt   # for Python
```

### Running Locally
```bash
# Add start command once defined
# npm run dev
# python main.py
```

### Running Tests
```bash
# Add test command once defined
# npm test
# pytest
```

### Building for Production
```bash
# Add build command once defined
# npm run build
```

---

## Code Conventions

> Update this section as conventions are established for the chosen tech stack.

### General
- Prefer clarity over cleverness
- Keep functions small and single-purpose
- Delete dead code rather than commenting it out
- Avoid over-engineering — build what's needed, not what might be needed later

### Naming
- Use descriptive, unambiguous names for variables, functions, and files
- Follow the conventions of the chosen language/framework (e.g., `camelCase` for JS, `snake_case` for Python)

### Error Handling
- Handle errors at system boundaries (user input, external APIs, file I/O)
- Avoid swallowing errors silently — log or surface them appropriately

---

## AI Assistant Instructions

### What to do
- Read existing code before modifying it
- Keep changes minimal and focused on the task at hand
- Update this CLAUDE.md whenever the project structure, tech stack, or conventions change significantly
- Prefer editing existing files over creating new ones unless a new file is clearly necessary

### What to avoid
- Do not add unused boilerplate, placeholder comments, or TODO stubs unless asked
- Do not refactor code outside the scope of the current task
- Do not add dependencies without a clear reason
- Do not commit `.env` files, secrets, or credentials

### When to ask
- If the tech stack or architecture is ambiguous, ask before generating substantial code
- If a task could be interpreted multiple ways, clarify before proceeding

---

## Environment & Configuration

- No `.env` file or secrets management configured yet
- No CI/CD pipelines (e.g., GitHub Actions) configured yet
- No Docker configuration yet

Once these are added, document them here with the expected variables and how to obtain them.

---

## Updating This File

Keep this file current as the project grows. In particular, update:
1. **Project Overview** — describe what the app does once it's defined
2. **Repository State** — remove the "empty repo" note and describe the actual structure
3. **Development Setup** — fill in real install, run, and test commands
4. **Code Conventions** — add language/framework-specific rules
5. **Environment & Configuration** — list required env vars with descriptions
