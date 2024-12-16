final = int(input("enter a number: "))
num = 1
counter = 0
while num <= final:
    if num % 3 == 0:
        print(num, end= " ")
        counter += 1
    num += 1
print(f"\nthe amount of multiples of 3 is: {counter}\n")