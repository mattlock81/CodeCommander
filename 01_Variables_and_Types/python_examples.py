"""
Python examples for Variables and Types

Reference implementation showing Python approach to variables and data types.
Compare with powershell_examples.ps1 to see the PowerShell equivalents.

Module: 01 - Variables and Types
Compare: powershell_examples.ps1
"""

from datetime import datetime

# =============================================================================
# Example 1: Basic Variable Declaration
# =============================================================================
# Python uses no prefix for variables - just the name
# Variables ARE case-sensitive (name and Name are DIFFERENT)
# Convention: use snake_case for variable names

username = "mlock"
display_name = "Matt Lock"
ticket_count = 15

# Output the values
# PowerShell: Write-Host "Username: $Username"
print(f"Username: {username}")
print(f"Display Name: {display_name}")
print(f"Ticket Count: {ticket_count}")

# =============================================================================
# Example 2: Type-Hinted Variables
# =============================================================================
# Type hints are OPTIONAL and NOT enforced at runtime
# They serve as documentation and enable IDE support
# PowerShell [type] enforces; Python type hints do not

project_name: str = "Jira Migration"
issue_count: int = 142
is_complete: bool = False
due_date: datetime = datetime(2026, 2, 28)

# Unlike PowerShell, this WON'T raise an error (type hints aren't enforced):
# issue_count: int = "not a number"  # Python allows this!

print(f"\nProject: {project_name}")
print(f"Issues: {issue_count}")
print(f"Complete: {is_complete}")
print(f"Due: {due_date.strftime('%Y-%m-%d')}")

# =============================================================================
# Example 3: String Interpolation and Formatting
# =============================================================================
# Python f-strings (f"...") are similar to PowerShell double quotes
# Regular strings don't interpolate - you MUST use the f prefix
# Single and double quotes are interchangeable in Python

server_name = "ATLPROD01"
environment = "Production"
port = 8080

# f-string - variables are interpolated (like PowerShell double quotes)
# PowerShell: $ConnectionString = "https://$ServerName`:$Port"
connection_string = f"https://{server_name}:{port}"
print(f"\nConnection: {connection_string}")

# Regular string - NO interpolation (different from PowerShell single quotes)
# In Python, single and double quotes behave the same
literal_example = "The variable is {server_name}"  # No f prefix = no interpolation
print(f"Literal: {literal_example}")

# Expressions inside f-strings (like PowerShell subexpressions)
# PowerShell: "Server has $($Port + 1) backup port"
message = f"Server {server_name} in {environment} has {port + 1} backup port"
print(message)

# Multi-line string with triple quotes (like PowerShell here-strings)
# PowerShell: @" ... "@
json_payload = f"""{{
    "server": "{server_name}",
    "environment": "{environment}",
    "port": {port}
}}"""
print("\nJSON Payload:")
print(json_payload)

# =============================================================================
# Example 4: Type Conversion and Casting
# =============================================================================
# Python uses type functions for conversion: int(), str(), float(), bool()
# PowerShell uses [type] syntax
# Useful when processing API responses or user input

string_number = "42"
string_decimal = "19.99"
string_bool = "true"

# Convert string to integer
# PowerShell: [int]$StringNumber
converted_int = int(string_number)
print(f"\nConverted Int: {converted_int} (Type: {type(converted_int).__name__})")

# Convert string to float (like PowerShell [double])
# PowerShell: [double]$StringDecimal
converted_float = float(string_decimal)
print(f"Converted Float: {converted_float} (Type: {type(converted_float).__name__})")

# Convert string to boolean - NOTE: Python bool() works differently!
# PowerShell: [bool]"true" -> True
# Python: bool("true") -> True (any non-empty string is True)
# Python: bool("false") -> True (still True because string is not empty!)
# For string "true"/"false", you need explicit comparison:
converted_bool = string_bool.lower() == "true"
print(f"Converted Bool: {converted_bool} (Type: {type(converted_bool).__name__})")

# Convert number back to string
# PowerShell: [string]$ConvertedInt
back_to_string = str(converted_int)
print(f"Back to String: '{back_to_string}' (Type: {type(back_to_string).__name__})")

# =============================================================================
# Example 5: Working with Jira-Style Data (Enterprise Example)
# =============================================================================
# Simulating data you might receive from Atlassian APIs
# Demonstrates practical variable usage in enterprise context

issue_key: str = "PROJ-1234"
summary: str = "Implement user authentication"
status: str = "In Progress"
assignee: str = "mlock"
story_points: int = 5
created: datetime = datetime(2026, 1, 15, 9, 30, 0)
updated: datetime = datetime.now()

# Calculate days since creation
# PowerShell: (New-TimeSpan -Start $Created -End $Updated).Days
days_open = (updated - created).days

# Build a formatted summary (like you might log or display)
# Using triple-quoted f-string for multi-line
issue_summary = f"""
=== JIRA Issue Details ===
Key:          {issue_key}
Summary:      {summary}
Status:       {status}
Assignee:     {assignee}
Story Points: {story_points}
Created:      {created.strftime('%Y-%m-%d %H:%M')}
Days Open:    {days_open}
"""

print(issue_summary)

# =============================================================================
# Example 6: Type Checking
# =============================================================================
# Verify types before processing - important for robust scripts
# PowerShell uses -is operator; Python uses isinstance()

test_value = 42

# Check if value is a specific type
# PowerShell: if ($TestValue -is [int])
if isinstance(test_value, int):
    print(f"\n{test_value} is an integer")

# Get the type name
# PowerShell: $TestValue.GetType().Name
type_name = type(test_value).__name__
print(f"Type name: {type_name}")

# Check against multiple types
# Note: Python has no direct $null equivalent in a list - we use None
values = ["hello", 42, 3.14, True, None]
for value in values:
    # PowerShell: if ($null -eq $Value) { "null" } else { $Value.GetType().Name }
    type_str = "NoneType" if value is None else type(value).__name__
    print(f"Value: '{value}' is type: {type_str}")

# =============================================================================
# Summary: Key Python Patterns for Variables
# =============================================================================
"""
Key takeaways compared to PowerShell:
1. No prefix needed for variables (no $ sign)
2. Type hints are documentation only - they don't enforce types
3. f-strings interpolate, regular strings don't (both quote types same)
4. Variables ARE case-sensitive (name != Name != NAME)
5. None represents absence of value (PowerShell uses $null)
6. Use isinstance() for type checking (PowerShell uses -is operator)
7. Use type() to get the type (PowerShell uses .GetType())
"""
