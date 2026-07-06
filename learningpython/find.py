# Replace the double space in a string with single spaces

# to detect the double spaces we use the function 'find()' , what find does? it returns the index of the value u write in its braces.. 

name = "SHiven is not a good boy"
print(name.find("o")) # now it will return the index of o , but it stops when it finds the first element, for example if it found 'o' at 11th index then it will not search behind that 'o' that at 15th or 16th index also 'o' , it stops at its first find

sentence = "Shiven  Is Mad. He  Become careless"
print(sentence.replace("  ", " ")) # simple like this
# in this replace, the string is not changed globally, instead a new string is created by the function to print with the changes
print(sentence)