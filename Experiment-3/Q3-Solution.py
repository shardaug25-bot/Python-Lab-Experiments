students = {}

while True:
    print("\n1. Insert Student")
    print("2. Delete Student")
    print("3. Search Student")
    print("4. Display Students")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll = input("Enter roll number: ")
        name = input("Enter student name: ")
        department = input("Enter department: ")

        students[roll] = {
            "Name": name,
            "Department": department
        }

        print("Student inserted successfully")

    elif choice == 2:
        roll = input("Enter roll number to delete: ")

        if roll in students:
            del students[roll]
            print("Student deleted successfully")
        else:
            print("Student not found")

    elif choice == 3:
        roll = input("Enter roll number to search: ")

        if roll in students:
            print(students[roll])
        else:
            print("Student not found")

    elif choice == 4:
        for roll, details in students.items():
            print(roll, details)

    elif choice == 5:
        break

    else:
        print("Invalid choice")