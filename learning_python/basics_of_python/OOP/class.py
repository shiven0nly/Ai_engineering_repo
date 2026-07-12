class Employee:
    lang="Python" # this is a class attributer
    salaray=1200000
    
shiven = Employee() # shiven is object here

print(shiven.lang, shiven.salary)
# it will print the lang = python and salary= 1200000

shub = Employee()
print(shub.salary)
# it will again print the salary = 1200000

# we can also add the attributes in between

shiven.name="shiven"
# here 'name' is instance attribute and 'salary' and 'lang' are class attributes as they directly belong to the class