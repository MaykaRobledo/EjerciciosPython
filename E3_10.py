# Solicite un número en segundos y muestre por pantalla dicha cantidad de tiempo en
# horas, minutos y segundos.

seg = int(input("Ingrese la cantidad de segundos que desee para pasarlos a horas, minutos y segundos: "))

# En Python "/" siempre da decimal; para la división entera de Java se usa "//"
horas = seg // 3600
minutos = seg % 3600 // 60
seg2 = seg % 60

print(f"{horas}:{minutos}:{seg2}")
