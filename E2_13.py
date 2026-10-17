# Escribe un programa que lee dos números y los visualiza en orden ascendente.

num = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num > num2:
    print(num, ",", num2)
else:
    print(num2, ",", num)
