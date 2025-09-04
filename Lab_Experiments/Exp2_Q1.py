n = int(input("Enter number of students: "))
students = {}

for _ in range(n):
    parts = input("Enter name and 3 marks: ").split()
    name = parts[0]
    marks = list(map(float, parts[1:]))
    students[name] = marks

q1 = input("Enter student name to get average: ")

if q1 in students:
    average = sum(students[q1]) / len(students[q1])
    print(f"{average:.2f}")
else:
    print("Student not found.")
