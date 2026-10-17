num = int(input("Ingrese un numero: "))
i = 1

# OJO: igual que en el Java original, si num >= 0 este bucle no termina nunca,
# porque i baja (1, 0, -1, ...) y siempre sigue siendo <= num. Se detiene con Ctrl + C.
while True:
    print(i)
    i -= 1
    if not (i <= num):
        break
