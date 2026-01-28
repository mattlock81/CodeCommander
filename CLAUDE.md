# CLAUDE.md - Python Learning Journey for PowerShell Developers

This document provides guidance for AI assistants working with the Python Learning repository.

## Project Overview

**Python Learning Journey** is a structured educational repository designed to teach Python to experienced PowerShell developers through direct comparison and hands-on practice.

**Target Audience:** PowerShell developers transitioning to Python
**Lesson Duration:** 15-30 minutes per lesson
**Approach:** Concept comparison (PowerShell → Python) with practical exercises

**Repository:** [Your-GitHub-Username]/python-learning-journey
**Status:** Active learning project

## Repository Structure

```
python-learning-journey/
├── CLAUDE.md                    # AI assistant guidelines (this file)
├── README.md                    # Progress tracker and overview
├── 01_Variables_and_Types/
│   ├── lesson.md               # Theory and comparisons
│   ├── powershell_examples.ps1 # PowerShell reference code
│   ├── python_examples.py      # Python equivalent code
│   ├── exercises.md            # Practice problems
│   └── lessons_learned.md      # Post-lesson reflections
├── 02_Functions_and_Parameters/
│   └── [same structure]
├── 03_Collections_Lists/
├── 04_Collections_Dictionaries/
├── 05_Control_Flow_Conditionals/
├── 06_Control_Flow_Loops/
├── 07_File_Operations/
├── 08_Error_Handling/
├── 09_REST_APIs_JSON/
├── 10_Modules_and_Packages/
└── 99_Final_Project/
    └── jira_api_client/        # Real-world Atlassian integration
```

## Learning Workflow

### Progress Tracking

The `README.md` file serves as the central progress tracker using this format:

```markdown
## Learning Progress

| Module | Lesson | Status | Completed Date | Notes |
|--------|--------|--------|----------------|-------|
| 01 | Variables and Types | ✅ Complete | 2026-01-29 | Understood mutability differences |
| 02 | Functions | 🔄 In Progress | - | Working on kwargs |
| 03 | Lists | ⬜ Not Started | - | - |
```

**Status Indicators:**
- ⬜ Not Started
- 🔄 In Progress
- ✅ Complete
- ⚠️ Needs Review

### Lesson Progression

1. **Read lesson.md** - Understand concept through PowerShell comparison
2. **Study code examples** - Compare PowerShell and Python implementations
3. **Complete exercises** - Practice in `exercises.md`
4. **Reflect and document** - Create `lessons_learned.md`
5. **Update README.md** - Mark lesson status
6. **Commit progress** - Git commit with descriptive message

### Branch Strategy

- **main branch:** Stable completed lessons
- **learning/lesson-XX:** Active lesson work
- **review/lesson-XX:** Lessons needing revisit

### Commit Guidelines

Use descriptive commit messages following this pattern:
- `lesson: Complete 01 - Variables and Types`
- `exercise: Add solution for functions exercise 3`
- `reflect: Document lessons learned for REST APIs module`
- `review: Revisit error handling patterns`

## AI Assistant Guidelines for Lesson Creation

### Before Creating a Lesson

1. **Check README.md** to identify next lesson in sequence
2. **Read previous lesson** to maintain continuity
3. **Understand learner context:** Experienced PowerShell developer, enterprise background

### Lesson Creation Pattern

Each lesson MUST follow this exact structure:

#### 1. Create lesson.md

**Required Sections:**
```markdown
# [Lesson Number]: [Topic Name]

## PowerShell Context
[Brief reminder of how PowerShell handles this concept]

## Python Equivalent
[Explanation of Python's approach]

## Key Differences
- Difference 1
- Difference 2
- Difference 3

## When to Use What
[Practical guidance]

## Common Gotchas for PowerShell Developers
[Specific pitfalls to avoid]

## Next Steps
[Preview of next lesson]
```

#### 2. Create powershell_examples.ps1

```powershell
<#
.SYNOPSIS
    PowerShell examples for [Topic]

.DESCRIPTION
    Reference implementation showing PowerShell approach to [concept].
    Compare with python_examples.py
#>

# Example 1: [Description]
# PowerShell approach
[code]

# Example 2: [Description]
# PowerShell approach
[code]

# Example 3: [Description]
# PowerShell approach with Comment-Based Help style
[code]
```

