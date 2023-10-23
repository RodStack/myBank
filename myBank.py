import csv

all_accounts = []

class Account:
    account_id = 1
    def __init__(self, name, balance, account_type):
        self.account_number = Account.account_id
        self.name = name
        self.balance = balance
        self.account_type = account_type
        Account.account_id += 1
        all_accounts.append(self)

    def deposit(self, amount):
        amount = float(amount)
        self.balance += amount
        print(f"Deposited {amount} into your account\n")
       

    def withdraw(self, amount):
        amount = float(amount)
        if amount > self.balance:
            print("Insufficient balance\n")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} from your account\n")
            

    def delete_account(self):
        if self.balance == 0:
            all_accounts.remove(self)
            print(f"Account {self.account_number} has been closed.")
        else:
            print(f"Account {self.account_number} cannot be closed because the balance is not 0.")

    def __str__(self):
        return f"Account Holder: {self.name} \nAccount Number: {self.account_number}\nAccount Type: {self.account_type} \nBalance: {self.balance}\n"
    
    @property
    def account_type(self):
        return self._account_type
    @account_type.setter
    def account_type(self, account_type):
        if account_type not in ["Checking", "Savings"]:
            raise ValueError("Account not available")
        self._account_type = account_type

def find_account_by_num(num):
    for account in all_accounts:
        if account.account_number == num:
            return account
    return None

def show_all():
    for account in all_accounts:
        print(account)
        print("--------------------------")

def total_balance():
    total = sum(account.balance for account in all_accounts)
    return total


def save_to_csv():
    with open("accounts.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Account Number", "Account Holder Name", "Balance", "Account Type"])
        for account in all_accounts:
            writer.writerow([account.account_number, account.name, account.balance, account.account_type])

def load_from_csv():
    try:
        with open("accounts.csv", mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                account_number, name, balance, account_type = row
                account = Account(name, float(balance), account_type)
                account.account_number = int(account_number)
    except FileNotFoundError:
        print("CSV file not found. A new one will be created when saving account information.")

def main():
    load_from_csv()  
    while True:
        print("Welcome")
        print("Choose an option:")
        print("1. Create a new account")
        print("2. Perform transactions on an account")
        print("3. Show all accounts")
        print("4. Close an account")
        print("5. Show total balance")
        print("6. Exit")
        choice = input()

        if choice == "1":
            name = input("Account Holder Name: ")
            balance = float(input("Initial Balance: "))
            account_type = input("Account Type: ")
            account = Account(name, balance, account_type)
            print(f"Account created for {name} with an initial balance of {balance} and type {account_type}\n")

        elif choice == "2":
            if not all_accounts:
                print("No accounts available. Create an account first.\n")
                continue

            print("Choose the account for transactions:")
            for account in all_accounts:
                print(f"{account.account_number}. {account.name}")

            account_number = int(input())
            selected_account = find_account_by_num(account_number)

            if selected_account:
                print(f"Transactions for the account of {selected_account.name}")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                option = input()

                if option == "1":
                    amount = input("Enter the amount to deposit: ")
                    selected_account.deposit(amount)

                elif option == "2":
                    amount = input("Enter the amount to withdraw: ")
                    selected_account.withdraw(amount)

                elif option == "3":
                    print(selected_account)

                else:
                    print("Invalid option.\n")

            else:
                print("Invalid account number.\n")

        elif choice == "3":
            print("All accounts:")
            show_all()

        elif choice == "4":
            if not all_accounts:
                print("No accounts available.\n")
                continue

            print("Choose the account to close:")
            for account in all_accounts:
                print(f"{account.account_number}. {account.name} - Balance: {account.balance}")
            account_number = int(input())
            selected_account = find_account_by_num(account_number)

            if selected_account:
                selected_account.delete_account()


        elif choice == "5":
            total = total_balance()
            print(f"Total balance across all accounts: {total}\n")
            
        elif choice == "6":
            save_to_csv()
            print("Thank you for using the system. Goodbye!")
            break

        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main()
