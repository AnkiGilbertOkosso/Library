import json
import os
from modules.library import Library
from modules.libraryuser import LibraryUser
from modules.librarystaff import LibraryStaff

DATA_DIR = "data"  # Directory for data files

def save_data(data, filename):
    data_path = os.path.join(DATA_DIR, filename)
    with open(data_path, "w") as file:
        json.dump(data, file, indent=4)

def load_data(filename):
    data_path = os.path.join(DATA_DIR, filename)
    if os.path.exists(data_path):
        with open(data_path, "r") as file:
            return json.load(file)
    else:
        return None

def load_library_data():
    library_data = load_data("library_data.json")
    if library_data:
        return library_data
    else:
        return Library()

def save_library_data(library):
    save_data(library, "library_data.json")

def load_user_data():
    user_data = load_data("user_data.json")
    if user_data:
        return user_data
    else:
        return []

def save_user_data(users):
    save_data(users, "user_data.json")

def load_staff_data():
    staff_data = load_data("staff_data.json")
    if staff_data:
        return staff_data
    else:
        return []

def save_staff_data(staff):
    save_data(staff, "staff_data.json")

def main():
    library = load_library_data()  # Load library data from JSON file
    users = load_user_data()  # Load user data from JSON file
    staff = load_staff_data()  # Load staff data from JSON file

    while True:
        print("\n--- Library Management System Menu ---")
        print("1. Manage Library")
        print("2. Manage Users")
        print("3. Manage Staff")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library_menu(library)
        # elif choice == "2":
        #     users_menu(users)
        # elif choice == "3":
        #     staff_menu(staff)
        # elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

    # Save data when the program exits
    save_library_data(library)  # Save library data to JSON file
    save_user_data(users)  # Save user data to JSON file
    save_staff_data(staff)  # Save staff data to JSON file

def library_menu(library):
    while True:
        print("\n--- Library Management Menu ---")
        print("1. List Books")
        print("2. Find a Book")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_books(library)
        elif choice == "2":
            find_book(library)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def list_books(library):
    books = library.list_books()
    if books:
        print("\nLibrary Books:")
        for book in books:
            print(book.title)
    else:
        print("\nThe library has no books at the moment.")

def find_book(library):
    title = input("Enter the title of the book to find: ")
    book = library.find_book(title)
    if book:
        print(f"Book '{book.title}' found.")
    else:
        print(f"Book '{title}' not found in the library.")


if __name__ == "__main__":
    main()
