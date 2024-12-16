number = int(input("enter an integer to find its divisors: "))
print("divisors of", number, ": ")
for i in range (1, number + 1):
    if number % i == 0:
        print(i)