import logging
from account.user import User
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

users = []

def create_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    user = User(name, email)
    if not user.is_valid_email(email):
        logging.error("Invalid email address!")
        return
    users.append(user)
    logging.info(f"User {name} created.\n")

def list_users():
    if not users:
        logging.info("No users available.\n")
        return False
    for i, user in enumerate(users):
        logging.info(f"{i+1}. {user}")
    return True

def create_account():
    if not users:  # Check if the users list is empty
        logging.info("No users available. Please create a user first.\n")
        return
    try:
        idx = int(input("Select user number: ")) - 1
        if idx < 0 or idx >= len(users):
            logging.error("Invalid user selection.\n")  # Updated error message
            return
        logging.info("Account Type:")
        logging.info("1. Savings Account")
        logging.info("2. Students Account")
        logging.info("3. Current Account")
        account_choice = int(input("Enter your choice (1, 2, 3): "))
        amount = float(input("Enter initial deposit: "))

        if account_choice == 1:
            account = SavingsAccount(amount)
        elif account_choice == 2:
            account = StudentAccount(amount)
        elif account_choice == 3:
            account = CurrentAccount(amount)
        else:
            logging.error("Invalid choice!")
            return

        users[idx].add_account(account)
        logging.info(f"{account.get_account_type()} added!\n")
    except ValueError:
        logging.error("Invalid input! Please enter a valid number.\n")

def deposit_money():
    list_users()
    idx = int(input("Select user: ")) - 1
    user = users[idx]
    for i, acc in enumerate(user.accounts):
        logging.info(f"{i+1}. Balance: Rs. {acc.get_balance()}")
    acc_idx = int(input("Select account: ")) - 1
    amount = float(input("Enter amount to deposit: "))  # Fixed bug
    user.accounts[acc_idx].deposit(amount)

def withdraw_money():
    list_users()
    idx = int(input("Select user: ")) - 1
    user = users[idx]
    for i, acc in enumerate(user.accounts):
        logging.info(f"{i+1}. Balance: Rs. {acc.get_balance()}")
    acc_idx = int(input("Select account: ")) - 1
    amount = float(input("Enter amount to withdraw: "))
    try:
        user.accounts[acc_idx].withdraw(amount)
        logging.info("Withdrawal successful.\n")
    except ValueError as e:
        logging.error(f"Error: {e}\n")

def view_transactions():
    list_users()
    idx = int(input("Select user: ")) - 1
    user = users[idx]
    for i, acc in enumerate(user.accounts):
        logging.info(f"\n{acc.get_account_type()} {i+1} - Balance: Rs. {acc.get_balance()}")
        for tx in acc.get_transaction_history():
            logging.info(tx)

