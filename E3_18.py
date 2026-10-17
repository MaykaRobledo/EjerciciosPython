# Cuente de forma descendente hasta cero desde un número dado.

num = int(input("Ingrese el numero hasta el que irá la cuenta atrás: "))

for i in range(num, 0, -1):  # de num hasta 1, bajando de 1 en 1
    print(i)
