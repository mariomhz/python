start = int(input("enter a number smaller than 100: "))
sum_odds = 0
counter = 0
while start <= 100:
    if start % 2 != 0:
        print(start, end=" ")
        sum_odds += start
        counter += 1
    start += 1
print(f"\nsum of odd numbers is: {sum_odds}")
print(f"amount of odd numbers is {counter}\n")