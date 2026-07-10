class Employee:
    a=1
    def show(self):
        print(f"The value of a is {self.a}")
        
e = Employee()
e.a=5
e.show()
# it will show 5

class Employee2:
    b=1
    @classmethod
    def show(self):
        print(f"The value of a is {self.a}")
        
c = Employee()
c.b=5
c.show()
# it will show 1