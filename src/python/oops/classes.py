"""
Defining class and Objects
- Class Body must not be empty but can be ignore with the help of Pass
- self can be renamed to anything
- class_suite work as static, shared across all instances
-  class_suite can be accessed using ClassNAme.variable

Attr
-  Start with a lowercase letter or _*. (Public)
-  Single leading _* :  private (Package Level Private)
-  Double leading __* : strong private (Cant Access Directly by Object)
-  Start & End  __*__ : Language defined Special Name

Built in Attrs

__doc__ − Class documentation string or none, if undefined.
__name__ − Class name.
__module__ − Module name in which the class is defined. This attribute is "__main__" in interactive mode.
__dict__ − Dictionary containing the class's namespace.
__bases__ − A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.

Attribute Methods
- The getattr(obj, name[, default]) − to access the attribute of object.
- The hasattr(obj,name) − to check if an attribute exists or not.
- The setattr(obj,name,value) − to set an attribute. If attribute does not exist, then it would be created.
- The delattr(obj, name) − to delete an attribute.

Garbage Collection:
- Object with 0 reference will get deleted automatically.
- __del__ method will invoke when garbade collecting
- del obj : deleted object manually
- When an object's reference count reaches zero, Python collects it automatically.
"""
from math import pi


class Person:
    """Optional class documentation string"""
    pass  # empty body


class Circle:
    """Using this instead of self"""

    def __init__(this, radi=1):
        this.radi = radi  # this instead of self

    def area(self):
        return pi * self.radi ** 2


circle = Circle(4)
print("area is: ", circle.area())


class Rectangle:
    """Member function with modifying member attrs, class_suite work as static"""
    defaultLength = 10

    def __init__(self, length=defaultLength, width=defaultLength):
        print("Constructor")
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

    def __del__(self):
        print("Destructor: Garbage Collected")


print("\nBuilt-In Class Attributes")
print("class suite: ", Rectangle.defaultLength)
print("Class Name: ", Rectangle.__name__)
print("Document: ", Rectangle.__doc__)
print("Module: ", Rectangle.__module__)
print("Bases: ", Rectangle.__bases__)
print("Dict: ", Rectangle.__dict__)

square = Rectangle(4, 4)

# Read Attr
print("Length is: ", square.length)
print("Length is: ", getattr(square, 'length'))

# Checking Attr exist
print("Has Height?: ", hasattr(square, 'height'))
# print("Has Height?: ", square.height) Attribute Error

# Modify Attr
square.length = 5
print("Modified length is: ", square.length)

setattr(square, "length", 10)
print("Modified area is: ", square.area())

# Delete Attr
del square.length
delattr(square, 'width')

# Clear Object
del square
