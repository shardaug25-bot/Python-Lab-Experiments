class SalaryReportView:
    def show_menu(self):
        print("\n--- Department-wise Salary Report ---")
        print("1. Add employee salary record")
        print("2. Show all department reports")
        print("3. Show report for one department")
        print("0. Exit")
        return input("Enter your choice: ").strip()

    def get_employee_details(self):
        employee_id = int(input("Enter employee ID: "))
        name = input("Enter employee name: ").strip()
        department = input("Enter department: ").strip()
        salary = float(input("Enter salary: "))
        return employee_id, name, department, salary

    def get_department(self):
        return input("Enter department name: ").strip()

    def display_reports(self, reports):
        if not reports:
            print("No salary records found.")
            return
        print("\nDepartment | Employees | Total Salary | Average | Minimum | Maximum")
        print("-" * 75)
        for row in reports:
            print(f"{row[0]} | {row[1]} | {row[2]:.2f} | {row[3]:.2f} | {row[4]:.2f} | {row[5]:.2f}")

    def display_report(self, report):
        if not report:
            print("No records found for that department.")
            return
        self.display_reports([report])

    def show_message(self, message):
        print(message)
