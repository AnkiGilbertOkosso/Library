import unittest
from modules.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        # Create a sample book for testing
        self.book = Book("Sample Book", "Sample Author", "978-1234567890", "Fiction", ["Adventure", "Mystery"], True)

    def test_get_info(self):
        self.assertEqual(self.book.get_info(), "Sample Book by Sample Author (Fiction)")

    def test_check_availability(self):
        self.assertEqual(self.book.check_availability(), "Available")

    def test_borrow_book(self):
        user = "John"
        self.assertEqual(self.book.borrow_book(user), "John has borrowed Sample Book")
        self.assertEqual(self.book.availability, False)

    def test_return_book(self):
        self.book.availability = False
        self.assertEqual(self.book.return_book(), "Sample Book has been returned")
        self.assertEqual(self.book.availability, True)

    def test_add_review(self):
        rating = 4
        review = "A great read!"
        self.assertEqual(self.book.add_review(rating, review), "Review and rating added successfully")
        self.assertEqual(self.book.ratings, [4])
        self.assertEqual(self.book.reviews, ["A great read!"])

if __name__ == '__main__':
    unittest.main()
