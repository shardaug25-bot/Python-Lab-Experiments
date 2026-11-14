import sqlite3

class EmployeeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            choice = self.view.show_menu()
            try:
                if choice == "1":
                    self.model.add_employee(*self.view.get_employee_details())
                    self.view.show_message("Employee added successfully.")
                elif choice == "2":
                    self.view.display_employees(self.model.get_all_employees())
                elif choice == "3":
                    employee_id = self.view.get_employee_id()
                    self.view.display_employee(self.model.search_employee(employee_id))
                elif choice == "4":
                    employee_id = self.view.get_employee_id()
                    if not self.model.search_employee(employee_id):
                        self.view.show_message("Employee not found.")
                        continue
                    name = input("Enter new name: ").strip()
                    department = input("Enter new department: ").strip()
                    salary = float(input("Enter new salary: "))
                    updated = self.model.update_employee(employee_id, name, department, salary)
                    self.view.show_message("Employee updated." if updated else "Employee not found.")
                elif choice == "5":
                    employee_id = self.view.get_employee_id()
                    deleted = self.model.delete_employee(employee_id)
                    self.view.show_message("Employee deleted." if deleted else "Employee not found.")
                elif choice == "0":
                    self.view.show_message("Exiting program.")
                    break
                else:
                    self.view.show_message("Invalid choice. Try again.")
            except ValueError:
                self.view.show_message("Invalid input. Enter a valid ID and numeric salary.")
            except sqlite3.IntegrityError:
                self.view.show_message("That employee ID already exists.")
            except sqlite3.Error as error:
                self.view.show_message(f"Database error: {error}")
