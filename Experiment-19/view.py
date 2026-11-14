class LibraryView:
    def show_menu(self):
        print("\n--- Library Record Management ---")
        print("1. Add book")
        print("2. Display all books")
        print("3. Search book")
        print("4. Update book details")
        print("5. Issue book")
        print("6. Return book")
        print("7. Delete book")
        print("0. Exit")
        return input("Enter your choice: ").strip()

    def get_book_details(self):
        book_id = int(input("Enter book ID: "))
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        return book_id, title, author

    def get_book_id(self):
        return int(input("Enter book ID: "))

    def display_books(self, books):
        if not books:
            print("No book records found.")
            return
        print("\nID | Title | Author | Status")
        print("-" * 55)
        for book in books:
            print(f"{book[0]} | {book[1]} | {book[2]} | {book[3]}")

    def display_book(self, book):
        if book:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Status: {book[3]}")
        else:
            print("Book not found.")

    def show_message(self, message):
        print(message)
