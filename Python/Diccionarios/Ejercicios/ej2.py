productos = {}
productos["Refresc"] = 1.25
productos["Aperitiu"] = 0.90
productos["Pastisset"] = 1.05
productos["Galetes"] = 1.35
productos["Suc"] = 0.95
producto = input("Introduce un producto: ")
cantidad = int(input("Introduce una cantidad: "))
if producto in productos:
    print(f"El total de la compra de {producto} es:", productos[producto] * cantidad)
else:
    print("Error, el producto no esta en el diccionario")