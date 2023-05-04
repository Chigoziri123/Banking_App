class Bank:
    """A class called bank"""
   # Initializing an empty customers dictionary
    def __init__(self):
        
        self.customers = {}
    # Registering a new customer account
    def register(self, name:str, account:str, password:str) -> str:
        if account in self.customers:
            return "Account already exists" """This indicates whether the registration was successful or not"""
        self.customers[account] = {"name": name, "password":password, "balance": 0, "transactions": []}
        return "Registration successful"
    # Authenticating a user
    def login(self, account:str, password:str) -> str:
        if account not in self.customers:
            return "Account does not exist"
        if self.customers[account]["password"] != password:
            return "Invalid password"
        return "Login successful"
    # Depositing money into a customer's account
    def deposit(self, account, amount):
        if account not in self.customers:
            return "Account does not exist"
        self.customers[account]["balance"] += amount
        self.customers[account]["transactions"]
        return "Deposit successful!"
# Transferring money from one account to another.
def transfer(self, account:str, recipient_account:str, amount:float) -> str:
        if account not in self.customers:
            return "Account does not exist"
        if recipient_account not in self.customers:
            return "Recipient account does not exist"
        if self.customers[account]["balance"] < amount:
            return "Insufficient funds"
        self.customers[account]["balance"] -= amount
        self.customers[account]["transactions"].append(f"You transferred {amount} to {recipient_account}")
        self.customers[recipient_account]["balance"] += amount
        self.customers[recipient_account]["transactions"].append(f"You received {amount} from {account}")
        return "Transfer successful"
# Returns transaction history
def history(self, account:str):
        if account not in self.customers:
            return "Account does not exist"
        # Looping through the transactions to obtain users' transaction history.
        for transaction in self.customers[account]["transactions"]:
            return transaction
# To check the current balance of a customer's account.
def check_balance(self, account):
        if account not in self.customers:
            return "Account does not exist"
        return f"Your balance is {self.customers[account]['balance']}"

"""Creating an object from the class Bank"""
XYZbank = Bank()
# Creating a user interface for users to input data
while True:
    print("Welcome to Chigoziri Bank!")
    print("1. Register")
    print("2. Login")
    print("3. Deposit")
    print("4. Transfer")
    print("5. Check balance")
    print("6. Transaction history")
    print("7. Exit")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        """ This is for registration """

        name = input("Enter your name: ")
        account = input("Enter your email: ")
        password = input("Enter your password: ")
        print(XYZbank.register(name, account, password))

    elif choice == "2":
        account = input("Enter your email: ")
        password = input("Enter your password: ")
        print(XYZbank.login(account, password))

    elif choice == "3":
        account = input("Enter your email: ")
        amount = float(input("Enter the amount to deposit: "))
        print(XYZbank.deposit(account, amount))

    elif choice == "4":
        account = input("Enter your email: ")
        recipient_account = input("Enter the recipient's email: ")
        amount = float(input("Enter the amount to transfer: "))
        print(XYZbank.transfer(account, recipient_account, amount))

    elif choice == "5":
        account = input("Enter your email: ")
        print(XYZbank.check_balance(account))

    elif choice == "6":
        account = input("Enter your email: ")
        print(XYZbank.history(account))

    elif choice == "7":
        print("Thank you for using the Bank!")
        break # To break here and start from the beginning.

    else:
        print("Invalid choice. Please try again.") 