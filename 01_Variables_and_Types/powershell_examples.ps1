<#
.SYNOPSIS
    PowerShell examples for Variables and Types

.DESCRIPTION
    Reference implementation showing PowerShell approach to variables and data types.
    Compare with python_examples.py to see the Python equivalents.

.NOTES
    Module: 01 - Variables and Types
    Author: Learning Repository
    Compare: python_examples.py
#>

# =============================================================================
# Example 1: Basic Variable Declaration
# =============================================================================
# PowerShell uses $ prefix for all variables
# Variables are case-insensitive ($Name and $name are the same)

$Username = "mlock"
$DisplayName = "Matt Lock"
$TicketCount = 15

# Output the values
Write-Host "Username: $Username"
Write-Host "Display Name: $DisplayName"
Write-Host "Ticket Count: $TicketCount"

# =============================================================================
# Example 2: Type-Constrained Variables
# =============================================================================
# Use [type] to enforce data types - assignment fails if types don't match
# This is useful for catching errors early in enterprise scripts

[string]$ProjectName = "Jira Migration"
[int]$IssueCount = 142
[bool]$IsComplete = $false
[datetime]$DueDate = "2026-02-28"

# Type constraint prevents invalid assignments
# Uncommenting the next line would cause an error:
# [int]$IssueCount = "not a number"  # Error: Cannot convert

Write-Host "`nProject: $ProjectName"
Write-Host "Issues: $IssueCount"
Write-Host "Complete: $IsComplete"
Write-Host "Due: $($DueDate.ToString('yyyy-MM-dd'))"

# =============================================================================
# Example 3: String Interpolation and Formatting
# =============================================================================
# Double quotes allow variable expansion
# Single quotes are literal (no expansion)

$ServerName = "ATLPROD01"
$Environment = "Production"
$Port = 8080

# Double quotes - variables are expanded
$ConnectionString = "https://$ServerName`:$Port"
Write-Host "`nConnection: $ConnectionString"

# Single quotes - literal string, no expansion
$LiteralExample = 'The variable is $ServerName'
Write-Host "Literal: $LiteralExample"

# Subexpression for complex expressions
$Message = "Server $ServerName in $Environment has $($Port + 1) backup port"
Write-Host $Message

# Here-string for multi-line text (useful for API payloads)
$JsonPayload = @"
{
    "server": "$ServerName",
    "environment": "$Environment",
    "port": $Port
}
"@
Write-Host "`nJSON Payload:"
Write-Host $JsonPayload

# =============================================================================
# Example 4: Type Conversion and Casting
# =============================================================================
# PowerShell uses [type] syntax for conversion
# Useful when processing API responses or user input

$StringNumber = "42"
$StringDecimal = "19.99"
$StringBool = "true"

# Convert string to integer
$ConvertedInt = [int]$StringNumber
Write-Host "`nConverted Int: $ConvertedInt (Type: $($ConvertedInt.GetType().Name))"

# Convert string to double (floating point)
$ConvertedDouble = [double]$StringDecimal
Write-Host "Converted Double: $ConvertedDouble (Type: $($ConvertedDouble.GetType().Name))"

# Convert string to boolean
$ConvertedBool = [bool]$StringBool
Write-Host "Converted Bool: $ConvertedBool (Type: $($ConvertedBool.GetType().Name))"

# Convert number back to string
$BackToString = [string]$ConvertedInt
Write-Host "Back to String: '$BackToString' (Type: $($BackToString.GetType().Name))"

# =============================================================================
# Example 5: Working with Jira-Style Data (Enterprise Example)
# =============================================================================
# Simulating data you might receive from Atlassian APIs
# Demonstrates practical variable usage in enterprise context

[string]$IssueKey = "PROJ-1234"
[string]$Summary = "Implement user authentication"
[string]$Status = "In Progress"
[string]$Assignee = "mlock"
[int]$StoryPoints = 5
[datetime]$Created = "2026-01-15T09:30:00"
[datetime]$Updated = Get-Date

# Calculate days since creation
$DaysOpen = (New-TimeSpan -Start $Created -End $Updated).Days

# Build a formatted summary (like you might log or display)
$IssueSummary = @"

=== JIRA Issue Details ===
Key:          $IssueKey
Summary:      $Summary
Status:       $Status
Assignee:     $Assignee
Story Points: $StoryPoints
Created:      $($Created.ToString('yyyy-MM-dd HH:mm'))
Days Open:    $DaysOpen
"@

Write-Host $IssueSummary

# =============================================================================
# Example 6: Type Checking
# =============================================================================
# Verify types before processing - important for robust scripts

$TestValue = 42

# Check if value is a specific type
if ($TestValue -is [int]) {
    Write-Host "`n$TestValue is an integer"
}

# Get the type name
$TypeName = $TestValue.GetType().Name
Write-Host "Type name: $TypeName"

# Check against multiple types
$Values = @("hello", 42, 3.14, $true, $null)
foreach ($Value in $Values) {
    $Type = if ($null -eq $Value) { "null" } else { $Value.GetType().Name }
    Write-Host "Value: '$Value' is type: $Type"
}

# =============================================================================
# Summary: Key PowerShell Patterns for Variables
# =============================================================================
<#
Key takeaways for Python comparison:
1. $ prefix is required for all variables
2. [type] constrains AND converts (Python type hints don't enforce)
3. Double quotes interpolate, single quotes are literal
4. Variables are case-insensitive
5. $null represents absence of value (Python uses None)
6. Use -is operator for type checking (Python uses isinstance())
#>
