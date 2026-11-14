class EmployeeView:
    def show_menu(self):
        print("\n--- Employee Management ---")
        print("1. Add employee")
        print("2. Display all employees")
        print("3. Search employee")
        print("4. Update employee")
        print("5. Delete employee")
        print("0. Exit")
        return input("Enter your choice: ").strip()

    def get_employee_details(self):
        employee_id = int(input("Enter employee ID: "))
        name = input("Enter employee name: ").strip()
        department = input("Enter department: ").strip()
        salary = float(input("Enter salary: "))
        return employee_id, name, department, salary

    def get_employee_id(self):
        return int(input("Enter employee ID: "))

    def display_employees(self, employees):
        if not employees:
            print("No employee records found.")
            return
        print("\nID | Name | Department | Salary")
        print("-" * 45)
        for employee in employees:
            print(f"{employee[0]} | {employee[1]} | {employee[2]} | {employee[3]:.2f}")

    def display_employee(self, employee):
        if employee:
            print(f"ID: {employee[0]}, Name: {employee[1]}, "
                  f"Department: {employee[2]}, Salary: {employee[3]:.2f}")
        else:
            print("Employee not found.")

    def show_message(self, message):
        print(message)
