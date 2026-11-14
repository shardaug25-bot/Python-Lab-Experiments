import sqlite3

class StudentController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            choice = self.view.show_menu()
            try:
                if choice == "1":
                    details = self.view.get_student_details()
                    self.model.add_student(*details)
                    self.view.show_message("Student added successfully.")
                elif choice == "2":
                    self.view.display_students(self.model.get_all_students())
                elif choice == "3":
                    student_id = self.view.get_student_id()
                    self.view.display_student(self.model.search_student(student_id))
                elif choice == "4":
                    student_id = self.view.get_student_id()
                    if not self.model.search_student(student_id):
                        self.view.show_message("Student not found.")
                        continue
                    name = input("Enter new name: ").strip()
                    department = input("Enter new department: ").strip()
                    year = int(input("Enter new year of study: "))
                    updated = self.model.update_student(student_id, name, department, year)
                    self.view.show_message("Student updated." if updated else "Student not found.")
                elif choice == "5":
                    student_id = self.view.get_student_id()
                    deleted = self.model.delete_student(student_id)
                    self.view.show_message("Student deleted." if deleted else "Student not found.")
                elif choice == "0":
                    self.view.show_message("Exiting program.")
                    break
                else:
                    self.view.show_message("Invalid choice. Try again.")
            except ValueError:
                self.view.show_message("Invalid input. Enter numbers where required.")
            except sqlite3.IntegrityError:
                self.view.show_message("That student ID already exists.")
            except sqlite3.Error as error:
                self.view.show_message(f"Database error: {error}")
