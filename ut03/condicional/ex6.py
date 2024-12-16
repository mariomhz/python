nota = float(input("\nintroduce la nota del alumno/a: "))
if nota < 0 or nota > 10:
    print("Error: La nota debe estar entre 0 y 10.")
elif nota < 5:
    print("Suspenso")
elif nota < 7:
    print("Aprobado")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")