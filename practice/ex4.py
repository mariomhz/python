#Fibonacci sequence
def generate_fibonacci(n):
    x, y = 0, 1
    print("fibonacci sequence:")
    for a in range(n):
        print(x, end= " ")
        x, y = y, x + y
        
n = int(input("introducir un numero para la secuencia de fibonacci: "))
generate_fibonacci(n)