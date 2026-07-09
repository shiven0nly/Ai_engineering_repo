class Employee:
    lang="python"
    
    def getLang():
        print(lang)

shiven = Employee()
shiven.getLang() # it will throw error as self is not passed her
# as this shiven.getLang() converts into
# Employee.getLang(shiven)
# but our getLang() doesnt receive argument but we are passing so it will not run properly

# to remove this error, we use the word 'self' in argument passing in the function, even though we dont use the function itself but we have to pass

class EM:
    lang="python"
    
    def getLangEM(self):
        print(self.lang)

shiv = EM()
shiv.getLangEM() # it will return the language python
