num1 = float(input("\nintroduce el dividendo: "))
num2 = float(input("introduce el divisor: "))
if num2 != 0:
    division = num1 / num2
    print(f"la división es: {division:.2f}")
else:
    print("error: No se puede dividir entre cero.")