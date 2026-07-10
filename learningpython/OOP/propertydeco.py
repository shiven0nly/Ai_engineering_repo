class Employee:
    
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name(self, value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]
    
e = Employee()
e.name='Shiven Sharma'
print(f"{e.fname} , {e.lname} , {e.name}")
# it prints: Shiven, Sharma, Shiven Sharma