**Requirements:**
- Use Comment-Based Help format
- Include 3-5 practical examples
- Show enterprise/professional patterns
- Include inline comments explaining WHY, not just WHAT

#### 3. Create python_examples.py

```python
"""
Python examples for [Topic]

Reference implementation showing Python approach to [concept].
Compare with powershell_examples.ps1
"""

# Example 1: [Description]
# Python approach - equivalent to PowerShell example 1
[code]

# Example 2: [Description]
# Python approach - equivalent to PowerShell example 2
[code]

# Example 3: [Description]
# Python approach with docstring style
[code]
```

**Requirements:**
- Mirror PowerShell examples exactly (same logic, different syntax)
- Use PEP 8 style
- Include docstrings for functions
- Show Pythonic patterns
- Add comments highlighting differences from PowerShell

#### 4. Create exercises.md

```markdown
# Exercises: [Topic Name]

Complete these exercises to practice [concept]. Solutions should be committed separately.

## Exercise 1: [Easy - Concept Application]
**PowerShell Reference:**
```powershell
[PowerShell code to convert]
```

**Your Task:**
Convert this PowerShell code to Python. Ensure it produces identical output.

**Expected Output:**
```
[output]
```

---

## Exercise 2: [Medium - Problem Solving]
**Scenario:**
[Real-world problem relevant to Atlassian/automation work]

**Requirements:**
- Requirement 1
- Requirement 2
- Requirement 3

**Hints:**
- Hint 1
- Hint 2

---

## Exercise 3: [Advanced - Integration]
**Challenge:**
[Complex scenario combining this lesson with previous concepts]

**Success Criteria:**
- Criteria 1
- Criteria 2

---

## Bonus Challenge (Optional)
[Extension activity for deeper learning]
```

**Requirements:**
- Minimum 3 exercises per lesson
- Progressive difficulty (easy → medium → advanced)
- Include PowerShell reference code when applicable
- Provide expected outputs
- Relate to enterprise/automation scenarios

#### 5. Create lessons_learned.md Template

**DO NOT pre-fill this file.** Create it as a template only. The learner completes it after finishing the lesson.

```markdown
# Lessons Learned: [Topic Name]

**Completed:** [Date]
**Time Spent:** [Duration]

## Key Takeaways

### What I Learned
1.
2.
3.

### Aha Moments
-

### Challenges Encountered
-

### How This Compares to PowerShell
-

## Practical Applications

### How I'll Use This
-

### Relevant to My Work
-

## Questions/Confusion
-

## Next Lesson Preview
**Topic:** [Next lesson topic]
**Why I'm interested:**

---

*Note: Be honest in reflections. Confusion is part of learning.*
```

### Code Quality Standards

#### PowerShell Examples
- Follow verb-noun naming conventions
- Use Comment-Based Help
- Include error handling examples where relevant
- Show enterprise patterns (not script kiddie code)
- Use Australian/British English spelling in comments

#### Python Examples
- Follow PEP 8 style guide
- Use type hints where appropriate (introduce gradually)
- Include docstrings (Google/NumPy style)
- Show Pythonic idioms
- Use Australian/British English spelling in comments and strings

### Common Patterns to Implement

#### Pattern 1: Variable Assignment Comparison

**PowerShell:**
```powershell
# Strongly typed variable
[string]$Name = "Matt"

# Type inference
$Count = 42
```

**Python:**
```python
# Type hints (optional but recommended)
name: str = "Matt"

# Type inference (more common)
count = 42
```

#### Pattern 2: Function Definition Comparison

**PowerShell:**
```powershell
function Get-UserInfo {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory=$true)]
        [string]$Username,

        [Parameter(Mandatory=$false)]
        [switch]$IncludeDetails
    )

    # Function body
}
```

**Python:**
```python
def get_user_info(username: str, include_details: bool = False) -> dict:
    """
    Retrieve user information.

    Args:
        username: The username to query
        include_details: Whether to include detailed information

    Returns:
        Dictionary containing user information
    """
    # Function body
    pass
```

## Lesson Catalogue

