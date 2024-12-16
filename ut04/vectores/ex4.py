numbers = []
while len(numbers) < 100:
    num = float(input("enter a number (0 to stop): "))
    if num == 0:
        break
    numbers.append(num)
print(f"The sum is: {sum(numbers)}")
print(f"The total number of entries: {len(numbers)}")