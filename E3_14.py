# Exija una contraseña (con repetir hasta que).

print("Ingrese la contraseña: ")
# Python no tiene do-while: se usa "while True" y un break al final
while True:
    print("Contraseña incorrecta, vuelva a intentarlo")
    contra = input()
    if contra == "1234":
        break

print("Contraseña correcta")