### Module 01: Variables and Types (15 min)
**Learning Objectives:**
- Understand Python's dynamic typing vs PowerShell's type system
- Learn variable naming conventions (snake_case vs PascalCase)
- Master string operations and formatting
- Work with numbers (int, float vs [int], [double])

**PowerShell Concepts Covered:**
- Variable declaration with type constraints
- String interpolation with `"$Variable"`
- Type casting with `[type]`

**Python Equivalents:**
- Dynamic typing with optional type hints
- f-strings and format()
- Type conversion functions

**Key Comparison:**
```
PowerShell: $myVariable = "value"
Python:     my_variable = "value"
```

---

### Module 02: Functions and Parameters (20 min)
**Learning Objectives:**
- Convert PowerShell functions to Python functions
- Understand parameter handling differences
- Learn default parameters and keyword arguments
- Master return values and multiple returns

**PowerShell Concepts Covered:**
- `[CmdletBinding()]` and advanced functions
- Parameter attributes and validation
- `param()` blocks
- Pipeline input

**Python Equivalents:**
- Function signatures with type hints
- `*args` and `**kwargs`
- Decorators (introduce basics)
- Return tuples vs PSCustomObject

**Key Comparison:**
```
PowerShell: function Verb-Noun { param($Name) }
Python:     def verb_noun(name: str) -> None:
```

---

### Module 03: Collections - Lists (25 min)
**Learning Objectives:**
- Convert PowerShell arrays to Python lists
- Master list comprehensions vs Where-Object
- Understand mutable vs immutable collections
- Learn list methods and operations

**PowerShell Concepts Covered:**
- Array declaration `@()`
- Array operations and indexing
- `ForEach-Object` and `Where-Object`
- Array addition and manipulation

**Python Equivalents:**
- List literals `[]`
- List comprehensions
- Slicing operations
- List methods (append, extend, pop)

**Key Comparison:**
```
PowerShell: $Array = @(1, 2, 3); $Array += 4
Python:     array = [1, 2, 3]; array.append(4)
```

---

### Module 04: Collections - Dictionaries (25 min)
**Learning Objectives:**
- Convert PowerShell hashtables to Python dictionaries
- Master dictionary operations and methods
- Understand key-value pair manipulation
- Learn dictionary comprehensions

**PowerShell Concepts Covered:**
- Hashtable declaration `@{}`
- Key-value access
- PSCustomObject vs Hashtable
- Ordered dictionaries

**Python Equivalents:**
- Dict literals `{}`
- Dictionary methods (get, keys, values, items)
- Dict comprehensions
- OrderedDict and dataclasses (preview)

**Key Comparison:**
```
PowerShell: $Hash = @{ Name = "Matt"; Role = "Dev" }
Python:     hash_dict = {"name": "Matt", "role": "Dev"}
```

---

### Module 05: Control Flow - Conditionals (20 min)
**Learning Objectives:**
- Convert if/elseif/else to Python conditionals
- Understand truthy/falsy values
- Learn ternary operators
- Master match/case (Python 3.10+) vs switch

**PowerShell Concepts Covered:**
- `if`, `elseif`, `else`
- `switch` statements
- Comparison operators `-eq`, `-ne`, `-gt`
- Logical operators `-and`, `-or`, `-not`

**Python Equivalents:**
- `if`, `elif`, `else`
- `match`/`case` statements
- Comparison operators `==`, `!=`, `>`
- Logical operators `and`, `or`, `not`

**Key Comparison:**
```
PowerShell: if ($Value -eq 10) { }
Python:     if value == 10:
```

---

### Module 06: Control Flow - Loops (25 min)
**Learning Objectives:**
- Convert ForEach-Object to Python loops
- Master for loops and while loops
- Understand enumerate() vs indexed loops
- Learn loop control (break, continue)

**PowerShell Concepts Covered:**
- `foreach ($item in $collection)`
- `ForEach-Object { $_ }`
- `while` and `do-while`
- `break` and `continue`

**Python Equivalents:**
- `for item in collection:`
- `while` loops
- `enumerate()` for index access
- `break` and `continue`

**Key Comparison:**
```
PowerShell: foreach ($item in $items) { }
Python:     for item in items:
```

---

### Module 07: File Operations (30 min)
**Learning Objectives:**
- Convert Get-Content/Set-Content to Python file I/O
- Understand context managers (with statement)
- Learn path operations (pathlib vs Join-Path)
- Master file reading/writing patterns

