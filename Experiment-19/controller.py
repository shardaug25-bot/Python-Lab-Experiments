import sqlite3

class LibraryController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            choice = self.view.show_menu()
            try:
                if choice == "1":
                    self.model.add_book(*self.view.get_book_details())
                    self.view.show_message("Book added successfully.")
                elif choice == "2":
                    self.view.display_books(self.model.get_all_books())
                elif choice == "3":
                    book_id = self.view.get_book_id()
                    self.view.display_book(self.model.search_book(book_id))
                elif choice == "4":
                    book_id = self.view.get_book_id()
                    if not self.model.search_book(book_id):
                        self.view.show_message("Book not found.")
                        continue
                    title = input("Enter new title: ").strip()
                    author = input("Enter new author: ").strip()
                    updated = self.model.update_book(book_id, title, author)
                    self.view.show_message("Book updated." if updated else "Book not found.")
                elif choice in ("5", "6"):
                    book_id = self.view.get_book_id()
                    status = "Issued" if choice == "5" else "Available"
                    updated = self.model.set_book_status(book_id, status)
                    if updated:
                        self.view.show_message("Book issued." if choice == "5" else "Book returned.")
                    else:
                        self.view.show_message("Book not found.")
                elif choice == "7":
                    book_id = self.view.get_book_id()
                    deleted = self.model.delete_book(book_id)
                    self.view.show_message("Book deleted." if deleted else "Book not found.")
                elif choice == "0":
                    self.view.show_message("Exiting program.")
                    break
                else:
                    self.view.show_message("Invalid choice. Try again.")
            except ValueError as error:
                self.view.show_message(f"Invalid input: {error}")
            except sqlite3.IntegrityError:
                self.view.show_message("That book ID already exists.")
            except sqlite3.Error as error:
                self.view.show_message(f"Database error: {error}")
