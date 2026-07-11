import json
import os
from datetime import datetime

script_dir = os.path.dirname(os.path.abspath(__file__))
bank_data_path = os.path.join(script_dir, "bank_data.json")

# load accounts data from json
def load_accounts():
    if not os.path.exists(bank_data_path):
        return {}
    with open(bank_data_path, "r") as file:
        return json.load(file)

# write new data to accounts
def save_accounts(account_store):
    with open(bank_data_path, "w") as file:
        json.dump(account_store, file, indent=4)


accounts = load_accounts()

# BankSystem: Handles user login and updation like: update password, update pin and forget password methods
class BankSystem:
    
    # Initing account details
    def __init__(self, name, account_number, password, pin, balance, history=None, account_store=None):
        self.name = name
        self.account_number = str(account_number)
        self.password = password
        self.pin = int(pin)
        self.balance = int(balance)
        self.history = history or []
        self.account_store = account_store if account_store is not None else accounts

    # storing account updation as dictionary
    def persist(self):
        self.account_store[self.account_number] = {
            "name": self.name,
            "password": self.password,
            "pin": self.pin,
            "balance": self.balance,
            "history": self.history,
        }
        save_accounts(self.account_store)

    # Login Method
    def login(self):
        max_attempts = 3
        for attempt in range(1, max_attempts + 1):
            entered_acc = input("Enter account number: ").strip()
            if not entered_acc.isdigit():
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
                    self.forget_password()
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

    # Update password Method
    def update_password(self):
        curr_pass = input("Enter your current password: ")
        if curr_pass == self.password:
            new_pass = input("Enter your new password: ")
            cnf_pass = input("Confirm your password: ")
            if new_pass == cnf_pass:
                print("Are you sure to change your password: ")
                user_choice = input("Enter 'YES' or 'NO': ").lower()
                if user_choice == "yes":
                    self.password = new_pass
                    self.persist()
                    print("Password changed successfully!")
                    return True
                print("Invalid input!!")
                return False
            print("Passwords donot match")
            return False
        print("Invalid password!")
        return False

    # Update PIN Method
    def update_pin(self):
        try:
            curr_pin = int(input("Enter your current pin: "))
        except ValueError:
            print("PIN only contains digits")
            return False
        if curr_pin == self.pin:
            try:
                new_pin = int(input("Enter your new pin: "))
            except ValueError:
                print("PIN only contains digits")
                return False
            try:
                cnf_pin = int(input("Confirm your pin: "))
            except ValueError:
                print("PIN only contains digits.")
                return False
            if new_pin == cnf_pin:
                print("Are you sure to change your pin: ")
                user_choice = input("Enter 'YES' or 'NO': ").lower()
                if user_choice == "yes":
                    self.pin = new_pin
                    self.persist()
                    print("PIN changed successfully!")
                    return True
                print("Invalid input!!")
                return False
            print("PIN Dont match")
            return False
        print("Invalid PIN!")
        return False

    # Forget Password Method
    def forget_password(self):
        new_pass = input("Enter your new password: ")
        cnf_pass = input("Confirm your password: ")
        if new_pass == cnf_pass:
            user_choice = input("Are you sure to update your password as new password is no longer valid after this. Input YES or NO: ").lower()
            if user_choice == "yes":
                self.password = new_pass
                self.persist()
                print("Your password updated successfully")
                return True
            print("New password not applied")
            return False
        return False

    # Account Info Method
    def account_info(self):
        print("\n===Your Account Information===")
        print(f"""
        Your name: {self.name},
        Your Account number: {self.account_number},
        Your Balance: {self.balance}
        """)
        print("\n============\n")


