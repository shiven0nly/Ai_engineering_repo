# write a program to print multiplication table of a given number using for loop:

n = int(input("Enter the number to find the multiplication table: "))
for i in range(1,11):
    print(f"{n} x {i}= {n*i}")

# Write a program to greet all the person names stored in a list and which starts with S

list = ['Harry','Soham','Sachin','Rahul']
for i in list:
    if i.startswith("S"):
        print("Hello",i)

# find the program to find whether a given number is prime or not:
n = int(input("Enter the num to check prime or not: "))
isPrime = False
if(n <= 0):
    print("prime not define")
if(n == 1):
    print("Prime number")

for i in range(2, n):
    if(n % i != 0):
        isPrime = True
        break

if(isPrime):
    print("Prime number")
else:
    print("Not a prime number")    
    
# Write a program to find the sum of first n natural numbers:
n = int(input("Enter the value of n: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print(total)

# find factorial of n
fact = 1
for i in range(n+1,1,-1):
    fact = fact * i
print(f"factorial of n is : {fact}")

