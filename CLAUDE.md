# CLAUDE.md - CodeCommander

This document provides guidance for AI assistants working with the CodeCommander repository.

## Project Overview

**CodeCommander** is a new project repository. This document will be updated as the project develops.

**Repository:** mattlock81/CodeCommander
**Status:** Initial setup

## Repository Structure

```
CodeCommander/
├── CLAUDE.md          # AI assistant guidelines (this file)
└── (project files to be added)
```

As the project grows, this section should be updated to reflect the actual directory structure and the purpose of each major directory.

## Development Workflow

### Branch Strategy

- **Main branch:** Primary stable branch
- **Feature branches:** Use descriptive names (e.g., `feature/add-cli-commands`, `fix/parsing-error`)
- **Claude branches:** AI-assisted work uses `claude/` prefix branches

### Commit Guidelines

1. Write clear, descriptive commit messages
2. Use conventional commit format when applicable:
   - `feat:` - New features
   - `fix:` - Bug fixes
   - `docs:` - Documentation changes
   - `refactor:` - Code refactoring
   - `test:` - Test additions/changes
   - `chore:` - Maintenance tasks

### Pull Request Process

1. Create feature branch from main
2. Make changes with atomic commits
3. Push branch and create PR
4. Include description of changes and any relevant context

## Coding Conventions

### General Guidelines

- Keep code simple and readable
- Follow existing patterns in the codebase
- Add comments only where logic isn't self-evident
- Prefer explicit over implicit code

### Testing

- Write tests for new functionality
- Ensure existing tests pass before committing
- Run the full test suite before pushing

## AI Assistant Guidelines

### Before Making Changes

1. **Read before editing:** Always read files before modifying them
2. **Understand context:** Explore related files to understand how components interact
3. **Check for patterns:** Follow existing code patterns and conventions

### When Implementing Features

1. Start with the minimal viable implementation
2. Avoid over-engineering or adding unnecessary abstractions
3. Don't add features beyond what was requested
4. Keep changes focused and atomic

### Code Quality

- Don't introduce security vulnerabilities (XSS, SQL injection, command injection, etc.)
- Validate inputs at system boundaries
- Trust internal code and framework guarantees
- Remove unused code completely (no commented-out code or placeholder comments)

### Communication

- Explain significant changes clearly
- Note any assumptions made
- Flag potential issues or edge cases
- Ask clarifying questions when requirements are ambiguous

## Common Tasks

### Setting Up the Project

```bash
# Clone the repository
git clone <repository-url>
cd CodeCommander

# (Additional setup steps to be documented as project develops)
```

### Running Tests

```bash
# (Test commands to be documented as project develops)
```

### Building the Project

```bash
# (Build commands to be documented as project develops)
```

## Dependencies

(To be documented as dependencies are added)

## Configuration

(To be documented as configuration options are added)

## Troubleshooting

### Common Issues

(To be documented as common issues are identified)

## Updates to This Document

This CLAUDE.md should be updated when:

- New directories or major files are added
- Development workflows change
- New conventions are established
- Dependencies are added or updated
- Build/test/deploy processes change

---

*Last updated: 2026-01-28*