# BankAccount class: handles transactions like: deposit money, withdraw money and transfer money from one bank account to another.
class BankAccount(BankSystem):
    
    # Check Balance Method
    def check_balance(self):
        try:
            check_pin = int(input("Enter your PIN: "))
        except ValueError:
            print("PIN only contains digits")
            return False
        if check_pin != self.pin:
            print("Invalide PIN entered")
            return False
        print(f"Current balance:{self.balance}")
        print("Transaction History")
        for transaction in self.history:
            print(transaction)
        return True

    # Deposity Money Method
    def deposit(self):
        try:
            deposit_amt = int(input("Enter the deposit amount: "))
        except ValueError:
            print("Enter only digits like:5000")
            return
        if deposit_amt > 0:
            self.balance += deposit_amt
            print("Transaction Succesful!!")
            print(f"Available balance: {self.balance}")
            current_time = datetime.now()
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
            self.history.append(f"Deposited: +{deposit_amt} : {formatted_time}")
            self.persist()
        else:
            print("Enter valid amount!!")

    # Withdraw Money Method
    def withdraw(self):
        try:
            withdraw_amt = int(input("Enter withdraw amount: "))
        except ValueError:
            print("Enter digits only like: 5000")
            return
        if withdraw_amt <= 0:
            print("Invalid Amount")
            return
        if withdraw_amt > self.balance:
            print("Insufficient amount!!")
            return
        try:
            pin = int(input("pin: "))
        except ValueError:
            print("Enter digits only like: 1234")
            return
        if pin == self.pin:
            self.balance -= withdraw_amt
            print("Transaction Successful!!")
            print(f"Available balance: {self.balance}")
            current_time = datetime.now()
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
            self.history.append(f"Withdraw: -{withdraw_amt} : {formatted_time}")
            self.persist()
        else:
            print("Invalid pin")

    # Main Menu Method
    def menu(self):
        while True:
            print("""Welcome, Choose the options:-
                0 -> Account Information
                1 -> Check Balance
                2 -> Deposit Amount
                3 -> Withdraw Amount
                4 -> Transfer Money
                5 -> update password
                6 -> update pin
                7 -> Interest Calculation
                8 -> Logout
                9 -> Exit""")
            print("====================")
            try:
                user_inp = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter digits only.")
                continue
            print("=====================")

            if user_inp == 0:
                self.account_info()
            elif user_inp == 1:
                self.check_balance()
            elif user_inp == 2:
                self.deposit()
            elif user_inp == 3:
                self.withdraw()
            elif user_inp == 4:
                self.transfer_money()
            elif user_inp == 5:
                self.update_password()
            elif user_inp == 6:
                self.update_pin()
            elif user_inp == 7:
                self.interest_calc()
            elif user_inp == 8:
                print("Thank you for using!!")
                return
            elif user_inp == 9:
                print("Thank you for using!!")
                raise SystemExit
            else:
                print("Invalid input!!")

    # Transfer Money Method
    def transfer_money(self):
        print(f"Account no. from money is transferred from: {self.account_number}")
        try:
            target_account_number = input("Enter recipient account number: ").strip()
        except EOFError:
            target_account_number = ""
        if not target_account_number.isdigit():
            print("Account number only contains digits.")
            return False

        target_account_data = self.account_store.get(target_account_number)
        if target_account_data is None:
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
        target_account_data["balance"] = int(target_account_data.get("balance", 0)) + amount
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        self.history.append(f"Transferred: -{amount} to {target_account_number} : {formatted_time}")
        target_account_data.setdefault("history", []).append(
            f"Received: +{amount} from {self.account_number} : {formatted_time}"
        )
        self.persist()
        print("Money Transferred successfully!!")
        print(f"Your current balance: {self.balance}")
        return True
    
    # Interest Calc Method
    def interest_calc(self):
        try:
            amount= int(input("Enter principle amount: "))
        except ValueError:
            print("Amount only contains digits.")
            return False
        interest_annual_rate=5
        print("Interest annual_rate= 5% per annum")
        try:
            time=int(input("Choose the time in months or years (1 -> Months and 2-> Years): "))
        except ValueError:
            print("Choose the options from 1 or 2")
            return False
        if(time == 1):
            print("You choose Months")
            try:
                months=int(input("Enter the no. of months: "))
                time_in_years= months/12
            except ValueError:
                print("Enter the digits only")
                return False
        else:
             print("You choose years")
             try:
                 years=int(input("Enter no.of years: "))
                 time_in_years=years
             except ValueError:
                 print("Years only contains digits.")
                 return False
        interest = (amount*interest_annual_rate*time_in_years) / 100
        print(f"Your total interest amount={interest}")
        total_amount=amount+interest
        print(f"Total amount=",total_amount)
        
        


print("====== BANK APP ========\n")

# Login User Method
def login_func():
    while True:
        user_choice = input("Enter your account number: ").strip()
        print("User Account Found!")
        if user_choice in accounts:
            account_data = accounts[user_choice]
            curr_user = BankAccount(
                name=account_data.get("name", ""),
                account_number=user_choice,
                password=account_data.get("password", ""),
                pin=account_data.get("pin", 0),
                balance=account_data.get("balance", 0),
                history=account_data.get("history", []),
                account_store=accounts,
            )
            if curr_user.login():
                curr_user.menu()
            else:
                print("Failed Login!!")
        else:
            print("Account not found!!")


# Main Function
if __name__ == "__main__":
    login_func()
