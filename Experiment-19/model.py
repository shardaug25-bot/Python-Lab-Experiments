import sqlite3

DB_NAME = "library.db"

class LibraryModel:
    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        with self.connect() as con:
            con.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    book_id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    status TEXT NOT NULL DEFAULT 'Available'
                        CHECK(status IN ('Available', 'Issued'))
                )
            """)

    def add_book(self, book_id, title, author):
        with self.connect() as con:
            con.execute(
                "INSERT INTO books (book_id, title, author, status) VALUES (?, ?, ?, 'Available')",
                (book_id, title, author)
            )

    def get_all_books(self):
        with self.connect() as con:
            return con.execute(
                "SELECT book_id, title, author, status FROM books ORDER BY book_id"
            ).fetchall()

    def search_book(self, book_id):
        with self.connect() as con:
            return con.execute(
                "SELECT book_id, title, author, status FROM books WHERE book_id = ?",
                (book_id,)
            ).fetchone()

    def update_book(self, book_id, title, author):
        with self.connect() as con:
            cursor = con.execute(
                "UPDATE books SET title = ?, author = ? WHERE book_id = ?",
                (title, author, book_id)
            )
            return cursor.rowcount > 0

    def set_book_status(self, book_id, status):
        if status not in ("Available", "Issued"):
            raise ValueError("Status must be Available or Issued.")
        with self.connect() as con:
            cursor = con.execute(
                "UPDATE books SET status = ? WHERE book_id = ?", (status, book_id)
            )
            return cursor.rowcount > 0

    def delete_book(self, book_id):
        with self.connect() as con:
            cursor = con.execute("DELETE FROM books WHERE book_id = ?", (book_id,))
            return cursor.rowcount > 0
