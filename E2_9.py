# Escribe un programa que pide la edad por teclado y nos muestra el mensaje de "eres mayor de edad" o el mensaje
# de "eres menor de edad".

edad = int(input("Ingrese su edad: "))

mayor = edad >= 18
if mayor:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
