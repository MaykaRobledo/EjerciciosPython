# Escribe un programa que lee dos números, calcula y muestra el valor de su suma, resta, producto y división. (Ten
# en cuenta la división por cero).

num = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

print("Suma:", num + num2)
print("Resta:", num - num2)
print("Multiplicacion:", num * num2)
if num2 == 0:
    print("No se puede dividir por 0")
else:
    print("Division:", num / num2)
