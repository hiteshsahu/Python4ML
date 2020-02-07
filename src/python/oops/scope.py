"""
Python has 2 Types of SCOPE : Global & Local
Global Scope:
- Variable created in the main body or with keyword "global"
- Available to all scope, global and local.

Local Scope:
- Variable created inside a function,
- Available only inside that function.
"""

total = 0  # Global variable.


def addNumber(num1, num2):
    total = num1 + num2  # total is local variable.
    global sum  # Force Global
    sum = total
    print("Inside the function local total : ", total)
    return total


addNumber(10, 20)
print("Outside function  total: ", total)
print("Outside function  sum: ", sum)
