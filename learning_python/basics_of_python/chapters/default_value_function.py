# In function we can pass the default values.. how they work is, they are passed in arguement like: end="Thanks" , and we use end='Thanks' in the arguments, so if no end argument is passed in the function then it will take the value end='thanks' , but , if argument is passed in function then end='passed argument'

def goodDay(name, ending="Thank You"):
    print(f"Good Day, {name}")
    print(ending)


goodDay("SHiven", "thanks")
# here it prints:-
# Good Day, Shiven
# thanks // it takes the passed value of ending 'thanks'
goodDay("Shub")
# here it prints:-
# Good Day, Shub
# Thank You // it takes the default value of ending 'Thank You'