bandera = True

# En Java cada bloque tiene su propio ámbito, por eso se podía declarar "int x"
# dos veces. En Python los bloques if NO crean un ámbito nuevo: x es la misma
# variable y la segunda asignación simplemente sustituye a la primera.
if True:
    x = 4

if True:
    x = 5

print("Dato: ")
