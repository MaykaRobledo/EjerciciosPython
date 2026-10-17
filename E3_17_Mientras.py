# Bucle infinito: se detiene con Ctrl + C
while True:
    num = int(input("Ingrese un numero: "))
    for i in range(0, num + 1):
        print(i)
