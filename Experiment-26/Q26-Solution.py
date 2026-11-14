import matplotlib.pyplot as plt

students, hours, scores = [], [], []
n = int(input("Number of students: "))
for i in range(n):
    student = input(f"Student {i+1} name/ID: ").strip()
    study = float(input("Study hours per week: "))
    score = float(input("Exam score: "))
    students.append(student); hours.append(study); scores.append(score)

plt.figure()
plt.hist(scores, bins=5, edgecolor="black")
plt.title("Distribution of Examination Scores")
plt.xlabel("Exam score"); plt.ylabel("Number of students"); plt.tight_layout()

plt.figure()
plt.scatter(hours, scores)
for i, student in enumerate(students):
    plt.annotate(student, (hours[i], scores[i]))
plt.title("Study Hours vs Examination Scores")
plt.xlabel("Study hours per week"); plt.ylabel("Exam score")
plt.grid(True); plt.tight_layout()
plt.show()