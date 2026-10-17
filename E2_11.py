# Escribe un programa que lee 2 números y muestra el mayor.

num = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num > num2:
    print(f"El primer numero ({num}) es mayor que el segundo numero ({num2}).")
else:
    print(f"El segundo numero ({num2}) es mayor que el primer numero ({num}).")
