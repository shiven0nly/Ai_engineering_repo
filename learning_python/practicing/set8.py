# print all the armstron numbers in the range of 100 to 1000
# -> what is armstrong number?
# ans: abc = a**3 + b**3 + c**3 = abc
for num in range(100,1001):
    order = len(str(num))
    sum = 0
    temp = num
    
    while temp>0:
        digit = temp % 10 # gives last digit: 153 % 10 = 3
        sum += digit ** order # suming up them with 0+digit, then digit+digit2
        temp //=10 # // means integer division(no decimals) 153//10 = 15
        # now next loop will go like digit % 10 = 15 % 10 = 5
        # then adding it by cubin it
        
    if num == sum:
        print(num)

# current population of town is 10000, so every year its population increased by 10% , end of each of the last 10 years
# 10th year - 10000
# 9th year - 9000
# 8th year - 8100 and so on

curr_pop = 10000
rate = 0.1
for i in range(11,1,-1):
    prev_year_pop = curr_pop-curr_pop*rate
    print(f"year-{i} pop = {prev_year_pop}")
    curr_pop = prev_year_pop

# Write a program to print all the unique combinations of 1,2,3,4
import itertools

numbers = [1, 2, 3, 4]

# Generate all permutations of length 4
perms = itertools.permutations(numbers) # already available function

for p in perms:
    print(p)

# HCF of two numbers
num1=30
num2=24

# so we have to loop them and update the numbers
while num2 != 0:
    num1,num2= num2,num1%num2
    # for first iteration:
    # 30 % 24 = 6
    # num1 = 24 and num2 = 6
    # again 24 % 6 = 4
    # num1 = 6 and num2 = 4
    # till it becomes zero.
print(num1)

# for LCM
x = 30
y = 24
greater = max(x, y)   # start from the larger number
while True:
    if greater % x == 0 and greater % y == 0:
        print(greater)
        break
    greater += 1

# Find the reverse of a number provided by the user(any number of digit):
num = int(input("Enter the number to find tis revers: "))
order = len(str(num))
# 123
rev=0
i = 0
while num > 0:
    digit = num%10 # 3
    rev = rev + digit*(10**(order-i-1)) # rev = 0   + 3 * 10^2 = 300
    i += 1
    num //= 10 # 12
print(rev)
# digit = 12%10 = 2
# rev = 300 + 2*10^1 = 320
# num = 1
# i = 2
# digit = 1 % 10 = 1
# rev = 320 + 1*10^0 = 320 + 1 = 321