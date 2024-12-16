# 10 numbers calculate arithmetic mean
numbers = []
for i in range(10):
    num = float(input(f"enter number {i + 1}: "))
    numbers.append(num)
mean = sum(numbers) /len(numbers)
print(f"the arithmetic mean is: {mean}")