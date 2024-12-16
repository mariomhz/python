max = float('-inf')
min = float('inf')
counter = 0
while counter < 5:
    num = int(input(f"\nenter the number {counter + 1}: "))
    if num > max:
        max = num
    if num < min:
        min = num
    counter += 1
print(f"the biggest number is: {max}")
print(f"the smallest number is: {min}")
