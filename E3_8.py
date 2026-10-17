# Lea dos números y los escriba en orden ascendente.

num = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num > num2:
    print("Orden:", num, ",", num2)
elif num < num2:
    print("Orden:", num2, ",", num)
else:
    print("Los numeros son iguales ")
