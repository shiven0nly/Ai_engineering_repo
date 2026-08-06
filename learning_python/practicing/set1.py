# add two numbers:
def sum(a,b):
    return a+b
print(sum(4,5))

# find the remainder:
def remainder(divisor,dividend):
    return divisor/dividend
print(remainder(5,2))

# check the type of variable using input
a = input("Enter any value: ")
print(type(a))

# comparison
a = 80
b = 43
if(a>b):
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")
    
# average of two numbers entered by the user
a = int(input("enter 1: "))
b = int(input("enter 2: "))
def avg(a,b):
    return (a+b)/2

print(f"Avg of {a} and {b} is {avg(a,b)}")

# Square of a number
def square(a):
    return a*a
print(f"square of {a} is: {square(a)}")
