# Permita convertir temperaturas F en C y C en F según opción. La relación entre
# temperaturas Celsius y Fahrenheit viene dada por la fórmula C= 5/9 (F-32).

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32

print("El temperatura es:", fahrenheit)

fahrenheit2 = float(input("Ingrese la temperatura en grados Fahrenheit: "))
celsius2 = (fahrenheit2 - 32) * 5 / 9

print("El temperatura es:", celsius2)
