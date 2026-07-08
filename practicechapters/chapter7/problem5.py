# print the following patternn

"""
        *   2 spaces 1 star 
       ***  1 spaces 3 stars
      ***** 0 spaces 5 stars
      
    for n = 3
    
=> 2i -1 pattern follow ho rha hai ok
=> spaces me ulta pattern follow ho rha hai like n - i pattern
"""
# three rows , columns is 5 with space
n = int(input("enter num: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="") # to print multiple * we multiply with (2*i-1) to print it 2*i-1 times
    print("\n")