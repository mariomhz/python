total = int(input("\nintroduce numero de segundos: "))
horas = total // 3600
minutos = (total % 3600) // 60
segundos = total % 60
print(f"{total} segundos son {horas} horas, {minutos} minutos y {segundos} segundos")
print()