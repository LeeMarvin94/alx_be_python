# library_management.py

class Book:
    """A class representing a book with a title, author, and its checked out status."""

    def __init__(self, title, author):
        """Initialize the book with a title, author, and set its checked out status to False."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """A class representing a library that manages a collection of books."""

    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Add a book to the library's collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title, marking it as unavailable."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"{title} has been checked out.")
                else:
                    print(f"{title} is already checked out.")
                return
        print(f"{title} not found in the library.")

    def return_book(self, title):
        """Return a book by title, marking it as available."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"{title} has been returned.")
                else:
                    print(f"{title} was not checked out.")
                return
        print(f"{title} not found in the library.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No available books at the moment.")

# library_management.py

class Book:
    """A class representing a book with a title, author, and its checked out status."""

    def __init__(self, title, author):
        """Initialize the book with a title, author, and set its checked out status to False."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """A class representing a library that manages a collection of books."""

    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Add a book to the library's collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title, marking it as unavailable."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"{title} has been checked out.")
                else:
                    print(f"{title} is already checked out.")
                return
        print(f"{title} not found in the library.")

    def return_book(self, title):
        """Return a book by title, marking it as available."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"{title} has been returned.")
                else:
                    print(f"{title} was not checked out.")
                return
        print(f"{title} not found in the library.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No available books at the moment.")


