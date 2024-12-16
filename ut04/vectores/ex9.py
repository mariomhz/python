#request 10 numbers and display them in ascending order
numbers = []
for i in range (10):
    numbers.append(int(input(f"enter number {i + 1}: ")))
numbers.sort()
print(f"numbers in ascending order: {numbers}")