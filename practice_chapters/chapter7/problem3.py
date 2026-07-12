# WAP to check prime or not

num = int(input("Enter the num: "))

if num <= 1:
    print(f"{num} is not a prime number")
else:
    isPrime = True
    
    for i in range(2,num):
        if(num % i == 0):
            isPrime = False
            break

    if isPrime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")