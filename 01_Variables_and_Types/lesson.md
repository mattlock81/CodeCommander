# 01: Variables and Types

Welcome to your first Python lesson! As an experienced PowerShell developer, you already understand variables and data types. This lesson will show you how Python handles these familiar concepts differently.

**Estimated Time:** 15 minutes

## PowerShell Context

In PowerShell, you're accustomed to:

```powershell
# Variable declaration with $ prefix
$Name = "Matt"

# Optional type constraints
[string]$Username = "mlock"
[int]$Count = 42

# String interpolation
$Message = "Hello, $Name! You have $Count items."

# Type casting
$Number = [int]"42"
$Text = [string]123
```

PowerShell uses the `$` prefix for all variables and supports optional type constraints using `[type]` syntax. Variables are case-insensitive (`$name` and `$Name` are the same).

## Python Equivalent

Python takes a different approach:

```python
# Variable declaration - no prefix needed
name = "Matt"

# Type hints (optional, for documentation)
username: str = "mlock"
count: int = 42

# String interpolation with f-strings
message = f"Hello, {name}! You have {count} items."

# Type conversion using functions
number = int("42")
text = str(123)
```

Python variables have no prefix, use `snake_case` naming by convention, and are **case-sensitive** (`name` and `Name` are different variables).

## Key Differences

| Aspect | PowerShell | Python |
|--------|------------|--------|
| Variable prefix | `$` required | None |
| Naming convention | `$PascalCase` or `$camelCase` | `snake_case` |
| Case sensitivity | Case-insensitive | Case-sensitive |
| Type constraints | `[type]$Var` (enforced) | `var: type` (hints only, not enforced) |
| String interpolation | `"Hello, $Name"` | `f"Hello, {name}"` |
| Type conversion | `[type]$value` | `type(value)` |
| Null/None | `$null` | `None` |

## Core Data Types Comparison

### Strings

| PowerShell | Python | Notes |
|------------|--------|-------|
| `[string]` | `str` | Immutable in both |
| `"double quotes"` | `"double"` or `'single'` | Python treats both the same |
| `'literal string'` | `r"raw string"` | Python raw strings for regex/paths |
| `` `n `` (backtick n) | `\n` | Newline character |

### Numbers

| PowerShell | Python | Notes |
|------------|--------|-------|
| `[int]` | `int` | Integers |
| `[double]` | `float` | Floating point |
| `[decimal]` | `decimal.Decimal` | Precise decimals (import required) |
| `1KB`, `1MB`, `1GB` | No equivalent | Calculate manually: `1024`, `1024**2` |

### Booleans

| PowerShell | Python | Notes |
|------------|--------|-------|
| `$true` | `True` | Capital T |
| `$false` | `False` | Capital F |
| `$null` | `None` | Capital N |

## When to Use What

### Use Type Hints When:
- Writing functions that others will use
- Working on larger projects
- You want IDE autocompletion and error checking
- Documenting expected data types

### Skip Type Hints When:
- Writing quick scripts
- Prototyping ideas
- The type is obvious from context

```python
# Type hint helpful - not obvious what's expected
def process_user(user_id: int, include_details: bool = False) -> dict:
    pass

# Type hint less necessary - obvious from context
name = "Matt"
count = 42
```

## Common Gotchas for PowerShell Developers

### 1. Case Sensitivity Catches You Out

```python
# These are THREE different variables!
Name = "Matt"
name = "matt"
NAME = "MATT"

print(Name)  # Matt
print(name)  # matt
print(NAME)  # MATT
```

**PowerShell habit to break:** Assuming `$name` and `$Name` are the same.

### 2. Type Hints Don't Enforce Types

```python
# This WON'T raise an error - type hints are just documentation
age: int = "twenty-five"  # Python allows this!
print(age)  # Output: twenty-five
```

**PowerShell habit to break:** Expecting `[int]$age` behaviour where assignment fails if types don't match.

### 3. No Variable Declaration Required

```python
# This creates the variable - no declaration needed
username = "mlock"

# But referencing an undefined variable raises an error
print(undefined_var)  # NameError: name 'undefined_var' is not defined
```

### 4. String Quotes Are Interchangeable

```python
# These are identical in Python
name1 = "Matt"
name2 = 'Matt'

# Use the other quote type to include quotes in strings
message = "He said 'hello'"
html = '<div class="container">'
```

**PowerShell difference:** In PowerShell, single quotes are literal (no interpolation), double quotes allow interpolation.

### 5. f-strings Require the `f` Prefix

```python
name = "Matt"

# WRONG - no interpolation happens
message = "Hello, {name}"
print(message)  # Output: Hello, {name}

# CORRECT - f-string interpolates
message = f"Hello, {name}"
print(message)  # Output: Hello, Matt
```

## Practical Examples

### Example 1: Working with User Data

**PowerShell approach:**
```powershell
[string]$Username = "mlock"
[string]$DisplayName = "Matt Lock"
[int]$TicketCount = 15

$Summary = "User $Username ($DisplayName) has $TicketCount open tickets."
```

**Python equivalent:**
```python
username: str = "mlock"
display_name: str = "Matt Lock"
ticket_count: int = 15

summary = f"User {username} ({display_name}) has {ticket_count} open tickets."
```

### Example 2: Type Conversion

**PowerShell approach:**
```powershell
$InputString = "42"
$Number = [int]$InputString
$BackToString = [string]$Number
```

**Python equivalent:**
```python
input_string = "42"
number = int(input_string)
back_to_string = str(number)
```

### Example 3: Checking Types

**PowerShell approach:**
```powershell
$Value = 42
$Value.GetType().Name  # Int32
$Value -is [int]       # True
```

**Python equivalent:**
```python
value = 42
type(value).__name__  # 'int'
isinstance(value, int)  # True
```

## Quick Reference Card

```python
# Variables
my_variable = "value"           # Basic assignment
my_var: str = "typed"           # With type hint

# Strings
name = "Matt"                   # String literal
greeting = f"Hello, {name}"     # f-string interpolation
multiline = """Line 1
Line 2"""                       # Multi-line string

# Numbers
count = 42                      # Integer
price = 19.99                   # Float
big_number = 1_000_000          # Underscores for readability

# Booleans and None
is_active = True
is_deleted = False
empty_value = None

# Type conversion
int("42")                       # String to int
str(42)                         # Int to string
float("3.14")                   # String to float
bool(1)                         # To boolean (True)
bool(0)                         # To boolean (False)

# Type checking
type(value)                     # Get type
isinstance(value, int)          # Check type
```

## Next Steps

In the next lesson, **02: Functions and Parameters**, you'll learn how to convert PowerShell functions to Python. You'll see how `param()` blocks translate to function signatures, and how `[CmdletBinding()]` patterns compare to Python decorators.

---

**Ready to practice?** Head to `exercises.md` to apply what you've learned!
