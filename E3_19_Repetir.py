# Calcule el factorial de un número dado mediante:
# Repetir hasta que.

n = int(input("Ingrese un numero para calcular su factorial: "))

fact = 1

while True:
    fact = fact * n
    if not (fact < n):
        break
print(f"La factorial del numero {n} es: {fact}")
