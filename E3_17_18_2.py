# Petición de datos
num = int(input("Ingrese el numero hasta el que irá la cuenta: "))

# Lógica
if num >= 0:
    for i in range(num, -1, -1):  # de num hasta 0, bajando de 1 en 1
        print(str(i) + " ")
else:
    for i in range(0, num + 1):  # con num negativo el rango queda vacío (igual que en Java)
        print(str(i) + " ")
