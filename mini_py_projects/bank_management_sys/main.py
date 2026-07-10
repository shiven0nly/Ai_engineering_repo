from datetime import datetime


# class BankAccount 
class BankAccount:
    # storing user information
    def __init__(self):
        self.account_number=1234567890
        self.password="admin123"
        self.pin=1234
        self.balance=1000
        self.history=[]
    
    # login
    def login(self):
        
        try:
            entered_acc = int(input("Enter account number: "))
        except ValueError:
            print("Account number must contain digits only")
        
        entered_pass = input("Enter your password: ")
        if entered_acc == self.account_number and entered_pass == self.password:
            print("=============")
            print("Login Successful")
            print("=============")
            current_time = datetime.now()
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
            print(f"Login: {formatted_time}")
            return True
        
        if entered_acc != self.account_number:
            print("Account number is Invalid!!")
        
        if entered_pass != self.password:
            print("Invalid password.")
            user_choice = input("Forget password? Enter YES or NO: ").strip().lower()
            if user_choice == "yes":
                self.forgetPassword()
                return True
            else:
                print("Ok, try again!")
                return False
        else:
            print("Invalid Input!!")
            return False
    
    # Check Balance
    def check_balance(self):
        print(f"Current balance:{self.balance}")
        print("Transaction History")
        
        for transaction in self.history:
            print(transaction)
        
        
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
            current_time = datetime.now()
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
            self.history.append(f"Deposited: +{depositAmt} : {formatted_time}")
            
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
                current_time = datetime.now()
                formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
                self.history.append(f"Withdraw: -{withdrawAmt} : {formatted_time}")
                
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
                4 -> update password
                5 -> update pin
                6 -> Exit""")
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
                self.updatePassword()
                
            elif(userInp == 5):
                self.updatePin()
            
            elif(userInp == 6):
                print("Thank you for using!!")
                break
            else:
                print("Invalid input!!")
            
    # update Password
    def updatePassword(self):
        curr_pass = input("Enter your current password: ")
        if(curr_pass == self.password):
            new_pass = input("Enter your new password: ")
            cnf_pass = input("Confirm your password: ")
            if(new_pass == cnf_pass):
                print("Are you sure to change your password: ")
                user_choice = input("Enter 'YES' or 'NO': ").lower()
                if(user_choice == "yes"):
                    self.password = new_pass
                    print("Password changed successfully!")
                    return True
                else:
                    print("Invalid input!!")
                    return False
            else:
                print("Passwords donot match")
                return False
        else:
            print("Invalid password!")
            return False
    
    # update pin
    def updatePin(self):
        try:
            curr_pin = int(input("Enter your current pin: "))
        except ValueError:
            print("PIN only contains digits")
            return False
        if(curr_pin == self.pin):
            try:
                new_pin = int(input("Enter your new pin: "))
            except ValueError:
                print("PIN only contains digits") 
                return False
            try:
                cnf_pin = int(input("Confirm your pin: "))
            except:
                print("PIN only contains digits.")
                return False
            if(new_pin == cnf_pin):
                print("Are you sure to change your pin: ")
                user_choice = input("Enter 'YES' or 'NO': ").lower()
                if(user_choice == "yes"):
                    self.pin = new_pin
                    print("PIN changed successfully!")
                    return True
                else:
                    print("Invalid input!!")
                    return False
            else:
                print("PIN Dont match")
                return False
        else:
            print("Invalid PIN!")
            return
        
    # forget password function
    def forgetPassword(self):
        new_pass = input("Enter your new password: ")
        cnf_pass = input("Confirm your password: ")
        if(new_pass == cnf_pass):
            user_choice = input("Are you sure to update your password as new password is no longer valid after this. Input YES or NO: ").lower()
            if(user_choice=="yes"):
                self.password = new_pass
                print("Your password updated successfully")
                return True
            else:
                print("New password not applied")
                return False
            
# Customer:

customer = BankAccount()

if customer.login():
    customer.menu()
else:
    print("Login failed")