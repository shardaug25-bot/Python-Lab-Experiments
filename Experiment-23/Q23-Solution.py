# Experiment 23: XML Student Management

import xml.etree.ElementTree as ET
import os

filename = "student_records.xml"


# Create XML file if it does not exist
if os.path.exists(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
else:
    root = ET.Element("students")
    tree = ET.ElementTree(root)


# Add student
def add_student():
    roll = input("Enter roll number: ")

    if root.find(f"student/[roll='{roll}']") is not None:
        print("Roll number already exists.")
        return

    name = input("Enter name: ")
    department = input("Enter department: ")
    cgpa = input("Enter CGPA: ")

    student = ET.SubElement(root, "student")

    ET.SubElement(student, "roll").text = roll
    ET.SubElement(student, "name").text = name
    ET.SubElement(student, "department").text = department
    ET.SubElement(student, "cgpa").text = cgpa

    tree.write(filename, encoding="utf-8", xml_declaration=True)

    print("Student added successfully.")


# Display students
def display_students():
    print("\nStudent Records")

    for student in root.findall("student"):
        print(
            student.findtext("roll"),
            student.findtext("name"),
            student.findtext("department"),
            student.findtext("cgpa")
        )


# Search student
def search_student():
    roll = input("Enter roll number to search: ")

    for student in root.findall("student"):
        if student.findtext("roll") == roll:
            print("\nStudent Found")
            print("Name:", student.findtext("name"))
            print("Department:", student.findtext("department"))
            print("CGPA:", student.findtext("cgpa"))
            return

    print("Student not found.")


# Delete student
def delete_student():
    roll = input("Enter roll number to delete: ")

    for student in root.findall("student"):
        if student.findtext("roll") == roll:
            root.remove(student)
            tree.write(
                filename,
                encoding="utf-8",
                xml_declaration=True
            )
            print("Student deleted successfully.")
            return

    print("Student not found.")


# Main menu
while True:
    print("\n--- XML Student Management ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")