# take four students name and take their marks and create a dictionary

dict = {} 
# we use the 'update' function , to update the key-value numbers

name = input("Enter name: ")
marks = input("Enter marks: ")

dict.update({name:marks})
name = input("Enter name: ")
marks = input("Enter marks: ")

dict.update({name:marks})
name = input("Enter name: ")
marks = input("Enter marks: ")

dict.update({name:marks})

print(dict)