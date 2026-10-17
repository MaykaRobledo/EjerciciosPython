# Escribe un programa que calcula el salario neto semanal de un trabajador en función del número de
# horas trabajadas y la tasa de impuestos de acuerdo a las siguientes hipótesis:
#     Las primeras 35 horas se pagan a tarifa normal.
#     Las horas que pasen de 35 se pagan a 1,5 veces la tarifa normal.
#     Las tasas de impuestos son:
#     Los primeros 500 euros son libres de impuestos.
#     Los siguientes 400 tienen un 25% de impuestos.
#     Los restantes un 45% de impuestos.
#     Escribir nombre, salario bruto, tasas y salario neto.

# Interacción con el usuario
nombre = input("Ingrese el nombre del trabajador: ")
horas = int(input("Horas trabajadas esta semana: "))
tarifa = float(input("Ingrese la tarifa por horas: "))

# Cálculos
if horas <= 35:
    salario_bruto = horas * tarifa
else:
    salario_bruto = (35 * tarifa) + (horas - 35) * tarifa * 1.5

if salario_bruto <= 500:
    impuestos = 0
elif salario_bruto <= 900:
    impuestos = (salario_bruto - 500) * 0.25
else:
    impuestos = (400 * 0.25) + (salario_bruto - 900) * 0.45

salario = salario_bruto - impuestos

# Imprimimos los resultados
print("Nombre del trabajador:", nombre)
print("Salario bruto:", salario_bruto)
print("Impuestos:", impuestos)
print("Salario neto:", salario)
