# if we want to pass the function without using self, we can use the 'static method'


class Em:
    lang="py"
    
    @staticmethod
    def greet():
        print("Hello")