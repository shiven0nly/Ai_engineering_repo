# write a store seven fruits in list:
fruits_list=['apple','banana','guava','dragon fruit','kiwi','promogrenate','cocunut']

# write a program to accept marks of 6 students and display them in sorted manner

marks = []

for i in range(6):
    a = int(input(f"Enter marks of student {i}: "))
    marks.append(a)

marks.sort()
print(marks)

# sum a list of numbers
print(sum(marks))

# count the number of zeroes in the following tuple
a = (7,0,8,0,0,9)
no_of_zeroes=a.count(0)
print(no_of_zeroes)