import math

# Escribe un programa que calcule el área de un cuadrado cuyo lado se introduce por teclado.

lado = float(input("Ingrese el lado: "))
base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))
radio = float(input("Ingrese el radio: "))
PI1 = math.pi

print("Area cuadrado:", lado * lado)
print("Area rectangulo:", base * altura)
print("Area circulo:", PI1 * radio * radio)
