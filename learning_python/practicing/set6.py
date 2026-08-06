# write a function to find the greatest of three numbers

def greatest(a,b,c):
    return max(a,b,c)

# write a program to convert celsius to fahrenheit:
def c_to_f(c):
    return (c*(9/5)+32)

# prevent python to return the new line after print
def no_new():
    return print(end="")

# recursive function calculate the sum of first n natural numbers:
def sum(a):
    if(a == 1):
        return 1
    else:
        return a+sum(a-1)

print(sum(10))

# fact using recrusion
def fact(a):
    if(a == 1 or a == 0):
        return 1
    else:
        return a*fact(a-1)
print(fact(5))