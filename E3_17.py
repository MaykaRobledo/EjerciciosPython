# Cuente de forma ascendente hasta un número dado.

num = int(input("Ingrese el numero hasta el que irá la cuenta: "))

for i in range(0, num + 1):  # range excluye el final, por eso num + 1
    print(i)
