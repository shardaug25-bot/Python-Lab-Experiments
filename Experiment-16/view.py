class StudentView:
    def show_menu(self):
        print("\n--- Student Information Management ---")
        print("1. Add student")
        print("2. Display all students")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("0. Exit")
        return input("Enter your choice: ").strip()

    def get_student_details(self):
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ").strip()
        department = input("Enter department: ").strip()
        year = int(input("Enter year of study: "))
        return student_id, name, department, year

    def get_student_id(self):
        return int(input("Enter student ID: "))

    def display_students(self, students):
        if not students:
            print("No student records found.")
            return
        print("\nID | Name | Department | Year")
        print("-" * 40)
        for student in students:
            print(f"{student[0]} | {student[1]} | {student[2]} | {student[3]}")

    def display_student(self, student):
        if student:
            print(f"ID: {student[0]}, Name: {student[1]}, "
                  f"Department: {student[2]}, Year: {student[3]}")
        else:
            print("Student not found.")

    def show_message(self, message):
        print(message)
