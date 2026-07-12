a = input("Enter number 1: ")
b = input("Enter number 2: ")

print("Sum is: ", a+b) # here a and b are coming as strings , so strings concatinate, and if a=1, b=2 , then a+b=12 .. 

# now if we really want to add the numbers as integers , then we have to typecaste

c = int(a)
d = int(b)
print("Sum is: ", c+d)