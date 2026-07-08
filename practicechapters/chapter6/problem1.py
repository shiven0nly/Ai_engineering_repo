# WAP to find the greatest of four numbers entered by user

a = int(input("Enter no.1: "))
b = int(input("Enter no.2: "))
c = int(input("Enter no.3: "))
d = int(input("Enter no.4: "))

if(a > b and a > c and a > d):
    print("a is greatest")
elif(b > a and b > c and b > d):
    print("b is greatest")
elif(c > b and c > a and c > d):
    print("c is greatest")
else:
    print("d is greatest")