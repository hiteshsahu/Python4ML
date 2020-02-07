"""
Python Data Types:
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

"""

# type() : get data type of variable
x = 5
print("Type is", type(x))

# isinstance(var, type) : checks if instance of
print("is Integer? ", isinstance(x, int))


class DataType(object):

        def __init__(self):
              print("Init")





