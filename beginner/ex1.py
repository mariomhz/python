#calculator
print("Welcome to the Calculator!")
num1 = float(input("enter the first number: "))
operator = input("enter an operator (+, -, *, /): ")
num2 = float(input("enter the second number: "))
if operator == "+": result = num1 + num2
elif operator == "-": result = num1 - num2
elif operator == "*": result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("error, cannot divide by zero.")
    else: result = num1 / num2
print("result: ", result)