import re

# En Python no hace falta declarar el tipo de las variables.
# Los comentarios que explican los tipos de Java se mantienen como referencia.

variable1 = 6  # int
print(f"HOLA MUNDO  {variable1}") #HAY 2 FORMAS DE IMPRIMIR
print("HOLA MUNDO", variable1)

variable2 = 120  # byte en Java; en Python todos los enteros son int
print(f"HOLA MUNDO  {variable2}")

variable3 = 5282  # short en Java
print(f"HOLA MUNDO  {variable3}")

variable4 = 678  # long en Java
print(f"HOLA MUNDO  {variable4}")

# En Python no hace falta poner la "f" de float, todos los decimales son float (64 bits)
variable5 = 354.8
print(f"HOLA MUNDO  {variable5}")

variable6 = 972.25  # double en Java
print(f"HOLA MUNDO  {variable6}")

variable7 = '%'  # char en Java; en Python es un str de longitud 1
print(f"HOLA MUNDO  {variable7}")

variable8 = False
print(f"HOLA MUNDO  {variable8}")

st = "hola mundo"
print(st)

x = 1
print(x)

y = 2
print(y)

z = 3
print(z)

a = 4
print(a)

b = 5
print(b)

st1 = "hola mundo"

print(len(st1))

print("hola"[0])
print("hola"[1])
print("hola"[2])
print("hola"[3])

print("Hola a todos"[2:])
print("Hola a todos"[5:])
print("Hola a todos"[4:10])

dias = "Lunes, Martes, Miércoles, Jueves, Viernes, Sábado, Domingo"
dias_array = dias.split(",")
# Según lo que pongas entre comillas es lo que se elimina
print("--Ejemplo 1--")
for dia in dias_array:
    print(dia)

correos = "test1@dominio.com, test2@dominio.com, test3@dominio.net"
reg_ex = r"@[A-Za-z0-9]+\.com"
print("--Ejemplo 3--")
for correo_sin_dominio in re.split(reg_ex, correos):
    print(correo_sin_dominio)

print("MENÚ:\n\top1:1\n\top2:2")
# Secuencias de escape:
# \n -----> Nueva Linea
# \t -----> Tabulador
# \r -----> Retroceso de Carro
# \f -----> Comienzo de Pagina
# \b -----> Borrado a la Izquierda
# \\ -----> El carácter barra inversa ( \ ).
# \' -----> El carácter comilla simple ( ' )
# \" -----> El carácter comilla doble ( " ).

# OPERADORES
# && -> and, || -> or, ! -> not

print("Dato:", (5 > 4) and (5 <= 4))
print("Dato:", (5 > 4) or (4 <= 5))
print("Dato:", (5 > 4) or not (5 <= 4))

# En Python una asignación no es una expresión; con := (operador morsa) sí se puede
print("Dato:", (x := 5))
print("Dato:", x == 5)
