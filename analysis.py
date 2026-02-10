import pandas as pd

df = pd.read_csv("student_data.csv")

print("student data:")
print(df)

avg = df["marks"].mean()
print("\nAverage Marks:",avg)

top_students = df[df["marks"] > 80]
print("\nTop Students:")
print("top_students")

top_students.to_csv("top_students.csv",index=False)
print("\nFile saved: top_students.csv")