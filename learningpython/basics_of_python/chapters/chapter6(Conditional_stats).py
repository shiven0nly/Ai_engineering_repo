# In this chapter we learn about CONDITIONAL STATEMENT
# IF ELSE ELIF

"""
SYNTAX:-
if(condition):
    print("statement1")
elif(condition2):
    print("statement2")
else:
    print("statement3")

Indentation is imp in python
    
"""
age = int(input("Enter your age: "))
# for && we use 'and' in python
# for || we use 'or' in python
# for ! we use 'not' in front

# if(not(age<=18))
    #   print("You are not allowed")

if(age >= 18 ):
    print("You are eligible for driving")
elif(age <= 0):
    print("Invalid age")
else:
    print("You are not eligible for driving")
