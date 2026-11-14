# Input students enrolled in two courses
course1 = set(input("Enter names for Course 1: ").split())
course2 = set(input("Enter names for Course 2: ").split())

print("Union:", course1.union(course2))
print("Intersection:", course1.intersection(course2))
print("Difference (Course 1 - Course 2):",
      course1.difference(course2))
print("Difference (Course 2 - Course 1):",
      course2.difference(course1))

# Tuple to store student details
roll = input("\nEnter roll number: ")
name = input("Enter student name: ")
department = input("Enter department: ")

student = (roll, name, department)

print("Student Details:", student)