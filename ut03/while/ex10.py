num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
if num1 > num2:
    num1, num2 = num2, num1
while num1 <= num2:
    print(num1, end= " ")
    num1 += 1
print("\n")