class Employee:
    company="ITC"
    def show(self):
        print(f"The name is {self.name}")
    
class Programmer:
        company="ITC Infotech"
        def show(self):
            print(f"The name is {self.name}")
        def showlang(self):
            print(f"the name is {self.name} and he is good with{self.lang}")
            
a = Employee()
b = Programmer()

print(a.company,b.company)
# it print ITC, ITC Infotech

# to create the same type of method/function in the other classes also, we use inheritance and we class2(class1) : means , class2 inherite , means it will take the things that are mentioned in class1

class Employee2:
    company="ITC"
    def show(self):
        print(f"The name is {self.name}")
    
class Programmer2(Employee2):
        company="ITC Infotech"
        def showlang(self):
            print(f"the name is {self.name} and he is good with{self.lang}")
            
c = Employee2()
d = Programmer2()
print(c.company,d.company)
# this will also print ITC ITC Infotech as company named is changed in the Programmer class

# we can also import multiple classes
class Employee3:
    company="ITC"
    def show(self):
        print(f"The name is {self.name}")
        
class coder:
    def showlang(self):
            print(f"the name is {self.name} and he is good with{self.lang}")
    
class Programmer3(Employee3,coder):
        company="ITC Infotech"

s = Employee3()
f = Programmer3()
