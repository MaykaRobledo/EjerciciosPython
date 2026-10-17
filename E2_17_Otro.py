# Escribe un programa que recibe como datos de entrada una hora expresada en horas, minutos y
# segundos que nos calcula y escribe la hora, minutos y segundos que serán, transcurrido un segundo.

# Interacción con el usuario
# (en Java se usaba JOptionPane; aquí se usa input() y print() en la consola)
time = input("Dime la hora en formato hh:mm:ss: ")

# Conversiones
hora = int(time[0:2])
min = int(time[3:5])
seg = int(time[6:8])

# Lógica
if seg >= 59:
    seg = 0
    min = min + 1
    if min >= 60:
        min = 0
        hora = hora + 1
        if hora >= 24:
            hora = 0
else:
    seg = seg + 1

print(f"La hora será: {hora}:{min}:{seg}")
