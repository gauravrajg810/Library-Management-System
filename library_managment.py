
import json
import os

FILE_NAME = "library.txt"

def load_books():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            books = json.load(file)
            if isinstance(books, list):
                return books
            print("Warning: Invalid library data.")
            return []
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read library data.")
        return []

def save_books():
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(books, file, indent=4)
    except OSError:
        print("Error: Could not save library data.")

def generate_book_id():
    highest_id = 100

    for book in books:
        book_id = book.get("id", "")
        if isinstance(book_id, str) and book_id.startswith("B"):
            number = book_id[1:]
            if number.isdigit():
                highest_id = max(highest_id, int(number))

    return "B" + str(highest_id + 1)

def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()

    if not title or not author:
        print("Title and author cannot be empty.")
        return

    book_id = generate_book_id()

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "status": "Available",
        "issued_to": ""
    }

    books.append(book)
    print(
        f"Book added. ID: {book_id} | "
        f"{title} | {author} | Available"
    )

def issue_book():
    book_id = input("Enter book ID: ").strip().upper()

    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Issued":
                print("Book is already issued.")
                return

            member = input("Enter member name: ").strip()
            if not member:
                print("Member name cannot be empty.")
                return

            book["status"] = "Issued"
            book["issued_to"] = member

            print(
                f"Book {book_id} issued to {member}. "
                f"Status: Issued"
            )
            print("Available books:", count_available())
            return

    print(f"Book ID {book_id} not found.")

def return_book():
    book_id = input("Enter book ID: ").strip().upper()

    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Available":
                print("This book is already available.")
                return

            book["status"] = "Available"
            book["issued_to"] = ""

            print(
                f"Book {book_id} returned. "
                f"Status: Available"
            )
            return

    print(f"Book ID {book_id} not found.")

def search_books():
    keyword = input("Enter title or author to search: ").strip().lower()

    if not keyword:
        print("Search text cannot be empty.")
        return

    found = False

    for book in books:
        if (keyword in book["title"].lower()
                or keyword in book["author"].lower()):
            print(
                f'{book["id"]} | {book["title"]} | '
                f'{book["author"]} | {book["status"]}'
            )
            found = True

    if not found:
        print("No matching books found.")

def display_books():
    if not books:
        print("No books in the library.")
        return

    for book in books:
        print(
            f'{book["id"]} | {book["title"]} | '
            f'{book["author"]} | {book["status"]}'
        )

def count_available():
    count = 0

    for book in books:
        if book["status"] == "Available":
            count += 1

    return count

books = load_books()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Display All Books")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_book()
    elif choice == "2":
        issue_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        search_books()
    elif choice == "5":
        display_books()
    elif choice == "6":
        save_books()
        print("Library data saved. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1 to 6.")