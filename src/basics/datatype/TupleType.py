"""
Tuple Data Type(tuple):
 - Just Like List but IMMUTABLE
 - No removal and Update Possible
"""

# Creating a Multi-Dimensional List

print(" \n-------CREATE---------- ")
multiDTuple = (('Hitesh', 'kumar', 'Sahu'), (29))
myTuple = ("0", "1", "2", "3", "4", "5", "6", "7")
fruitList = tuple(("apple", "banana", "cherry"))

print(multiDTuple)


print(" \n-------READ---------- ")
print("List[1]: ", multiDTuple[1])
print("List[0][0]: ", multiDTuple[0][0])
print("List[0][-2]: ", multiDTuple[0][-2]) # negative index start from -1

for x in myTuple:
    print("Element", x)

print(myTuple)
print("LENGTH", len(myTuple))
print("MAX", max(myTuple))
print("MIN", min(myTuple))


print("myTuple[:4]: ", myTuple[:4])
print("myTuple[2:]: ", myTuple[2:])


if "9" in myTuple:
    print("Yes, '9' is in the list")
else:
    print("No, '9' is not in the list")

print(" \n-------UPDATE---------- ")

# UPDATE IS NOT SUPPORTED

print(" \n-------DELETE---------- ")

# DELETE  IS NOT SUPPORTED

del myTuple
