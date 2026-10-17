# Pregunte qué día de la semana es hoy, y diga qué día será mañana.

dia = int(input("Ingrese el dia de la semana en numeros (1 = lunes; 2 = martes; 3 = miercoles; 4 = jueves; 5 = viernes; 6 = sabado; 7 = domingo: "))

if dia == 1:
    print("Hoy es lunes")
elif dia == 2:
    print("Hoy es martes")
elif dia == 3:
    print("Hoy es miercoles")
elif dia == 4:
    print("Hoy es jueves")
elif dia == 5:
    print("Hoy es viernes")
elif dia == 6:
    print("Hoy es sabado")
elif dia == 7:
    print("Hoy es domingo")
else:
    print("No es un numero correcto")

# El switch de Java se traduce con match/case (Python 3.10 o superior).
# No hace falta "break": cada case se ejecuta solo y termina.
match dia:
    case 1:
        print("Mañana es martes")
    case 2:
        print("Mañana es miercoles")
    case 3:
        print("Mañana es jueves")
    case 4:
        print("Mañana es viernes")
    case 5:
        print("Mañana es sabado")
    case 6:
        print("Mañana es domingo")
    case 7:
        print("Mañana es lunes")
    # case _: print("No es un numero correcto")   # equivale al default
