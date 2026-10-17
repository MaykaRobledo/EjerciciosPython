# Se imprime un mensaje
# (en Java se usaba JOptionPane; aquí se usa print en la consola)
print("Hello World")

# Se continua en la terminal
num = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num > num2:
    print("El primer numero es mayor que el segundo numero")
elif num < num2:
    print("El segundo numero es mayor que el primer numero")
else:
    print("Los numeros son iguales")
