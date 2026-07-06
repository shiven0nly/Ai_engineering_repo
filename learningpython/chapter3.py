"""
name = "Harry" # String
# 1. single quoted string
# 2. DOuble quoted string
# 3. Triple quoted STring

"""

# =========
"""
Strings are immutable , we cant change the strings character

=> We can slice the string using indexing
"""
name = "Shiven"
nameShort = name[2] # print only the character that's position is specified here

slicing = name[0:3] # start from index 0 al the way till 3, like 0th , 1st , 2nd position include , 3rd position wont include

print(nameShort)
print(slicing)
print(len(name)) # to print the length of the string

# FUNCTIONS IN STRINGS =====
# 1. Length of string = len(name)

# 2. string.endswith("anything you want to search")

# 3. string.startswith("__")

# 4. string.capitalize

# 5. 