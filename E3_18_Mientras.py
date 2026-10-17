# Bucle infinito: se detiene con Ctrl + C
while True:
    num = int(input("Ingrese el numero hasta el que irá la cuenta atrás: "))

    for i in range(num, 0, -1):
        print(i)
