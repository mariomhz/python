numbers = []
for i in range(10):
    numbers.append(int(input(f"enter number {i + 1}: ")))
target = int(input("enter a number to search for: "))
if target in numbers:
    print(f"the number {target} was found in position {numbers.index(target) + 1}.")
else:
    print(f"the number {target} is not in the list.")