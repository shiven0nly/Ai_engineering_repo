class BankAccount:
    # storing user information
    def __init__(self):
        self.account_number=1234567890
        self.password="admin123"
        self.pin=1234
        self.balance=1000
    
    # login
    def login(self):
        
        try:
            entered_acc = int(input("Enter account number: "))
        except ValueError:
            print("Account number must contain digits only")
        entered_pass= input("Enter your password: ")
        
        if (entered_acc == self.account_number and entered_pass == self.password):
            print("=============")
            print("Login Successful")
            print("=============")
            return True
        else:
            print("Inavalid Account number or Password")
            return False
    
    # Check Balance
    def check_balance(self):
        print(f"Current balance:{self.balance}")
        
        
    # Deposit
    def deposit (self):
        try:
            depositAmt = int(input("Enter the deposit amount: "))
        except ValueError:
            print("Enter only digits like:5000")
            return
        if(depositAmt > 0):
            self.balance += depositAmt
            print("Transaction Succesful!!")
            print(f"Available balance: {self.balance}")
            
        else:
            print("Enter valid amount!!")
            
    
    # Withdraw:
    def withdraw(self):
        try:
            withdrawAmt=int(input("Enter withdraw amount: "))
        except ValueError:
            print("Enter digits only like: 5000")
            return 
        if(withdrawAmt <= 0):
            print("Invalid Amount")
            return
            
        if(withdrawAmt > self.balance):
            print("Insufficient amount!!")
            return
            
        elif(withdrawAmt <= self.balance):
            try:
                pin = int(input("pin: "))
            except ValueError:
                print("Enter digits only like: 1234")
                return
            if(pin == self.pin):
                self.balance -= withdrawAmt
                print("Transaction Successful!!")
                print(f"Available balance: {self.balance}")
                
            else:
                print("Invalid pin")
                
        else:
            print("Invalid Input!!")
            
    
    # Menu
    def menu(self):
        while(True):
            print("""Welcome, Choose the options:-
                  1 -> Check Balance
                  2 -> Deposit Amount
                  3 -> Withdraw Amount
                  4 -> Exit""")
            print("====================")
            try:
                userInp=int(input("Enter your choice: "))
            except ValueError:
                 print("Please enter digits 1,2,3 or 4 only.")
                 continue
            print("=====================")
            
            if(userInp == 1):
                self.check_balance()
                
            elif(userInp == 2):
                self.deposit()
                
            elif(userInp == 3):
                self.withdraw()
            
            elif(userInp == 4):
                print("Thank you for using!!")
                break
            else:
                print("Invalid input!!")
            
            
# Customer:

customer = BankAccount()

if customer.login():
    customer.menu()
else:
    print("Login failed")