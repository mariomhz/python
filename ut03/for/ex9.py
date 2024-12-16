start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
if start <= end:
    for i in range(start, end + 1):
        print(i, end=" ")
    print()
else:
    print("counting not possible as the starting number is greater than the ending number.")