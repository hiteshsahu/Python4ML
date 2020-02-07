### Learning Python hard way

 [Comment](./begin/HelloWorld.py) :

        # This is an example of single line comment
        """
        This is a example of multi line comment
        """

 ### [Identifiers](./begin/Identifiers.py) :

-  Contain only (A-z, 0-9, and _ )
-  Start with a lowercase letter or _.
-  Single leading _* :  private
-  Double leading __* :  strong private
-  Start & End  \_\_*\_\_ : Language defined Special Name
-  CASE SENSITIVE
-  Class names start with an uppercase letter.

### [DataTypes](./datatype/):

        - Boolean :	bool
        - Numeric :	int, float, complex
        - Text    :	str
        - List    :	list, tuple, range
        - Set     :	set, frozenset
        - Map     :	dict
        - Binary  :	bytes, bytearray, memoryview

There are six sequence types:

         - strings,
         - Unicode strings (deprecated)
         - lists            :  ordered , mutable. Allows duplicate members.
         - tuples,          :  ordered , immutable. Allows duplicate members.
         - buffers, and
         - xrange objects.

 [Boolean Data Type(bool)](./datatype/Boolean.py) :
 
    - Only be True or False
    - "None" is false
    - All numbers are True, except 0.
    - All strings are True, except Empty strings. ie  ""
    - All Collections(list, tuple, set, and dictionary) are True, except Empty ones.ie. (), [], {},
    - Objects from a class with a __len__ function that returns 0 is always false
    
    

[Numeric Data Type:](./datatype/NumericType.py) 

    - int     :  -N, 0 , +N,  Hexa, Octa Decimal
    - float   :  -N.N, 0, +N.N or with e
    - complex :  N+iN

Casting:

- Type int(x) to convert x to a int integer.
- Type long(x) to convert x to a long integer.
- Type float(x) to convert x to a floating-point number.
- Type complex(x) to convert x to a complex number with real part x and imaginary part zero.
- Type complex(x, y) to convert x and y to a complex number with real part x and imaginary part y. x and y are numeric expressions
    
 
[String Type(str):](./datatype/StringType.py) 
    
    - Single Line:  "" =''
    - Multi  Line:  """ """ = ''' '''
    - No character literals         
    
    
[List Data Type(list):](./datatype/ListType.py) 

    - Just Like Array following indexing
    - **Unlike Arrays, list can hold HETEROGENEOUS DATA TYPE
    -  Repetition allowed
    -  Multi Dimensional
    
    
[Tuple Data Type(tuple):](./datatype/SetType.py) 

     - Just Like List but IMMUTABLE
     - No removal and Update Possible
    
    
[Set Data Type(set):](./datatype/SetType.py) :

    -  UN INDEXED
    -  Can hold HETEROGENEOUS DATA TYPE
    -  Repetition NOT allowed
    -  SINGLE Dimensional
    
[Dictionary Data Type(dict):](./datatype/DictionaryType.py) :
    
    - Just Like js Objects
    - INDEXED
    - UNORDERED
    - MUTABLE
    - Multi Dimensional
    - KEY is UNIQUE

 ------------------------   
 
### [Logic flow](./logic/):


[Operators:](./logic/Operators.py) 

    
    -Arithmetic : +, -, *, /, %(modulus), //(floor division), **(exponential)
    -Relational: ==,!=, >, <, <=, >=,
    -Assignment : =, +=, -=, *=, /=, %=,  //=, **=
    -Logical : and, or Not
    -Bitwise : &(and),|(or), ^(xor), ~(not), >>(shift right), <<(shift left)
    -Membership : in, not in
    -Identity : is, not is

[Control flow:](./logic/Decision&Loop.py) 


// remove decimal place in positive and round to int for negative

elif = else if

Decision tree In Python

- if: elif:  else:
- while :    else:
- for x in : else:

Breaking & Passing
- pass : add to empty if condition
- break: breaks loop
- continue: skip loop

Range:
- range(n) : return sequence of 0 to n-1
- range(n,m): sequence of  n+1,n+2 .. <m
- range(n,m,l): sequence of n, n+l,n+2l ...<m

#### [Exceptions:](./logic/Decision&Loop.py) 

try-> catch->else-> finally
    
        try:
            result = x/y
        except ZeroDivisionError as error:
            print("Variable Y is zero: ", format(error))
        except (RuntimeError, TypeError, NameError):
            print("Multiple Error Cached ")
        except:
            print("Generic Error Cached", sys.exc_info()[0])
        else:
            print("Nothing went wrong", result)
        finally:
            print("Finally Called\n")
        
        
       
 ------------------------   
 
### [OOPS](./oops/):

#### [Scope:](./oops/scope.py) 

Python has 2 Types of SCOPE : Global & Local
##### Global Scope:
- Variable created in the main body or with keyword "global"
- Available to all scope, global and local.

##### Local Scope:
- Variable created inside a function,
- Available only inside that function.


[Python Functions:](./oops/functions.py) 

    - Must return a value or simply return to exit function
    - Function Suite have local scope
    - Argument are pass by Reference: Actually modify the input values
    - Argument can have Default value use of =
    - Argument order is important until you pass values like (ArgName = Argvalue ,...)
    - Variable Length argument be can passed using *vartuple


   
***Lamda Function:***
 Anonymous function take any number of Arguments and return 1 value

    addNumber = lambda num1, num2: num1+num2
    print("Lamda Sum: ", addNumber(20, 30))
    
---------

#### [Defining Class and Objects:](./oops/classes.py) 


- Class Body must not be empty but can be ignore with the help of Pass
- self can be renamed to anything
- class_suite work as static, shared across all instances
-  class_suite can be accessed using ClassNAme.variable

##### Attr

    -  Start with a lowercase letter or _*. (Public)
    -  Single leading _* :  private (Package Level Private)
    -  Double leading __* : strong private (Cant Access Directly by Object)
    -  Start & End  __*__ : Language defined Special Name

##### Built in Attrs

    __doc__ − Class documentation string or none, if undefined.
    __name__ − Class name.
    __module__ − Module name in which the class is defined. This attribute is "__main__" in interactive mode.
    __dict__ − Dictionary containing the class's namespace.
    __bases__ − A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.

##### Attribute Methods

    - The getattr(obj, name[, default]) − to access the attribute of object.
    - The hasattr(obj,name) − to check if an attribute exists or not.
    - The setattr(obj,name,value) − to set an attribute. If attribute does not exist, then it would be created.
    - The delattr(obj, name) − to delete an attribute.

##### Garbage Collection:
- Object with 0 reference will get deleted automatically.
- __del__ method will invoke when garbade collecting
- del obj : deleted object manually
- When an object's reference count reaches zero, Python collects it automatically.
    
    
 #### [Inheritance:](./oops/inheritance.py) 
 

  -class C(A, B):   # subclass of A and B

 Checking
 - issubclass(sub, sup): check if sub is a subclass of the superclass sup.
 - isinstance(obj, Class): check if obj is an instance of Class or instance of a subclass of Class
