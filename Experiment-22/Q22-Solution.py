# Experiment 22: Parse and Display XML Data

import xml.etree.ElementTree as ET

# Take XML filename
filename = input("Enter XML filename: ")

try:
    # Parse XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    print("\nXML Data")
    print("Root Element:", root.tag)

    # Display student details
    for student in root.findall("student"):

        roll = student.find("roll").text
        name = student.find("name").text
        department = student.find("department").text
        cgpa = student.find("cgpa").text

        print("\nStudent Details")
        print("Roll Number:", roll)
        print("Name:", name)
        print("Department:", department)
        print("CGPA:", cgpa)

except FileNotFoundError:
    print("XML file not found.")

except ET.ParseError:
    print("Invalid XML format.")