**PowerShell Concepts Covered:**
- `Get-Content`, `Set-Content`
- `Test-Path`, `New-Item`
- `Join-Path` and path manipulation
- File system providers

**Python Equivalents:**
- `open()` and file objects
- Context managers (`with` statement)
- `pathlib.Path`
- File methods (read, write, readlines)

**Key Comparison:**
```
PowerShell: Get-Content -Path $file
Python:     with open(file) as f: content = f.read()
```

---

### Module 08: Error Handling (25 min)
**Learning Objectives:**
- Convert try/catch to Python try/except
- Understand exception types
- Learn error handling best practices
- Master custom exceptions

**PowerShell Concepts Covered:**
- `try`, `catch`, `finally`
- `$Error` automatic variable
- `-ErrorAction` parameter
- Custom error types

**Python Equivalents:**
- `try`, `except`, `finally`
- Exception hierarchy
- `raise` statements
- Custom exception classes

**Key Comparison:**
```
PowerShell: try { } catch [System.Exception] { }
Python:     try: ... except Exception as e:
```

---

### Module 09: REST APIs and JSON (30 min)
**Learning Objectives:**
- Convert Invoke-RestMethod to requests library
- Master JSON serialisation/deserialisation
- Understand HTTP methods and headers
- Learn authentication patterns

**PowerShell Concepts Covered:**
- `Invoke-RestMethod`
- `ConvertFrom-Json`, `ConvertTo-Json`
- Authentication headers
- API response handling

**Python Equivalents:**
- `requests` library
- `json.loads()`, `json.dumps()`
- Session objects and auth
- Response objects

**Key Comparison:**
```
PowerShell: Invoke-RestMethod -Uri $url -Method Get
Python:     response = requests.get(url)
```

**Practical Application:**
This lesson directly prepares for Atlassian API integration in the final project.

---

### Module 10: Modules and Packages (25 min)
**Learning Objectives:**
- Convert PowerShell modules to Python packages
- Understand import systems
- Learn virtual environments
- Master package management (pip vs PowerShell Gallery)

**PowerShell Concepts Covered:**
- Module manifest (.psd1)
- `Import-Module`
- Module structure and functions
- PowerShell Gallery

**Python Equivalents:**
- `__init__.py` and packages
- `import` statements
- `venv` and virtual environments
- `pip` and PyPI

**Key Comparison:**
```
PowerShell: Import-Module MyModule
Python:     import my_module
```

---

### Module 99: Final Project - Jira API Client (Multi-lesson)

**Project Overview:**
Build a command-line Jira API client that demonstrates all learned concepts.

**Features to Implement:**
1. Authentication with Atlassian API
2. Retrieve and display issues
3. Create new issues
4. Update issue status
5. Error handling and logging
6. Configuration file management

**Lessons:**
- **99.1:** Project setup and structure (15 min)
- **99.2:** Authentication and configuration (20 min)
- **99.3:** Issue retrieval and display (25 min)
- **99.4:** Issue creation and updates (30 min)
- **99.5:** Error handling and refinement (20 min)
- **99.6:** Documentation and packaging (15 min)

**Learning Objectives:**
- Apply all learned concepts in real-world context
- Build professional Python application
- Create reusable code for Atlassian work
- Develop portfolio-worthy project

## Special Instructions for Claude Code

### When Starting a New Lesson

1. **Verify current progress:**
   ```markdown
   Check README.md to confirm which lesson to create next
   ```

2. **Create lesson directory:**
   ```bash
   mkdir [XX_Lesson_Name]/
   ```

3. **Generate all 5 required files:**
   - `lesson.md` (theory and comparison)
   - `powershell_examples.ps1` (reference code)
   - `python_examples.py` (Python equivalents)
   - `exercises.md` (practice problems)
   - `lessons_learned.md` (template only - learner completes)

4. **Update README.md:**
   - Add lesson to progress tracker
   - Set status to "🔄 In Progress"
   - Update last modified date

5. **Create learning branch:**
   ```bash
   git checkout -b learning/lesson-XX
   ```

### Lesson Content Guidelines

