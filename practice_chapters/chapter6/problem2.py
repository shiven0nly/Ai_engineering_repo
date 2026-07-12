# WAP to check three subjects marks, each subject has marks above 33% , and aggregated marks above 40%


marks1 = int(input("Enter marks1: "))
marks2 = int(input("Enter marks2: "))
marks3 = int(input("Enter marks3: "))

# Check for total percentage
total_percentage = (100*(marks1 + marks2 + marks3)) / 300

if((marks1 and marks2 and marks3)>=33):
    if(total_percentage >= 40):
        print("You are passed")
    else:
        print("You failed")
else:
    print("You failed")
