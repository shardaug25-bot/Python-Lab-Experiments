import sqlite3

class SalaryReportController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            choice = self.view.show_menu()
            try:
                if choice == "1":
                    self.model.add_employee(*self.view.get_employee_details())
                    self.view.show_message("Employee salary record added.")
                elif choice == "2":
                    self.view.display_reports(self.model.get_all_department_reports())
                elif choice == "3":
                    department = self.view.get_department()
                    self.view.display_report(self.model.get_department_report(department))
                elif choice == "0":
                    self.view.show_message("Exiting program.")
                    break
                else:
                    self.view.show_message("Invalid choice. Try again.")
            except ValueError:
                self.view.show_message("Invalid input. Enter a numeric ID and salary.")
            except sqlite3.IntegrityError:
                self.view.show_message("That employee ID already exists.")
            except sqlite3.Error as error:
                self.view.show_message(f"Database error: {error}")