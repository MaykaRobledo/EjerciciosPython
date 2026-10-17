num = int(input("Ingrese un numero: "))
i = 1

# do-while: el cuerpo se ejecuta al menos una vez y la condición se comprueba al final
while True:
    print(i)
    i += 1
    if not (i <= num):
        break
