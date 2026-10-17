# Calcule el promedio de notas de 3 alumnos.

nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))

suma = nota1 + nota2 + nota3
media = suma // 3  # división entera, como en Java (con "/" saldría con decimales)

print("La media es:", media)
