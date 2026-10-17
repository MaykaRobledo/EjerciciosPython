# Escribe un programa que dado el precio de un artículo y el precio de venta real nos muestre el porcentaje de
# descuento realizado.

precio = float(input("Ingrese el precio de un articulo: "))
venta = float(input("Ingrese el precio de venta real: "))

descuento = ((precio - venta) / precio) * 100
print("El descuento es:", descuento)
