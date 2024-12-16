start = int(input("enter the starting number: "))
end = int(input("enter the ending number: "))
if start <= end:
    total_sum = sum(range(start, end + 1))
    print(f"the sum of integers from {start} to {end} is:", total_sum)
else:
    print("starting number must be smaller than ending number.")