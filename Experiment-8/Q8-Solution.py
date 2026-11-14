# Experiment 8: NumPy Array Operations

import numpy as np

students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

mid_marks = []
end_marks = []

print("\nEnter Mid-Semester Marks")

for i in range(students):
    marks = list(map(float, input(
        f"Enter marks of Student {i + 1}: "
    ).split()))

    if len(marks) != subjects:
        print("Incorrect number of marks.")
        exit()

    mid_marks.append(marks)


print("\nEnter End-Semester Marks")

for i in range(students):
    marks = list(map(float, input(
        f"Enter marks of Student {i + 1}: "
    ).split()))

    if len(marks) != subjects:
        print("Incorrect number of marks.")
        exit()

    end_marks.append(marks)


# Convert lists into NumPy arrays
mid = np.array(mid_marks)
end = np.array(end_marks)

# Vectorized calculations
mid_total = np.sum(mid, axis=1)
end_total = np.sum(end, axis=1)

mid_average = np.mean(mid, axis=1)
end_average = np.mean(end, axis=1)

improvement = np.zeros(students)

nonzero = mid_total != 0

improvement[nonzero] = (
    (end_total[nonzero] - mid_total[nonzero])
    / mid_total[nonzero]
) * 100


# Display results
print("\nStudent Results")

for i in range(students):
    print("\nStudent", i + 1)
    print("Mid-Semester Total:", mid_total[i])
    print("End-Semester Total:", end_total[i])
    print("Mid-Semester Average:", mid_average[i])
    print("End-Semester Average:", end_average[i])
    print("Percentage Improvement:", round(improvement[i], 2), "%")