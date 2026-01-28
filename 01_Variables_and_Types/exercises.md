# Exercises: Variables and Types

Complete these exercises to practice Python variables and data types. Save your solutions in a file called `solutions.py` in this directory.

---

## Exercise 1: Easy - Basic Variable Conversion

**PowerShell Reference:**
```powershell
# Convert this PowerShell code to Python

[string]$FirstName = "Matt"
[string]$LastName = "Lock"
[int]$YearsExperience = 8
[string]$Department = "IT Operations"

$FullName = "$FirstName $LastName"
$Profile = "Employee: $FullName | Department: $Department | Experience: $YearsExperience years"

Write-Host $Profile
```

**Your Task:**
Convert this PowerShell code to Python. Use appropriate variable naming conventions (snake_case) and f-strings for interpolation.

**Expected Output:**
```
Employee: Matt Lock | Department: IT Operations | Experience: 8 years
```

**Hints:**
- Remember: no `$` prefix in Python
- Use `snake_case` for variable names
- Use f-strings (f"...") for string interpolation

---

## Exercise 2: Medium - Jira Issue Formatter

**Scenario:**
You're building a script to format Jira issue data for a daily standup report. You receive the following data as strings (as you might from an API) and need to convert and format them appropriately.

**Input Data (as strings):**
```python
issue_key_raw = "DEVOPS-4521"
summary_raw = "Deploy new monitoring stack"
story_points_raw = "8"
hours_logged_raw = "12.5"
is_blocked_raw = "false"
created_date_raw = "2026-01-20"
```

**Requirements:**
1. Create properly typed variables from the raw string data
2. Convert `story_points_raw` to an integer
3. Convert `hours_logged_raw` to a float
4. Convert `is_blocked_raw` to a boolean (handle "true"/"false" strings correctly)
5. Calculate remaining effort: `story_points * 2 - hours_logged` (assuming 2 hours per story point)
6. Create a formatted summary string

**Expected Output:**
```
=== Daily Standup Update ===
Issue:        DEVOPS-4521
Summary:      Deploy new monitoring stack
Story Points: 8
Hours Logged: 12.5
Blocked:      No
Remaining:    3.5 hours
```

**Hints:**
- For boolean conversion from string, compare: `is_blocked_raw.lower() == "true"`
- Use f-strings with formatting: `f"{value:.1f}"` for one decimal place
- Use conditional expression for "Yes"/"No": `"Yes" if condition else "No"`

---

## Exercise 3: Advanced - Configuration Parser

**Challenge:**
Create a simple configuration parser that processes server connection details. This simulates reading configuration from environment variables or a config file.

**Requirements:**

1. Define these configuration variables with type hints:
   - `server_host` (string): "jira.company.com"
   - `server_port` (integer): 443
   - `use_ssl` (boolean): True
   - `timeout_seconds` (float): 30.0
   - `max_retries` (integer): 3
   - `api_version` (string): "v3"

2. Create a function-like structure (we'll learn proper functions next lesson) that builds a connection URL:
   - If `use_ssl` is True, use "https://", otherwise "http://"
   - Include the port only if it's not the default (443 for https, 80 for http)
   - Append the API version path

3. Create a configuration summary showing all values and their types

4. Demonstrate type checking using `isinstance()` for at least 3 variables

**Expected Output:**
```
=== Server Configuration ===
Host:         jira.company.com (str)
Port:         443 (int)
SSL:          True (bool)
Timeout:      30.0 seconds (float)
Max Retries:  3 (int)
API Version:  v3 (str)

Connection URL: https://jira.company.com/v3
(Port 443 omitted - default for HTTPS)

Type Validation:
- server_host is str: True
- server_port is int: True
- use_ssl is bool: True
```

**Success Criteria:**
- All variables have appropriate type hints
- URL is correctly constructed based on SSL and port
- Type checking demonstrates `isinstance()` usage
- Output is clearly formatted

---

## Bonus Challenge: Type-Safe Configuration Validator

**Extension of Exercise 3:**

Create a validation system that:

1. Accepts configuration as a dictionary of strings (simulating raw config file data):
```python
raw_config = {
    "host": "jira.company.com",
    "port": "443",
    "ssl": "true",
    "timeout": "30.0",
    "retries": "3"
}
```

2. Converts each value to the appropriate type
3. Validates that:
   - Port is between 1 and 65535
   - Timeout is positive
   - Retries is between 0 and 10
4. Reports any validation errors
5. Returns a "clean" configuration with proper types

**Expected Output (valid config):**
```
Configuration Valid!
Parsed Configuration:
- host: jira.company.com (str)
- port: 443 (int) ✓
- ssl: True (bool)
- timeout: 30.0 (float) ✓
- retries: 3 (int) ✓
```

**Expected Output (invalid config with port = "99999"):**
```
Configuration Errors:
- port: 99999 is out of valid range (1-65535)

Parsed Configuration (with errors):
- host: jira.company.com (str)
- port: 99999 (int) ✗
- ssl: True (bool)
- timeout: 30.0 (float) ✓
- retries: 3 (int) ✓
```

**Hints:**
- Use try/except for type conversion (we'll cover this properly in Module 08, but you can preview it here)
- Store validation results in a list
- This exercise previews dictionaries (Module 04) - it's okay to look ahead!

---

## Solution Check

After completing the exercises, verify your solutions:

1. **Exercise 1:** Does your output match exactly?
2. **Exercise 2:** Are all types correctly converted? Is the boolean handled properly?
3. **Exercise 3:** Does the URL construction handle both SSL and non-SSL cases?
4. **Bonus:** Does validation catch invalid values?

Remember: The goal is not just to get the output right, but to understand HOW Python handles variables and types differently from PowerShell.

---

*When you've completed these exercises, document your learnings in `lessons_learned.md`*