**DO:**
- Make direct PowerShell → Python comparisons
- Use realistic enterprise scenarios
- Include practical, work-relevant examples
- Explain WHY Python does things differently
- Highlight common pitfalls for PowerShell developers
- Use Australian/British English spelling
- Keep lessons focused (15-30 min completion time)

**DON'T:**
- Assume prior Python knowledge
- Use trivial "Hello World" examples exclusively
- Ignore PowerShell context
- Overwhelm with advanced topics too early
- Use American English spelling
- Create lessons longer than 30 minutes

### Exercise Creation Guidelines

**Exercise Difficulty Progression:**

**Easy (Exercise 1):**
- Direct syntax conversion
- Single concept application
- Provided PowerShell code to convert
- Expected output shown

**Medium (Exercise 2):**
- Problem-solving using lesson concepts
- Minimal scaffolding
- Scenario-based (e.g., "Parse this API response")
- Hints provided

**Advanced (Exercise 3):**
- Integrate multiple concepts
- Open-ended solution
- Real-world complexity
- Success criteria rather than step-by-step

**Bonus (Optional):**
- Extension of advanced exercise
- Introduces preview of future concepts
- Encourages experimentation

### Code Example Requirements

**Every code example must:**
1. Be runnable without modification
2. Include clear comments
3. Show output in comments or docstrings
4. Follow style guidelines (PEP 8 for Python, Verb-Noun for PowerShell)
5. Be practical (no foo/bar examples)

**Example Quality Check:**
```python
# BAD: Too simplistic
x = 5
print(x)

# GOOD: Practical and relatable
"""
Convert Atlassian API timestamp to readable date.
PowerShell equivalent: Get-Date -Format "yyyy-MM-dd"
"""
from datetime import datetime

api_timestamp = "2026-01-29T10:30:00.000+1100"
parsed_date = datetime.fromisoformat(api_timestamp)
readable = parsed_date.strftime("%Y-%m-%d")
print(f"Issue created: {readable}")  # Output: Issue created: 2026-01-29
```

### Progress Tracking Automation

After each lesson completion:

1. **Learner creates lessons_learned.md**
2. **Claude Code updates README.md:**
   ```markdown
   | XX | Topic Name | ✅ Complete | YYYY-MM-DD | [Key insight from lessons_learned] |
   ```

3. **Commit with descriptive message:**
   ```bash
   git add .
   git commit -m "lesson: Complete XX - Topic Name"
   ```

4. **Merge to main when ready:**
   ```bash
   git checkout main
   git merge learning/lesson-XX
   git push origin main
   ```

### Handling Learner Questions

When the learner asks for clarification:

1. **Reference the comparison pattern:**
   - Show PowerShell way first
   - Explain Python equivalent
   - Highlight key difference

2. **Provide additional examples:**
   - Create supplementary code in lesson directory
   - Name files clearly (e.g., `extra_example_dictionaries.py`)

3. **Update lesson.md if needed:**
   - Add "Additional Notes" section
   - Don't recreate entire file
   - Append clarifications

### Common Scenarios

#### Scenario 1: Learner stuck on exercise

**Response pattern:**
1. Ask what they've tried
2. Provide hint, not solution
3. If still stuck, show PowerShell equivalent
4. Guide to Python translation
5. Only provide solution as last resort

#### Scenario 2: Learner wants to skip ahead

**Response pattern:**
1. Confirm prerequisite lessons completed
2. Warn about concept dependencies
3. Allow skip but note in README.md
4. Suggest return later for review

#### Scenario 3: Learner requests custom example

**Response pattern:**
1. Create example in current lesson directory
2. Use format: `custom_example_[topic].py` and `.ps1`
3. Maintain comparison pattern
4. Commit separately

#### Scenario 4: Learner finds error in lesson

**Response pattern:**
1. Acknowledge and thank for feedback
2. Fix immediately
3. Update lesson files
4. Commit with: `fix: Correct [issue] in lesson XX`
5. Note in README.md if significant

## README.md Template

When creating the initial README.md, use this structure:

