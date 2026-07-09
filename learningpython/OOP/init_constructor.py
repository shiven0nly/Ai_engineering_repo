# we can also pass instance attribute directly to class using __inti__()


class Em():
    def __init__(self,name,lang,salary):
        self.name=name
        self.lang=lang
        self.salary=salary
        print(f"name is={name},\nsalary is={salary},\nlang is={lang}")


shiven = Em("Shiven","Python",1300000)
# it will print the output without calling it
# as its __init__() function as behavior to run without calling