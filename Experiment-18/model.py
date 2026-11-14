import sqlite3

DB_NAME = "salary_report.db"

class SalaryReportModel:
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

    def get_departments(self):
        with self.connect() as con:
            return [row[0] for row in con.execute(
                "SELECT DISTINCT department FROM employees ORDER BY department"
            ).fetchall()]

    def get_department_report(self, department):
        # Parameterized query: user input is passed separately from SQL.
        with self.connect() as con:
            return con.execute(
                """SELECT department, COUNT(*), SUM(salary), AVG(salary), MIN(salary), MAX(salary)
                   FROM employees WHERE department = ? GROUP BY department""",
                (department,)
            ).fetchone()

    def get_all_department_reports(self):
        with self.connect() as con:
            return con.execute(
                """SELECT department, COUNT(*), SUM(salary), AVG(salary), MIN(salary), MAX(salary)
                   FROM employees GROUP BY department ORDER BY department"""
            ).fetchall()
