#display 10 numbers after asking for them
numbers = []
while len(numbers) < 10:
    num = int(input("enter a number (must be distinct): "))
    if num not in numbers:
        numbers.append(num)
    else:
        print("number already entered, try again.")
print("the numbers are:", " ".join(map(str, numbers)))