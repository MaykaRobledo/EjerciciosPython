# Escribe un programa que lea tres números distintos y nos diga cuál es el mayor.

num = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

if num > num2 and num > num3:
    print("El primer numero es el mayor")
elif num2 > num and num2 > num3:
    print("El segundo numero es el mayor")
elif num3 > num and num3 > num2:
    print("El tercer numero es el mayor")
else:
    print("Los tres numeros son iguales")
