# Escribe un programa que pide la edad por teclado y nos muestra el mensaje de "Eres mayor de edad" solo si lo
# somos.

edad = int(input("Ingrese su edad: "))

mayor = edad >= 18
if mayor:
    print("Es mayor de edad")
