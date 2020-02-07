"""
Boolean Data Type(bool):
- Only be True or False
- None is false
- All numbers are True, except 0.
- All strings are True, except Empty strings. ie  ""
- All Collections(list, tuple, set, and dictionary) are True, except Empty ones.ie. (), [], {},
- Objects from a class with a __len__ function that returns 0 is always false
"""

# Empty, 0 or null value are False Values
print(bool(None))   # Null
print(bool(False))  # false
print(bool(0))      # 0 Number
print(bool(""))     # empty String
print(bool(()))     # empty Tuple
print(bool([]))     # empty List
print(bool({}))     # empty Dictionary

# Class with__len__ returning 0 is False


class TestClass():
    def __len__(self):
        return 0


testObj = TestClass()

# Can use to assert if its empty, null or return  0 in __len__
if bool(testObj):
    print("Object is True ", bool(testObj),"\n")

else:
    print("Object is False ", bool(testObj), "\n")

print(bool(True))                   # True
print(bool(2.75))                   # Non 0 Number
print(bool("Hitesh"))               # Non empty String
print(bool(('Hitesh', 'Sahu')))     # Non empty Tuple
print(bool(['Hitesh', 'Sahu']))     # Non empty List
print(bool({'firstName':'Hitesh',
            'lastName': 'Sahu'}))    # Nonempty Dictionary

