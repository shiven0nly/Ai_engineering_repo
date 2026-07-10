import random
def computer_choose(min_num, max_num):
    return random.randint(min_num, max_num)


print("====== Number Guessing Game ======")

print("""
Choose the difficulty:
1 -> Easy   (1 - 30)
2 -> Medium (1 - 100)
3 -> Hard   (100 - 999)
""")

userDif = int(input("Enter difficulty level: "))

if userDif == 1:
    min_num, max_num = 1, 30
elif userDif == 2:
    min_num, max_num = 1, 100
elif userDif == 3:
    min_num, max_num = 100, 999
else:
    print("Invalid Input!")
    exit()

computer = computer_choose(min_num, max_num)

count = 0

while True:
    userInp = int(input(f"Enter a number ({min_num}-{max_num}): "))
    count += 1

    if userInp < min_num or userInp > max_num:
        print("Enter a valid number!")
        continue

    if userInp > computer:
        print("Guess Lower!")

    elif userInp < computer:
        print("Guess Higher!")

    else:
        print("🎉You Won!")
        print(f"Correct Number: {computer}")
        print(f"Number of tries: {count}")
        break