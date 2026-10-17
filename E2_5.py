import math

# Escribe un programa que toma como dato de entrada un número que corresponde a la longitud de un radio y nos
# escribe la longitud de la circunferencia, el área del círculo y el volumen de la esfera que corresponden con dicho
# radio.

radio = float(input("Ingrese el radio: "))
PI = math.pi

print("Perímetro de la circunferencia:", 2 * PI * radio)
print("Área del círculo:", PI * radio * radio)
# En Python 4/3 es división decimal (1.333...), no entera como en Java
print("Volumen de la esfera:", 4 / 3 * PI * radio * radio * radio)
