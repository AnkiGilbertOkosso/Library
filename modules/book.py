#!/usr/bin/python3

class Book:
    """
    Represents a book in the library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN (International Standard Book Number) of the book.
        genre (str): The genre of the book.
        tags (list of str): Tags or keywords associated with the book.
        availability (bool): Whether the book is available for borrowing.
        ratings (list of int): User ratings for the book.
        reviews (list of str): User reviews of the book.
        due_date (str): The due date for returning the book.

    Methods:
        get_info(): Get information about the book.
        check_availability(): Check if the book is available.
        borrow_book(user): Allow a user to borrow the book.
        return_book(): Return the book to the library.
        add_review(rating, review): Add a user review and rating for the book.
    """

    def __init__(self, title, author, isbn, genre, tags, availability):
        """
        Initialize a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
            genre (str): The genre of the book.
            tags (list of str): Tags or keywords associated with the book.
            availability (bool): Whether the book is available for borrowing.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.tags = tags
        self.availability = availability
        self.ratings = []
        self.reviews = []
        self.due_date = None

    def get_info(self):
        """
        Get information about the book.

        Returns:
            str: A string containing the book's title, author, and genre.
        """
        return f"{self.title} by {self.author} ({self.genre})"

    def check_availability(self):
        """
        Check if the book is available for borrowing.

        Returns:
            str: "Available" if the book is available, "Not available" otherwise.
        """
        return "Available" if self.availability else "Not available"

    def borrow_book(self, user):
        """
        Allow a user to borrow the book.

        Args:
            user (str): The name of the user borrowing the book.

        Returns:
            str: A message indicating the success or failure of the borrowing operation.
        """
        if self.availability:
            self.availability = False
            return f"{user} has borrowed {self.title}"
        else:
            return f"Sorry, {self.title} is not available."

    def return_book(self):
        """
        Return the book to the library.

        Returns:
            str: A message indicating the success or failure of the return operation.
        """
        if not self.availability:
            self.availability = True
            return f"{self.title} has been returned."
        else:
            return f"{self.title} is already available."

    def add_review(self, rating, review):
        """
        Add a user review and rating for the book.

        Args:
            rating (int): The user's rating for the book.
            review (str): The user's review of the book.

        Returns:
            str: A message confirming the addition of the review and rating.
        """
        self.ratings.append(rating)
        self.reviews.append(review)
        return "Review and rating added successfully."
