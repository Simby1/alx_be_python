class Book:
    """
    Represents a book in the library.
    Attributes: title, author (public) and _is_checked_out (private-like).
    """
    
    def __init__(self, title, author):
        """Initialize a Book with title, author, and availability."""
        self.title = title
        self.author = author
        # Private-like attribute for internal state (Encapsulation)
        self._is_checked_out = False 

    def check_out(self):
        """Checks the book out, making it unavailable."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Returns the book, making it available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns the current availability status of the book."""
        return not self._is_checked_out
    
    def __str__(self):
        """String representation of the book for display."""
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book objects.
    """
    
    def __init__(self):
        """Initialize the Library with an empty list of books."""
        # Private-like list to store books (Encapsulation)
        self._books = []

    def add_book(self, book):
        """Adds a Book object to the library's collection."""
        if isinstance(book, Book):
            self._books.append(book)

    def _find_book(self, title):
        """Helper method to find a book by its title."""
        for book in self._books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title):
        """
        Marks a book as checked out based on its title.
        Prints a message indicating success or failure.
        """
        book = self._find_book(title)
        if book and book.is_available():
            book.check_out()
            print(f"Checked out: {title}")
        elif book and not book.is_available():
            print(f"Error: '{title}' is already checked out.")
        else:
            print(f"Error: Book '{title}' not found.")

    def return_book(self, title):
        """
        Marks a book as returned, making it available again.
        Prints a message indicating success or failure.
        """
        book = self._find_book(title)
        if book and not book.is_available():
            book.return_book()
            print(f"Returned: {title}")
        elif book and book.is_available():
            print(f"Error: '{title}' was not checked out.")
        else:
            print(f"Error: Book '{title}' not found.")

    def list_available_books(self):
        """
        Prints the title and author of all books currently available.
        """
        available_count = 0
        for book in self._books:
            if book.is_available():
                print(book) # Uses the Book's __str__ method
                available_count += 1
        
        if available_count == 0 and len(self._books) > 0:
            print("No books are currently available.")
        elif len(self._books) == 0:
            print("The library is empty.")
