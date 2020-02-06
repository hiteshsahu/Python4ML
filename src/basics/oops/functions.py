"""
Python Functions
- Must return a value or simply return to exit function
- Function Suite have local scope
- Argument are pass by Reference: Actually modify the input values
- Argument can have Default value use of =
- Argument order is important until you pass values like (ArgName = Argvalue ,...)
- Variable Length argument be can passed using *vartuple
"""

def printLogs(TAG, log ="Default Example", *tupleInfo):
    """Simple Function Demo"""
    print(TAG, ":", log)
    for info in tupleInfo:
        print(info)
    return

printLogs("FUN")
printLogs("FUN", "Required Example")
printLogs(TAG="FUN", log="Unordered Input Example")
printLogs(TAG="FUN", log="Unordered Input Example")
printLogs("FUN", "Varible Length Input Example","This", "Is", "AN", "Example")

"""Lamda Function : Anonymous function take any number of Arguments and return 1 value"""

addNumber = lambda num1, num2: num1+num2
print("Lamda Sum: ", addNumber(20, 30))

