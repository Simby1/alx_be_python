class BankAccount:
  
    def __init__(self, initial_balance=0):
        """
        Initializes the BankAccount with an optional starting balance.
        """
        # Encapsulation: Using a private-like attribute (by convention)
        # to store the balance, requiring interaction through methods.
        self._account_balance = initial_balance

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
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self._account_balance}")
