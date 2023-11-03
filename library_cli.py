#!/usr/bin/python3
from modules.book import Book   
from modules.library import Library
from modules.libraryuser import LibraryUser
from modules.librarystaff import LibraryStaff

def main():
    library = Library()  # Create a Library instance

    while True:
        print("\nLibrary Management System")
        print("1. Log in as User")
        print("2. Log in as Staff")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            # User Login
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user = library.authenticate_user(username, password)
            if isinstance(user, LibraryUser):
                user_menu(user, library)
            else:
                print("Authentication failed. Please check your credentials.")

        elif choice == "2":
            # Staff Login
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            staff = library.authenticate_user(username, password)
            if isinstance(staff, LibraryStaff):
                staff_menu(staff, library)
            else:
                print("Authentication failed. Please check your credentials.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

def user_menu(user, library):
    while True:
        print("\nUser Menu")
        print("1. View Borrowed Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Reserve a Book")
        print("5. Log out")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            borrowed_books = user.view_borrowed_books()
            if borrowed_books:
                print("Borrowed Books:")
                for book in borrowed_books:
                    print(book.title)
            else:
                print("You have not borrowed any books.")
        
        elif choice == "2":
            title = input("Enter the title of the book you want to borrow: ")
            book = library.find_book(title)
            if book:
                result = user.borrow_book(book)
                print(result)
            else:
                print(f"Book '{title}' not found in the library.")
        
        elif choice == "3":
            title = input("Enter the title of the book you want to return: ")
            book = library.find_book(title)
            if book:
                result = user.return_book(book)
                print(result)
            else:
                print(f"Book '{title}' not found in your borrowed books.")
        
        elif choice == "4":
            title = input("Enter the title of the book you want to reserve: ")
            book = library.find_book(title)
            if book:
                result = user.reserve_book(book)
                print(result)
            else:
                print(f"Book '{title}' not found in the library.")
        
        elif choice == "5":
            print("Logged out.")
            break
        
        else:
            print("Invalid choice. Please try again.")

def staff_menu(staff, library):
    while True:
        print("\nStaff Menu")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Issue Fine")
        print("4. Log out")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the title of the book to add: ")
            author = input("Enter the author of the book: ")
            isbn = input("Enter the ISBN of the book: ")
            genre = input("Enter the genre of the book: ")
            tags = input("Enter tags or keywords (comma-separated): ").split(",")
            availability = input("Is the book available (True/False): ").lower() == "true"
            book = Book(title, author, isbn, genre, tags, availability)
            library.books.append(book)
            print(f"{title} has been added to the library.")

        elif choice == "2":
            title = input("Enter the title of the book to remove: ")
            book = library.find_book(title)
            if book:
                library.books.remove(book)
                print(f"{title} has been removed from the library.")
            else:
                print(f"Book '{title}' not found in the library.")

        elif choice == "3":
            username = input("Enter the username of the user to issue a fine to: ")
            amount = float(input("Enter the fine amount: "))
            user = library.authenticate_user(username, "password")  # Password is not required for issuing a fine in this example
            if isinstance(user, LibraryUser):
                # Implement the logic to issue a fine to the user
                print(f"A fine of ${amount:.2f} has been issued to {user.name}.")
            else:
                print(f"User '{username}' not found.")

        elif choice == "4":
            print("Logged out.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
