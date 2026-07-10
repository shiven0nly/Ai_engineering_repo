from datetime import datetime


# class BankAccount 
class BankAccount:
    # storing user information
    def __init__(self,name, account_number, password, pin, balance):
        self.name = name,
        self.account_number = account_number
        self.password = password
        self.pin = pin
        self.balance = balance
        self.history=[]
    
    # login
    def login(self):
        max_attempts = 3
        for attempt in range(1, max_attempts + 1):
            try:
                entered_acc = int(input("Enter account number: "))
            except ValueError:
                print("Account number must contain digits only")
                if attempt == max_attempts:
                    print("Maximum login attempts reached. Exiting.")
                    exit()
                print(f"Attempt left: {max_attempts - attempt}")
                continue

            entered_pass = input("Enter your password: ")
            if entered_acc == self.account_number and entered_pass == self.password:
                print("=============")
                print("Login Successful")
                print("=============")
                current_time = datetime.now()
                formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
                print(f"Login: {formatted_time}")
                print("===========")
                print(f"Welcome,{self.name}")
                print("===========")
                return True

            if entered_acc != self.account_number:
                print("Account number is Invalid!!")
            elif entered_pass != self.password:
                print("Invalid password.")
                user_choice = input("Forget password? Enter YES or NO: ").strip().lower()
                if user_choice == "yes":
                    self.forgetPassword()
                    return True
                else:
                    print("Ok, try again!")
            else:
                print("Invalid Input!!")

            if attempt == max_attempts:
                print("Maximum login attempts reached. Exiting.")
                exit()
            print(f"Attempt left: {max_attempts - attempt}")
        return False
    
    # Check Balance
    def check_balance(self):
        
        try:
            check_pin =int(input("Enter your PIN: "))
        except ValueError:
            print("PIN only contains digits")
        if(check_pin != self.pin):
            print("Invalide PIN entered")
            return False
        if(check_pin == self.pin):
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
                0 -> Account Information
                1 -> Check Balance
                2 -> Deposit Amount
                3 -> Withdraw Amount
                4 -> Transfer Money
                5 -> update password
                6 -> update pin
                7 -> Logout
                8 -> Exit""")
            print("====================")
            try:
                userInp=int(input("Enter your choice: "))
            except ValueError:
                 print("Please enter digits only.")
                 continue
            print("=====================")
            
            if(userInp == 0):
                self.accountInfo()
            
            elif(userInp == 1):
                self.check_balance()
                
            elif(userInp == 2):
                self.deposit()
                
            elif(userInp == 3):
                self.withdraw()
            
            elif(userInp == 4):
                self.transferMoney()
                
            elif(userInp == 5):
                self.updatePassword()
                
            elif(userInp == 6):
                self.updatePin()
            
            elif(userInp == 7):
                print("Thank you for using!!")
                return login_func()
            elif(userInp == 8):
                print("Thank you for using!!")
                exit()
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
            return False
        
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
    
    # Transfer Money
    def transferMoney(self):
        print(f"Account no. from money is transferred from: {self.account_number}")
        try:
            target_account_number = int(input("Enter recipient account number: "))
        except ValueError:
            print("Account number only contains digits.")
            return False

        target_account = accounts.get(target_account_number)
        if target_account is None:
            print("Recipient account not found.")
            return False

        try:
            amount = int(input("Enter the amount to transfer: "))
        except ValueError:
            print("Put amount in digits only.")
            return False

        if amount <= 0:
            print("Enter a valid amount greater than zero.")
            return False

        if amount > self.balance:
            print("Insufficient funds.")
            return False

        try:
            user_pin = int(input("Enter your pin: "))
        except ValueError:
            print("PIN only contains digits.")
            return False

        if user_pin != self.pin:
            print("Invalid PIN.")
            return False

        user_choice = input("Are you sure you want to transfer (Enter YES or NO): ").strip().lower()
        if user_choice != "yes":
            print("Transaction Denied!!")
            return False

        self.balance -= amount
        target_account.balance += amount
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        self.history.append(f"Transferred: -{amount} to {target_account_number} : {formatted_time}")
        target_account.history.append(f"Received: +{amount} from {self.account_number} : {formatted_time}")

        print("Money Transferred successfully!!")
        print(f"Your current balance: {self.balance}")
        return True


    # Account Information
    def accountInfo(self):
        print("\n===Your Account Information===")
        print(f"""
        Your name: {self.name},
        Your Account number: {self.account_number},
        Your Balance: {self.balance}
        """)
        print("\n============\n")
# Customer:

customer1 = BankAccount(
    name="Bhalu",
    account_number=1111,
    password="1111",
    pin=1111,
    balance=1000,
)
    
customer2 = BankAccount(
    name="Aalu",
    account_number=2222,
    password="2222",
    pin=2222,
    balance=1000
)

customer3 = BankAccount(
    name="Kalu",
    account_number=3333,
    password="3333",
    pin=3333,
    balance=1000
)
accounts = {
    1111: customer1,
    2222: customer2,
    3333: customer3
}

print("====== BANK APP ========\n")

def login_func():
    user_choice=int(input("Enter your account number: "))
    if user_choice in accounts:
        curr_user=accounts[user_choice]
    
        if curr_user:
            if curr_user.login():
                curr_user.menu()
            else:
                print("Failed Login!!")
        else:
            print("Failed Login!!")
    else:
        print("Account not found!!")    
        
login_func()