'''
1 -> for rock
2 -> for paper
3 -> for scissor
'''
import random

# function to choose random number
def computer_choose(num):
    return random.choice(num)


# user input
print("""Enter these values for your choice
         r -> rock
         p -> paper
         s -> scissor""")
youInp = input("enter your choice: ")
youDict = {"r": 1, "p": 2, "s":3}
youStr = youDict[youInp]

# Function call that computer choose between 1,2,3
num = [1,2,3]
computer = int(computer_choose(num))

computerDict = {1:"rock", 2:"paper",3:"scissor"}

computerStr = computerDict[computer]

print(f"Computer choose {computerStr}")

# if-else ladder
if(computer == 2 and youStr == 1 ):
    print("Computer Won!")
elif(computer == 2 and youStr == 3):
    print("You Won!")
elif(computer == 2 and youStr == 2):
    print("Draw")
elif(computer == 1 and youStr == 2 ):
    print("You Won!")
elif(computer == 1 and youStr == 3):
    print("Computer Won!")
elif(computer == 1 and youStr == 1):
    print("Draw")
elif(computer == 3 and youStr == 1 ):
    print("You Won!")
elif(computer == 3 and youStr == 2):
    print("Computer Won!")
elif(computer == 3 and youStr == 3):
    print("Draw")
else:
    print("Invalid Input!!")