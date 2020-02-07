"""
Set Data Type(set):
-  UN INDEXED
-  Can hold HETEROGENEOUS DATA TYPE
-  Repetition NOT allowed
-  SINGLE Dimensional
"""

# Creating a Multi-Dimensional List
from math import pi

print(" \n-------CREATE---------- ")
multiDSet = {'Hitesh', 'kumar', 'Sahu', 29, "Sahu", pi}
mySet = {"0", "1", "2", "3", "4", "5", "6", "7"}
fruitSet = set(["apple", "banana", "cherry"])

print(multiDSet)


print(" \n-------READ---------- ")

print("INDEXING NOT ALLOWED")

print("Traversing Elements")
for x in mySet:
    print("Element", x)

print(mySet)
print("LENGTH", len(mySet))
print("MAX", max(mySet))
print("MIN", min(mySet))


if "9" in mySet:
    print("Yes, '9' is in the list")


print(" \n-------UPDATE---------- ")

mySet.add("10")
print("Add 10:", mySet)

mySet.update(["9", "10", "8"])
print("update([9, 10, 8]):", mySet)

print(" \n-------DELETE---------- ")

mySet.remove("10")
print("remove 10:", mySet)  # THROW ERROR

mySet.discard("10")
print("discard 10:", mySet)  #NOT THROW ERROR

print("POP :", mySet.pop())


mySet.clear()
print("clear:", mySet)

del fruitSet
print("del:", fruitSet)