"""
String Type(str) :
- Single Line:  "" =''
- Multi  Line:  """ """ = ''' '''
- No character literals
"""
# Single Line
name = "Hitesh"

surname = ' Sahu'

testString = "  Hitesh Sahu  "

# MultiLine
lorel = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(lorel, "\n")

print("name is", name)
print("surname is", surname)

print("Name Length ", len(name))        # LENGTH

# READ

print(" \n-------READ---------- ")
print(" H in name: ", 'H' in name)                 # In: char At
print(" H count in name: ", name.count('H'))       # In: char At

print(" H not in name: ", 'H' not in name)          # In: char At
print("Start With H?: ", name.strip()
      .startswith('H'))                             # In: char At
print("End With h?:", name.endswith('h'))           # In: char At


print("name[0]: ", name[0])                           # SLICE: char At
print("name[3:len(name)]:", name[3:len(name)])        # RANGE SLICE:  Sub String [ From Inclusive : To Exclude]

# Update
print(" \n-------UPDATE---------- ")
print("Concate: ", name + surname)       # CONCATENATION: Add
print("Repeate: ", name + surname*2)     # REPETITION
print("Replace ",
      testString.replace("sh", "ch"))    # REPLACE
print("Stripe", testString.strip())      # TRIM : remove white space


print(" \n-------CASE CHANGE---------- ")
print("Lower ", testString.lower())                     # LowerCase
print("Upper ", testString.upper())                     # Upper Case
print("Swap case ", testString.swapcase())               # Swap Case

print("Capitalize ", testString.strip().capitalize())    # Capitalize Case of first word
print("Title ", testString.title())                      # title Case: Capitalize Case of each word

print(" \n-------FORMATTING---------- ")

print("Split ", testString.split(" "))   # Split

#  Formatting
quantity = 3
itemNo = 567
price = 49.95
myOrder = "I want {} pieces of item {} for {} dollars."
print(myOrder.format(quantity, itemNo, price))