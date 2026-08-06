# write a program to store information of programmers
class Programmers:
    company="Ydv InfoTech Sols"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def getInfo(self):
        print(f"Name: {self.name}, salary: {self.salary}")
    
p1 = Programmers("Shiven","20lpa")
p2 = Programmers("Rahul",'24lpa')

p1.getInfo()
p2.getInfo()

# calculator capable of finding the square, cube and square

class Calculator:
    def __init__(self,op,a):
        self.op=op
        self.a=a
        
    def calc(self):
        if(self.op==2):
            print(f"square of the number is: {self.a**2}")
        elif(self.op==3):
            print(f"cube of the number is: {self.a**3}")
        elif(self.op==1):
            print(f"square root of the number is: {self.a**0.5}")
        else:
            print("Invalid input")

a = Calculator(3,5)
a.calc()

s = ()
print(type(s))
s = []
print(type(s))
s={}
print(type(s))
s = {1,}
print(type(s))