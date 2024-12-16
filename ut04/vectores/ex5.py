numbers = []
for i in range(10):
    numbers.append(float(input(f"enter decimal number {i + 1}: ")))
mean = sum(numbers) / len(numbers)
print(f"numbers above the mean ({mean}): ")
for num in numbers:
    if num > mean:
        print(num)