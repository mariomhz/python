try:
    num1 = float(input("enter the first number: "))
    operator = input("enter the operator(+, -, *, /): ")
    num2 = float(input("enter the second number: "))
    operators = ["+", "-", "*", "x", "/"]
    
    if operator not in operators:
        raise ValueError("invalid operator!")
    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = num1 / num2
        
    print("result: ", result)

except ValueError as ve:
    print("input error:", ve)
    
except ZeroDivisionError as zde:
    print("math error:", zde)