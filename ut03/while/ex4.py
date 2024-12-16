start = int(input("introduce un numero menor que 100: "))
while start <= 100: #empiezo el while determinando que el numero sea menor de 100
    if start % 2 != 0: #si el numero es impar
        print(start, end=" ") #lo imprimo
    start += 1 #incremento de uno el numero inicial
print("\n")