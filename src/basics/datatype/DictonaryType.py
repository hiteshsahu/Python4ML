"""
Dictionary Data Type(dict):
- Just Like js Objects
- INDEXED
- UNORDERED
- MUTABLE
- Multi Dimensional
- KEY is UNIQUE
"""

# Creating a Multi-Dimensional List


# CREATE
print(" \n-------CREATE---------- ")

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict", dict)

dict2 = dict.copy()
print("dict2", dict2)
print()

# READ

print(" \n-------READ---------- ")
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

print()
print("AllKey: ", dict.keys())
print("Has Key: ", "Blah" in dict)
print("Default: ", dict.get('Blah', "NA"))
print("AllValue: ", dict.values())
print("Pairs: ", dict.items())


print()

# UPDATE
print(" \n-------UPDATE---------- ")
print("dict['Name']: ", dict['Name'])
dict['Name'] = "LION"
print ("dict['Name']: ", dict['Name'])

# Set key with default value
dict.setdefault('Sex', "Male")
print("Set Default ", dict['Sex'])

# update
dict2 = {'Sex': 'female'}
dict.update(dict2)
print( "Update", dict['Sex'])

print()

# DELETE
print(" \n-------DELETE---------- ")
del dict['Name']  # remove entry with key 'Name'
dict.clear()      # remove all entries in dict
del dict          # delete entire dictionary

#  print ("dict['Age']: ", dict['Age'])
## print (")