```markdown
# Python Learning Journey for PowerShell Developers

A structured learning path for experienced PowerShell developers transitioning to Python.

## About This Repository

This repository contains a complete learning curriculum designed specifically for PowerShell developers. Each lesson directly compares PowerShell concepts with Python equivalents, making the transition smooth and intuitive.

**Learning Duration:** 15-30 minutes per lesson
**Total Lessons:** 25+
**Final Project:** Jira API Client

## Learning Progress

| Module | Lesson | Status | Completed | Notes |
|--------|--------|--------|-----------|-------|
| 01 | Variables and Types | ⬜ Not Started | - | - |
| 02 | Functions and Parameters | ⬜ Not Started | - | - |
| 03 | Collections - Lists | ⬜ Not Started | - | - |
| 04 | Collections - Dictionaries | ⬜ Not Started | - | - |
| 05 | Control Flow - Conditionals | ⬜ Not Started | - | - |
| 06 | Control Flow - Loops | ⬜ Not Started | - | - |
| 07 | File Operations | ⬜ Not Started | - | - |
| 08 | Error Handling | ⬜ Not Started | - | - |
| 09 | REST APIs and JSON | ⬜ Not Started | - | - |
| 10 | Modules and Packages | ⬜ Not Started | - | - |
| 99 | Final Project: Jira Client | ⬜ Not Started | - | - |

**Legend:**
- ⬜ Not Started
- 🔄 In Progress
- ✅ Complete
- ⚠️ Needs Review

## Repository Structure

Each lesson follows this pattern:

```
XX_Lesson_Name/
├── lesson.md               # Theory and PowerShell comparison
├── powershell_examples.ps1 # PowerShell reference code
├── python_examples.py      # Python equivalent code
├── exercises.md            # Practice problems
└── lessons_learned.md      # Your reflections (complete after lesson)
```

## How to Use This Repository

1. **Start with lesson 01** - lessons build on each other
2. **Read lesson.md** - understand the concept comparison
3. **Study the examples** - compare PowerShell and Python side-by-side
4. **Complete exercises** - practice makes perfect
5. **Document learnings** - fill in lessons_learned.md
6. **Update progress** - mark lesson complete in this README
7. **Commit your work** - track your progress with git

## Prerequisites

- PowerShell experience (intermediate to advanced)
- Python 3.10+ installed
- Git basics
- Text editor or IDE (VS Code recommended)

## Learning Tips

- **Don't rush** - 15-30 minutes per lesson is intentional
- **Do the exercises** - reading isn't learning, doing is
- **Reflect honestly** - lessons_learned.md is for you
- **Ask questions** - use issues or discussions
- **Compare constantly** - leverage your PowerShell knowledge

## Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [PowerShell vs Python Quick Reference](link-to-resource)
- [Atlassian REST API Documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/)

## Final Project

The learning path culminates in building a real Jira API client that you can use in your work. This project integrates all concepts learned and produces portfolio-worthy code.

---

**Last Updated:** 2026-01-29
**Current Lesson:** Not started
**Total Time Invested:** 0 hours
```

## Troubleshooting

### Issue: Lesson Too Long

**Symptoms:** Lesson takes >30 minutes to complete
**Solution:**
1. Split into two lessons (XX.1 and XX.2)
2. Move advanced topics to bonus section
3. Simplify examples without losing value
4. Remove tangential information

### Issue: Exercise Too Difficult

**Symptoms:** Learner stuck for >15 minutes
**Solution:**
1. Add intermediate hints
2. Provide PowerShell reference code
3. Break into smaller sub-exercises
4. Create supplementary examples

### Issue: Python Concept Has No PowerShell Equivalent

**Symptoms:** Struggling to create comparison
**Solution:**
1. Explain why PowerShell doesn't have this
2. Show closest PowerShell approximation
3. Explain Python's design rationale
4. Provide context for when this is useful

### Issue: Unclear Progress State

**Symptoms:** README.md doesn't reflect actual progress
**Solution:**
1. Check lessons_learned.md files (if exists = completed)
2. Look at git commit history
3. Ask learner directly
4. Update README.md to match reality

## Updates to This Document

This CLAUDE.md should be updated when:

- New lesson patterns are established
- Common issues are identified
- Learner feedback suggests improvements
- Repository structure changes
- Additional modules are added
- Python version requirements change

---

**Last Updated:** 2026-01-29
**Python Version:** 3.10+
**Target Audience:** Experienced PowerShell Developers
**Maintained By:** AI Assistant (Claude Code) + Matt (Learner)
