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