import plotly.express as px
import pandas as pd

students, marks = [], []
n = int(input("Number of students: "))
for i in range(n):
    students.append(input(f"Student {i+1} name/ID: ").strip())
    marks.append(float(input("Mathematics marks: ")))
df = pd.DataFrame({"Student": students, "Mathematics": marks})
fig = px.bar(df, x="Student", y="Mathematics",
             title="Mathematics Marks by Student",
             labels={"Mathematics": "Marks"})
fig.show()
