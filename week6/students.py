import csv

students = []

# with open("students.csv") as file:
#     for line in file:
#         name, language = line.rstrip().split(",")
#         student = {"name": name, "language": language}
#         students.append(student)

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "language": row["language"], "state": row["state"]})

# Lambda function = function that has no name
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is learning {student['language']} and is from {student['state']}")

# The above lambda is equivalent to:
# def get_name(student):
#     return student["name"]
# print("\nWithout Lambda:")
# for student in sorted(students, key=get_name, reverse=True):
#     print(f"{student['name']} is learning {student['language']}")