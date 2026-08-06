# write a program to find the greatest of four numbers entered by the user:

list = []
for i in range(4):
    a = int(input(f"Enter the num{i}: "))
    list.append(a)

print(f"greatest of all: {max(list)}")

# write a program to check student pass or fail?
marks=[]
for i in range(3):
    a = int(input(f"ENter subject {i} marks: "))
    marks.append(a)

if((marks[0] > 33) and (marks[1] > 33) and (marks[2] > 33)):
    if((sum(marks)*100)/300 > 40):
        print("Pass")
    else:
        print("fail")
else:
    print("fail")

# spam filter
spam = ['make a lot of money','buy now','subscribe now','click this']
email="""
Hello 'Rahul', My name is Micheal
From XYZ brand
Do you want to 'make a lot of money' in just few hours than 'click this' link to get redirected.
"""
if any(keyword in email for keyword in spam):
    print("Spam Email")
else:
    print("Normal Email")

# find the program to find whether a given username contains less than 10 characters or not.
username=input("Enter your username: ")

while(username):
    if(len(username) <= 10):
        print("Correct username")
        break
    else:
        username=input("Enter your username: ")

