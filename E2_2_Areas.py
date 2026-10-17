import math

# Escribe un programa que calcule el área de un cuadrado cuyo lado se introduce por teclado

# Calcular areas de cuadrado, rectangulo y circulo
x = 5
print("Area cuadrado:", x * x)

pi = 3.1416
print("Area círculo:", pi * x * x)

y = 8
print("Area rectángulo:", x * y)

# Calcular areas con datos ingresados por el usuario
lado = int(input("Ingrese el lado: "))
base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))
radio = int(input("Ingrese el radio: "))
PI1 = math.pi  # constante (por convención, en mayúsculas)

print("Area cuadrado:", lado * lado)
print("Area rectangulo:", base * altura)
print("Area circulo:", PI1 * radio * radio)

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ahora dime su edad: ")
print(f"Hola {nombre} {apellido}, tienes {edad} años")
