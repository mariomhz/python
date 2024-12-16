max = float('-inf')
min = float('inf')
sum = 0
counter = 0

while True:
    num = int(input("enter a number (enter 0 to stop): "))
    if num == 0:
        break
    if num > max:
        max = num
    if num < min:
        min = num
    sum += num
    counter += 1

if counter > 0:
    average = sum / counter
    print(f"biggest number: {max}, smallest number: {min}, average: {average}")
else:
    print("no numbers were entered.\n")