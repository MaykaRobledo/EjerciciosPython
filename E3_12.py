import math

# Pregunte una nota y la convierta en calificación habitual (suspenso, aprobado,
# notable, sobresaliente).

nota = float(input("Ingrese una nota: "))

# Math.round de Java redondea .5 hacia arriba. El round() de Python redondea .5 al par
# más cercano (round(2.5) = 2), por eso se usa floor(nota + 0.5) para mantener el mismo resultado.
match math.floor(nota + 0.5):
    case 1 | 2 | 3 | 4:  # los case apilados de Java se agrupan con "|"
        print("Insuficiente")
    case 5:
        print("Suficiente")
    case 6:
        print("Bien")
    case 7:
        print("Notable")
    case 8:
        print("Notable")
    case 9:
        print("Sobresaliente")
    case 10:
        print("Sobresaliente")
    case _:  # default
        print("No es una nota validda.")
