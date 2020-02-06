"""
List Data Type(list):
- Just Like Array following indexing
- **Unlike Arrays, list can hold HETEROGENEOUS DATA TYPE
-  Repetition allowed
-  Multi Dimensional
"""

# Creating a Multi-Dimensional List

print(" \n-------CREATE---------- ")
List = [['Hitesh', 'kumar', 'Sahu'], [29]]
thislist = ["0", "1", "2", "3", "4", "5", "6", "7"]
fruitList = list(("apple", "banana", "cherry"))

print(List)


print(" \n-------READ---------- ")
print("List[1]: ", List[1])
print("List[0][0]: ", List[0][0])
print("List[0][-2]: ", List[0][-2]) # negative index start from -1

for x in thislist:
    print("Element", x)

print(thislist)
print("LENGTH", len(thislist))
print("MAX", max(thislist))
print("MIN", min(thislist))


print("thislist[:4]: ", thislist[:4])
print("thislist[2:]: ", thislist[2:])


print(" \n-------UPDATE---------- ")

thislist[1] = "9"
print(thislist)

print("\nTraversing Elements")
if "9" in thislist:
    print("Yes, '9' is in the list")

thislist.reverse()
print("Reverse", thislist)

thislist.sort()
print("Sorted", thislist)

thislist.append("10")
print("Append 10:", thislist)

thislist.insert(7, "8")
print("Insert 8:", thislist)

thislist.insert(1, "1")
print("Insert 1:", thislist)

print(" \n-------DELETE---------- ")

thislist.remove("10")
print("remove 10:", thislist)

thislist.pop(9)
print("pop 9:", thislist)

del thislist[8]
print("del 8:", thislist)

thislist.clear()
print("clear:", thislist)