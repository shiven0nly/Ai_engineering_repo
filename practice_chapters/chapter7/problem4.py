# WAP to find the fact

num = int(input("ENter ther num: "))

fact = 1
for i in range(1, num+1):
    fact = fact * i

print(f"factorial of {num} is:", fact)