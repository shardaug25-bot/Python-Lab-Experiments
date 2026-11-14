import sqlite3

DB_NAME = "employees.db"

class EmployeeModel:
    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        with self.connect() as con:
            con.execute("""
                CREATE TABLE IF NOT EXISTS employees (
                    employee_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    department TEXT NOT NULL,
                    salary REAL NOT NULL
                )
            """)

    def add_employee(self, employee_id, name, department, salary):
        with self.connect() as con:
            con.execute(
                "INSERT INTO employees (employee_id, name, department, salary) VALUES (?, ?, ?, ?)",
                (employee_id, name, department, salary)
            )

    def get_all_employees(self):
        with self.connect() as con:
            return con.execute(
                "SELECT employee_id, name, department, salary FROM employees ORDER BY employee_id"
            ).fetchall()

    def search_employee(self, employee_id):
        with self.connect() as con:
            return con.execute(
                "SELECT employee_id, name, department, salary FROM employees WHERE employee_id = ?",
                (employee_id,)
            ).fetchone()

    def update_employee(self, employee_id, name, department, salary):
        with self.connect() as con:
            cursor = con.execute(
                "UPDATE employees SET name = ?, department = ?, salary = ? WHERE employee_id = ?",
                (name, department, salary, employee_id)
            )
            return cursor.rowcount > 0

    def delete_employee(self, employee_id):
        with self.connect() as con:
            cursor = con.execute(
                "DELETE FROM employees WHERE employee_id = ?", (employee_id,)
            )
            return cursor.rowcount > 0
