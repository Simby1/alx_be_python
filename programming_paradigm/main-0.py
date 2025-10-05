import sys
from bank_account import BankAccount

def main():
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Initializing account with a balance for testing scenarios
    # The initial balance should be adjusted for comprehensive testing
    account = BankAccount(100) 

    # Split the single argument (e.g., 'deposit:50') into command and amount
    try:
        command_params = sys.argv[1].split(':')
        command = command_params[0].lower()
        amount = float(command_params[1]) if len(command_params) > 1 else None
    except (IndexError, ValueError):
        # Handle cases like 'deposit' without an amount, or non-numeric amount
        command = sys.argv[1].lower() if len(sys.argv[1].split(':')) == 1 else None
        amount = None


    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command or missing amount for deposit/withdraw.")

if __name__ == "__main__":
    main()