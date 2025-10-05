class BankAccount:

    def __init__(self, initial_balance=0):
        """
        Initializes the BankAccount with an optional starting balance.
        """
        # Ensure the initial balance is treated as a float
        self._account_balance = float(initial_balance) 

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.
        """
        if amount > 0:
            self._account_balance += amount

    def withdraw(self, amount):
        """
        Deducts the amount from the balance if funds are sufficient.
        Returns True on success, False otherwise.
        """
        if amount > 0 and self._account_balance >= amount:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Prints the current account balance formatted with two decimal places.
        """
        # FIX: Use f-string formatting with ':.2f' to display two decimal places
        # This will convert 250 to 250.00
        print(f"Current Balance: ${self._account_balance:.2f}") 
