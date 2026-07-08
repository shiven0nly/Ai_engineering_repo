# In this chapter we learn about loops

for i in range(1,6): # it will print 1,2,3,4,5 not 6
    print(i)

# ==================
# WHILE LOOP

i = 0
while(i<6):
    print(i)
   # i++ its not work here
    i += 1 # or i = i+1
    
print("\n=========================\n")
    
list = ["mongo", "apple", "banana", "guava","pineapple","beetroot","carrot","watermelon","melon","grapes"]

# for i in list:
#     print(i)

i = 0
while i < len(list):
    print(list[i])
    i += 1
    
print("\n====================\n")
    
# ============

# FOR LOOP WITH ELSE
# An optional else can be used with a for loop if the code is to be executed when the loops exhausts.

l = [7,8,6]
for item in l:
    print(item)
else:
    print("done") # this is printed when the loop exists / exhausts!

# we can use classic break and continue statements in the loops also..

