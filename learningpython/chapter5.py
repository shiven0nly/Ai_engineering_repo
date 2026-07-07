# In this chapter we read about DICTIONARY & SETS 

"""
Dictionary is a collection of keys-value pairs

1. it is unordered.
2. it is mutable
3. it is indexed
4. cannot contain duplicate keys

# syntax ============
a = {"name": "shiven" 
     "from": "India"
     "marks": [75,74,85]}

# methods ===========

1. a.items() : returns a list of (key, value) tuples
2. a.keys() : returns a list containing dictionary's keys
3. a.updated({"friend"}): updates the dictionary with supplied key-value pairs
4. a.get("name"): returns the value of the specified keys (and value is returned ed: "shiven" is returned here)

# We can store multiple items in the form of array in one key of the dictonary

b = {
    "name" : ["shiv" , "shiva" , "Shiven" , "ashiva" , "shivens"]
    "marks" : [89,75,24,63,12,45,32]
}


"""
b = {
    "name" : ["shiv" , "shiva" , "Shiven" , "ashiva" , "shivens"],
    "marks" : [89,75,24,63,12,45,32]
}
print(b["name"]) # to print the values present in the 'name' key

print(b) # print the complete dictionary

"""
print(marks.get("name"))
print(marks["name"])

they both give the same output

but if we do some change

print(marks.get("name2"))
print(marks["name2"])
# now name2 keypair doesnt exist in the dict
so

print(marks.get("name2")) 
# this line gives: None

print(marks["name2"])
# this line gives keyError
"""

# to create the empty dict
dict = {}
print(type(dict))


# =============
# SET
s = {1,2,3,4} # its set , we use curly braces , [] -> list , () -> tuple , {} -> dict and set

# to create empty set
e = set() # dont use s = {} it create empty dictionary
# we use set, where elements dont repeat
set = {1,4,3,2,2,2,2}
print(set)
set.add(56)
print(set) # it append the element

# =================
# Operations on set

"""
1. len(set) : returns the length of set
2. set.remove(element) : updates the set 'set' and removes 'element' from set
3. set.pop()
4. set.clear() : empties the set 'set'
5. set.union(set2) : returns a new set with all items from both sets.
6. set.intersection(set2) : returns a new set which contains only item in both sets.
"""
