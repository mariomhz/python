boys = int(input("enter the amount of boys: "))
girls = int(input("enter the amount of girls: "))
total = boys + girls
if total > 0:
    print(f"boys percentage: {boys / total * 100:.2f}%")
    print(f"girls percentage: {girls / total * 100:.2f}%")
else:
    print("\nthere are no student enrolled in this course.")