students = []
grades = []
for _ in range(10):
    name = input("enter the student's name: ")
    grade = float(input(f"enter {name}'s grade: "))
    students.append(name)
    grades.append(grade)
mean = sum(grades) / len(grades)
print(f"the average grade is: {mean}.")
print("students with grades below the average:")
for i in range(len(grades)):
    if grades[i] < mean:
        print(f"{students[i]}: {grades[i]}")