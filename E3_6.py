# Compare dos valores de entrada A y B, y diga cuál es mayor.

num = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num > num2:
    print("El primer numero mayor que el segundo numero")
elif num < num2:
    print("El primer numero menor que el segundo numero")
else:
    print("Los numeros son iguales")
