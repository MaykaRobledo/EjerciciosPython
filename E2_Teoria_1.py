num1 = 65.0  # double en Java
print("Dato 1:", int(num1))  # casting (int)

num2 = 41
print("Dato 2:", chr(num2))  # casting (char): en Python se usa chr()

num3 = 52.0
print("Dato 3:", int(num3))

num4 = True
print("Dato:", num4)

# Python no tiene los operadores ++ ni --, se usa += 1 y -= 1
num6 = 5
num6 += 1  # equivale a ++num6 (incrementa y luego se usa)
print("Dato:", num6)

num7 = 5
print("Dato:", num7)  # equivale a num7++ (se usa y luego se incrementa)
num7 += 1

num8 = 5
num8 += 1
print("Dato:", num8)

# Para restar es igual pero con "-= 1"

num9 = 5
num9 += 12
print("Dato:", num9)

num10 = 5
num10 %= 5
print("Dato:", num10)

num11 = 4
# x %= 3
print("Dato:", (not (num11 == 3)) or (not (num11 == 4)))

bandera = True
# Operador ternario: en Python es "valor_si_true if condicion else valor_si_false"
num12 = 4 if bandera else 5
if bandera:
    num12 = 4
else:
    num12 = 5
print("Dato:", num12)
