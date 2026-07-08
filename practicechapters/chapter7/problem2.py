# WAP to greet all the person names stored in the list and which starts with S

l = ["Harry", "Soham", "Sachin", "Rahul"]

for name in l:
    if(name.startswith("S")): # to take the name starts with S , its simply we write it
        print(f"Hello {name}")
