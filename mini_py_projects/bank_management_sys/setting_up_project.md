# This is the file to brainstorm about the bank management system project before writing the code

**So, Before starting we structure the project essentials**

### these are the elements that are hardcoded stored
1. account number and password for login
2. atm pin to withdraw money
3. balance


### functions require
1. login()
2. check_balance()
3. deposit()
4. withdraw()
5. show_menu()
6. exit()

#### Step 1: Login
1. user enter the account number and password
2. check password: yes or no
3. if yes: show_menu()
4. if no: Login Failed

* For this we use strings and if-else

#### Step 2: Main Menu
* Show_menu(): show the following things
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit

* we want that after every function execute except: exit, the show_menu() will appear again, means we have to put in a infinte loop

**FLOW**
Login -> Menu -> Deposit -> Money Added -> Menu Again -> Check Balance -> Menu Again -> Exit

#### Step 3: Check Balance
* current Balanc: 250000
* Hardcoded

#### Step 4: Deposit

**FLOW**
Enter Amount -> Amount > 0? -> Yes -> balance +=amount -> success -> return main menu 
* No pin needed

#### Step 5: Withdraw

**FLOW**
Enter Amount -> Enter PIN(hardcoded) -> Pin correct ? -> No -> Transaction Failed -> if Yes -> Enough balance? (corner case) -> No -> Insufficient Balance -> If Enough balance -> yes -> balanc -= amount -> Transaction Successful -> return main menu

#### Step 6: Exit

* Thank You
* Visit again!!

then , **break**

---

We Use **OOPS** for writing clean code:-

```
Bank Account = {
    Account Number
    Password
    PIN
    Balance

# ==============

    def login()
    def deposit()
    def withdraw()
    def check_balance()
    def menu()
}
```

---

## THE TWO SYSTEMS
**Here, I made the bank management system in two parts:-
1. BankSystem:- That handles user login and updation like: update password, update pin, forget password
2. BankAccount:- That handles transactions like: deposit , withdraw and money transfer

* This makes the system more clean and easy to scale for future requirements.
* I used Inheritance property to take the BankSystem Credentials to use in BankAccount

---

### Additional Features we can add:
- [done] Transaction History
- [done] Change Password
- [done] Change PIN
- [done] Multiple Users (using a dictionary)
- [done] Transfer Money between accounts
- [] Interest Calculation
- [done] Account Details
- [done] Logout option
- [done] Maximum 3 login attempts
- [done] Input validation (try-except)
- [done] Date and time of transactions
- [] Save data to a file (so balance persists after restarting)


---
**Author:** *Shiven Sharma*