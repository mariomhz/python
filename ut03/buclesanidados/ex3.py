num = int(input("enter a number: "))
if num > 1:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"the number {num} is a prime number.")
    else:
        print(f"the number {num} is not a prime number.")
else:
    print("the number must be bigger than 1.")