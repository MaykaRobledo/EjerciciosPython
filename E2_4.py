# Escribe un programa que lea dos números, calcule y muestre el valor de sus suma, resta, producto y división.

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

suma = num1 + num2
resta = num1 - num2

print("La suma de los 2 numeros es:", suma)
print("La resta de los 2 numeros es:", resta)
print("El producto de los 2 numeros es:", num1 * num2)
print("La división de los 2 es:", num1 / num2)  # da ZeroDivisionError si num2 es 0
