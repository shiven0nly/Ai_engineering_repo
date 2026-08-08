 # Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers.

total = 0
count = 0

while True:
    num = int(input("Enter the num: "))
    if num == 0:
        break
    total += num
    count += 1

if count:
    print(f"avg of your tries: {total/count} and total counts={count}")
else:
    print("No numbers entered.")
    
# Extract username from a given email.
#Eg if the email is nitish24singh@gmail.com then the username should be nitish24singh

user_email = input("enter your email: ").strip()
if '@' in user_email:
    username = user_email.split('@')[0]
else:
    username = user_email

print(username)
print(f"your username become: {username}")

# Write a python program to remove all the duplicates from a list 
list = [1,3,4,5,1,5,6,3]
new_list = set(list)
print(new_list)

# write a program to print the star pattern:
"""
*
**
***
****
*****
"""
star = "*"
for i in range(1,6):
    print(f"{star*i}")
print("\n\n")
# prin the pattern:
"""
*    # ek star 
**   # do star
***  # teen star
**   # do star
*    # ek star
"""
for i in range(1,4):
    print(f"{star*i}")
for i in range(3,0,-1):
    print(f"{star*i}")
print("\n\n")

# print this pattern:
"""
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * *   

"""
space = " "
for i in range(1,6):
    stars = " ".join([star] * (2*i - 1))
    print(f"{space*(5-i)}{stars}")
    
# print this pattern:
"""

1 
1 2 1 
1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 """

for i in range(1,6):
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()
print("\n\n")

# print the following program:
"""
1
2 3
4 5 6
7 8 9 10
"""

num = 1
for i in range(1,5):
    for j in range(1,i+1):
        print(num,end=" ")
        num += 1
    print()