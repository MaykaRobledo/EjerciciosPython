# Escribe un programa que lea una calificación numérica entre 0 y 10 y la transforma en calificación alfabética,
# escribiendo el resultado.
#     de 0 a <3 Muy Deficiente.
#     de 3 a <5 Insuficiente.
#     de 5 a <6 Bien.
#     de 6 a <9 Notable
#     de 9 a 10 Sobresaliente

nota = float(input("Ingrese una nota: "))

if 0 <= nota <= 3:
    print("Muy deficiente")
elif 3 < nota <= 5:
    print("Insuficiente")
elif 5 < nota <= 6:
    print("Bien")
elif 6 < nota <= 9:
    print("Notable")
elif 9 < nota <= 10:
    print("Notable")
else:
    print("Has ingresado un numero no valido, por favor ingrese un numero válido (0 -10)")
