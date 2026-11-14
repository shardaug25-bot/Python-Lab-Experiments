import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

n = int(input("Number of students: "))
records = []
subjects = ["Mathematics", "Physics", "Chemistry", "English"]
for i in range(n):
    name = input(f"Student {i+1} name/ID: ").strip()
    row = {"Student": name}
    for subject in subjects:
        row[subject] = float(input(f"{subject} marks: "))
    records.append(row)

df = pd.DataFrame(records)
for subject in subjects:
    sns.histplot(data=df, x=subject, kde=True)
    plt.title(f"{subject} Score Distribution")
    plt.show()
sns.pairplot(df[subjects])
plt.show()
sns.heatmap(df[subjects].corr(), annot=True, vmin=-1, vmax=1)
plt.title("Correlation Heatmap of Subject Scores")
plt.tight_layout()
plt.show()