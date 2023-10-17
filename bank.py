import random
class Account:
    accounts = []
    canTakeLoan = True

    def __init__(self, name, email, address, acctype):
        self.name = name  
        self.email = email
        self.address = address
        self.balance = 0
        self.type = acctype
        self.transactions = []
        self.loan_count = 0
        self.loanTaken = 0
        self.accountNo = random.randint(10000, 99999)

        Account.accounts.append(self)
        print(f"\n ---- > Account created successfully. Account No: {self.accountNo}")


    def deposit(self, amount):
        self.balance += amount
        print(f"\nDeposited ${amount}. \n Your New balance: ${self.balance}")


    def withdraw(self, amount):
        if 0 <= amount <= self.balance:
            self.balance -= amount
            print(f"\nWithdrew ${amount} and your New balance is: ${self.balance}")
        else:
            print("\nWithdrawal amount exceeded")


    def check_balance(self):
        print(f"\nCurrent Balance: ${self.balance}")


    def takeloan(self, amount):
        if self.canTakeLoan == True and self.loan_count < 2:
            self.loan_count += 1
            self.balance += amount
            self.loanTaken += amount
            print(f"\n you take loan =  ${amount}.")
        else:
            print("\n Loan not available")

    def transactions_history(self):
        print("\nTransaction history:")
        for transaction in self.transactions:
            print(transaction)

    def transfer(self, receiver, amount):
        if receiver not in Account.accounts:
            print("\n Account does not exist")
        else:
            if 0 <= amount <= self.balance:
                self.balance -= amount
                receiver.deposit(amount)
                print(f"\n Transferred ${amount} to {receiver.name}.")
                self.transactions.append(f" transferred ${amount} to the account : {receiver.name}")
            else:
                print("\n Invalid transfer amount")



class Admin:
  
    def delete_account(self, account_no):
        for account in Account.accounts:
            if account.accountNo == account_no:
                Account.accounts.remove(account)
                print(f"\nAccount No: {account_no} deleted.")
                return
        print(f"\nAccount No: {account_no} not found.")

    def show_all_users(self):
        print("\nUser Accounts lists:")
        for account in Account.accounts:
            print(f"Account No: {account.accountNo}, Name: {account.name} , balance: {account.balance}")

    def total_balance(self):
        Total = sum(account.balance for account in Account.accounts)
        print(f"\nTotal  Balance: ${Total}")

    
    def toggle_loan(self, value):
        Account.canTakeLoan = value

    def total_loan(self):
        totalLoan = sum(account.loanTaken for account in Account.accounts)
        print(f"\nTotal Loan Amount: ${totalLoan}")



admin_password = '1234'
isAdmin = False


current_user = None
while True:
    if current_user is None and not isAdmin:
        print("No user logged in!")
        ch = input("Register/login (R/L), If Admin(A): ")
        if ch == "R":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            account_type = input("Enter account type: ")
            current_user = Account(name, email, address, account_type)
        elif ch == "L":
            account_number = int(input("Account number: "))
            for user in Account.accounts:
                if user.accountNo == account_number:
                    current_user = user
                    break
            if current_user is None:
                print("Account not found.")
        elif ch == "A":
            password = input("Enter admin password: ")
            if password == admin_password:
                isAdmin = True
        else:
            print("Invalid choice")

    else:
        if isAdmin:
            print("\n Welcome admin! ")
            print("1. Create Account")
            print("2. Delete Account")
            print("3. Show All Accounts")
            print("4. Total Bank Balance")
            print("5. Total Loan")
            print("6. Toggle Loan Status")
            print("7. Exit")
            option  = input("Enter your option: ")

            if option  == "1":
                name = input("Enter user's name: ")
                email = input("Enter user's email: ")
                address = input("Enter user's address: ")
                account_type = input("Enter user's account type: ")
                Account(name, email, address, account_type)

            elif option  == "2":
                account_no = int(input("Enter Account No to delete: "))
                Admin().delete_account(account_no)

            elif option  == "3":
                Admin().show_all_users()

            elif option  == "4":
                Admin().total_balance()

            elif option  == "5":
                Admin().total_loan()

            elif option  == "6":
                toggle_choice = input("Enter 'True' or 'False' to toggle loan status: ")
                Admin().toggle_loan(toggle_choice)
                

            elif option  == "7":
                isAdmin = False

        else:
            print(f"\nWelcome {current_user.name} !\n")
            print("1. Deposit Money")
            print("2. Withdraw Money")
            print("3. Check Balance")
            print("4. Request loan")
            print("5. Transfer Money")
            print("6. Transaction History")
            print("7. Exit")
            option = input("Enter your option: ")

            if option == "1":
                amount = float(input("Enter the amount to deposit: "))
                current_user.deposit(amount)

            elif option == "2":
                amount = float(input("Enter the amount to withdraw: "))
                current_user.withdraw(amount)

            elif option == "3":
                current_user.check_balance()

            elif option == "4":
                amount = float(input("Enter the amount to loan: "))
                current_user.takeloan(amount)

            elif option == "5":
                amount = float(input("Enter the amount to transfer: "))
                receiver_account_no = int(input("Enter the receiver's Account No: "))
                for account in Account.accounts:
                    if account.accountNo == receiver_account_no:
                        current_user.transfer(account, amount)
                        break
                else:
                    print("Receiver not found.")

            elif option == "6":
                current_user.transactions_history()

            elif option == "7":
                current_user = None
