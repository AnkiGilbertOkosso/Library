#!/usr/bin/python3
from modules.book import Book
class LibraryUser:
    """
    Represents a library user.

    Attributes:
        name (str): The name of the user.
        user_id (str): A unique user ID.
        username (str): The username for logging in.
        password (str): The password for logging in.
        books_borrowed (list): A list of books borrowed by the user.
        reserved_books (list): A list of books reserved by the user.

    Methods:
        view_borrowed_books(): View the list of books currently borrowed by the user.
        borrow_book(book): Borrow a book from the library.
        return_book(book): Return a borrowed book to the library.
        reserve_book(book): Reserve a book from the library.
    """

    def __init__(self, name, user_id, username, password):
        """
        Initialize a LibraryUser instance.

        Args:
            name (str): The name of the user.
            user_id (str): A unique user ID.
            username (str): The username for logging in.
            password (str): The password for logging in.
        """
        self.name = name
        self.user_id = user_id
        self.username = username
        self.password = password
        self.books_borrowed = []
        self.reserved_books = []

    def view_borrowed_books(self):
        """
        View the list of books currently borrowed by the user.

        Returns:
            list: A list of books currently borrowed by the user.
        """
        return self.books_borrowed

    def borrow_book(self, book):
        """
        Borrow a book from the library.

        Args:
            book (Book): The book to be borrowed.

        Returns:
            str: A message indicating the success or failure of the borrowing operation.
        """
        if book in self.reserved_books:
            self.reserved_books.remove(book)
        if len(self.books_borrowed) < 3:
            self.books_borrowed.append(book)
            return f"{self.name} has borrowed {book.title}"
        else:
            return f"Sorry, {self.name} has borrowed the maximum number of books."

    def return_book(self, book):
        """
        Return a borrowed book to the library.

        Args:
            book (Book): The book to be returned.

        Returns:
            str: A message indicating the success or failure of the return operation.
        """
        if book in self.books_borrowed:
            self.books_borrowed.remove(book)
            return f"{self.name} has returned {book.title}"
        else:
            return f"{self.name} did not borrow {book.title}."

    def reserve_book(self, book):
        """
        Reserve a book from the library.

        Args:
            book (Book): The book to be reserved.

        Returns:
            str: A message indicating the success or failure of the reservation.
        """
        if book.availability and book not in self.reserved_books:
            self.reserved_books.append(book)
            return f"{self.name} has reserved {book.title}"
        elif book in self.reserved_books:
            return f"{self.name} has already reserved {book.title}"
        else:
            return f"Sorry, {book.title} is not available for reservation."
