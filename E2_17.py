# Escribe un programa que recibe como datos de entrada una hora expresada en horas, minutos y
# segundos que nos calcula y escribe la hora, minutos y segundos que serán, transcurrido un segundo.

hora = int(input("Ingrese la hora: "))
minutos = int(input("Ingrese los minutos: "))
segundos = int(input("Ingrese los segundos: "))

if segundos >= 59:
    segundos = 0
    minutos = minutos + 1
    if minutos >= 60:
        minutos = 0
        hora = hora + 1
        if hora >= 24:
            hora = 0
else:
    segundos = segundos + 1

print(f"La hora después de un segundo será: {hora}:{minutos}:{segundos}")
