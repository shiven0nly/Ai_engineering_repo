# In this chapter we learn about functions and its use cases
"""
A function is a group of statement performing a specific task.

When a program gets bigger in size and its complexity grows. it gets difficult for a program to keep track on which piece of code is doing what!

a function can be reused by the programmer in a given program any number of times


# SYNTAX:-

def function():
    print("Heloo")
    
# function call:
function()  -> write function name here only

# if u want to pass arguments in function like specific values or variables u can

"""
# Function definition
def hello():
    print("This is a function")

hello() # Function call

def avg(a, b, c):
    avg_num = ( int(a)+int(b)+int(c) ) / 3
    return avg_num

a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))

print(f"Avg of numbers {a, b, c} is: {avg(a,b,c)}")

# Write a factorial using function

def factorial(n):
    fact = 1
    for i in range (1, n+1):
        fact = fact*i
    return fact

n = int(input("Enter the num to get its factorial: "))
print(f"factorial of {n} is: ", factorial(n))

# Writing factorial func as recursion

def rec_factorial(n):
    if (n == 1 or n == 0):
        return 1
    return n * rec_factorial(n - 1)
print(f"factorial of {n} is: ", rec_factorial(n))