#!/usr/bin/python3
from modules.book import Book
from modules.libraryuser import LibraryUser
from modules.librarystaff import LibraryStaff


class Library:
    """
    Represents a library.

    Attributes:
        books (list): A collection of books in the library.
        users (list): Registered library users.
        staff (list): Library staff members.
        historical_data (list): Historical data or records of library activities.

    Methods:
        list_books(): List all books in the library.
        find_book(title): Find a book by its title.
        authenticate_user(username, password): Authenticate a user or staff member.
    """

    def __init__(self):
        """
        Initialize a Library instance.
        """
        self.books = []
        self.users = []
        self.staff = []
        self.historical_data = []

    def list_books(self):
        """
        List all books in the library.

        Returns:
            list: A list of all books in the library.
        """
        return self.books

    def find_book(self, title):
        """
        Find a book by its title.

        Args:
            title (str): The title of the book to search for.

        Returns:
            Book: The book with the specified title, or None if not found.
        """
        for book in self.books:
            if book.title == title:
                return book
        return None

    def authenticate_user(self, username, password):
        """
        Authenticate a user or staff member.

        Args:
            username (str): The username for authentication.
            password (str): The password for authentication.

        Returns:
            object: The authenticated user or staff member, or None if authentication fails.
        """
        for user in self.users:
            if user.username == username and user.password == password:
                return user

        for staff_member in self.staff:
            if staff_member.username == username and staff_member.password == password:
                return staff_member

        return None
