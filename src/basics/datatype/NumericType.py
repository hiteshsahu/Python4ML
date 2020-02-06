"""
Numeric Data Type(bool):

- int     :  -N, 0 , +N,  Hexa, Octa Decimal
- float   :  -N.N, 0, +N.N or with e
- complex :  N+iN

Casting:

 int(x):

Type long(x) to convert x to a long integer.

Type float(x) to convert x to a floating-point number.

Type complex(x) to convert x to a complex number with real part x and imaginary part zero.

Type complex(x, y) to convert x and y to a complex number with real part x and imaginary part y. x and y are numeric expressions
"""

import sys
from math import pi, e

intVar = -299         # int : plus minus without decimal
intHex = 0xA0F         #Hexa-decimal
intOct = 0o37          #Octal

floatVar = pi     # Float : plus minus with decimal
floatVarSci = 3e2  # Float with more precision

complexVar = e + 5j  # Complex: a+ij

# Type Checking
print("\n -----------Checking--------")
print(type(intVar), "is Integer? ", isinstance(intVar, int))
print(type(intHex), "is Integer? ", isinstance(intHex, int))
print(type(intOct), "is Integer? ", isinstance(intOct, int))

print(type(floatVar), "is Float? ", isinstance(floatVar, float))
print(type(floatVarSci), "is Float? ", isinstance(floatVarSci, float))
print(type(complexVar), "is Complex? ", isinstance(complexVar, complex))

# TypeCasting

print("\n -----------Casting--------")
print("Before", intVar, "After", float(intVar))   # int to float:add decimal
print("Before", intOct, "After", float(intOct))   # int to float:add decimal
print("Before", intHex, "After", float(intHex))   # int to float:add decimal
print("Before", intVar, "After", complex(intVar))  # int to complex:

print("Before", floatVar, "After", int(floatVar))         # float to int: lose precision
print("Before", floatVarSci, "After", int(floatVarSci))   # float to int: lose precision
print("Before", intVar, "After", complex(floatVar, floatVarSci))  # float to complex:
print("Before", intVar, "After", complex(intVar, floatVar))  # int & float to complex with 2 params:

# Cant Cast Complex to Int or float
try:
    print("Before", complexVar, "After", int(complexVar))
except TypeError:
    print("Oops! No valid casting :", sys.exc_info())


# Convert float to String , Concat String with Numbers
print("Before", floatVar, "After", "" + str(floatVar))

