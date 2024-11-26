import os

# File to store account data
ACCOUNTS_FILE = "accounts.txt"

def read_accounts():
    """Reads accounts from the file and returns them as a list of dictionaries."""
    accounts = []
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, "r") as file:
            for line in file:
                account_number, name, balance, history = line.strip().split(", ")
                accounts.append({
                    "account_number": account_number,
                    "name": name,
                    "balance": float(balance),
                    "history": history.split(";") if history else []
                })
    return accounts

def write_accounts(accounts):
    """Writes the list of accounts back to the file."""
    with open(ACCOUNTS_FILE, "w") as file:
        for account in accounts:
            history = ";".join(account["history"])
            file.write(f"{account['account_number']}, {account['name']}, {account['balance']}, {history}\n")

def create_account():
    """Creates a new account."""
    account_number = input("Enter a new account number: ").strip()
    name = input("Enter the account holder's name: ").strip()
    try:
        initial_deposit = float(input("Enter initial deposit amount: "))
        if initial_deposit < 0:
            print("Initial deposit cannot be negative.")
            return
    except ValueError:
        print("Invalid deposit amount.")
        return

    accounts = read_accounts()
    if any(acc["account_number"] == account_number for acc in accounts):
        print("Account number already exists.")
        return

    accounts.append({
        "account_number": account_number,
        "name": name,
        "balance": initial_deposit,
        "history": [f"Account created with deposit: {initial_deposit}"]
    })
    write_accounts(accounts)
    print("Account created successfully!")

def balance_inquiry():
    """Checks the balance for a specific account."""
    account_number = input("Enter the account number: ").strip()
    accounts = read_accounts()
    account = next((acc for acc in accounts if acc["account_number"] == account_number), None)
    if account:
        print(f"Account holder: {account['name']}")
        print(f"Balance: {account['balance']:.2f}")
    else:
        print("Account not found.")

def deposit():
    """Deposits money into an account."""
    account_number = input("Enter the account number: ").strip()
    accounts = read_accounts()
    account = next((acc for acc in accounts if acc["account_number"] == account_number), None)
    if account:
        try:
            amount = float(input("Enter the deposit amount: "))
            if amount <= 0:
                print("Deposit amount must be positive.")
                return
            account["balance"] += amount
            account["history"].append(f"Deposited: {amount}")
            write_accounts(accounts)
            print(f"Deposit successful! New balance: {account['balance']:.2f}")
        except ValueError:
            print("Invalid amount.")
    else:
        print("Account not found.")

def main():
    """Main function to handle user commands."""
    while True:
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Balance Inquiry")
        print("3. Deposit Money")
        print("4. Exit")
        choice = input("Select an option (1-4): ").strip()
        if choice == "1":
            create_account()
        elif choice == "2":
            balance_inquiry()
        elif choice == "3":
            deposit()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
