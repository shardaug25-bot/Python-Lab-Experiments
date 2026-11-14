import sqlite3

DB_NAME = "students.db"

class StudentModel:
    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        with self.connect() as con:
            con.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    student_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    department TEXT NOT NULL,
                    year INTEGER NOT NULL
                )
            """)

    def add_student(self, student_id, name, department, year):
        with self.connect() as con:
            con.execute(
                "INSERT INTO students (student_id, name, department, year) VALUES (?, ?, ?, ?)",
                (student_id, name, department, year)
            )

    def get_all_students(self):
        with self.connect() as con:
            return con.execute(
                "SELECT student_id, name, department, year FROM students ORDER BY student_id"
            ).fetchall()

    def search_student(self, student_id):
        with self.connect() as con:
            return con.execute(
                "SELECT student_id, name, department, year FROM students WHERE student_id = ?",
                (student_id,)
            ).fetchone()

    def update_student(self, student_id, name, department, year):
        with self.connect() as con:
            cursor = con.execute(
                "UPDATE students SET name = ?, department = ?, year = ? WHERE student_id = ?",
                (name, department, year, student_id)
            )
            return cursor.rowcount > 0

    def delete_student(self, student_id):
        with self.connect() as con:
            cursor = con.execute(
                "DELETE FROM students WHERE student_id = ?", (student_id,)
            )
            return cursor.rowcount > 0
