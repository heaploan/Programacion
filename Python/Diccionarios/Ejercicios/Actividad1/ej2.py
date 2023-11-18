# Se crea un diccionario llamado 'productos' con nombres de productos y sus respectivos precios.
productos = {}
productos["Refresc"] = 1.25
productos["Aperitiu"] = 0.90
productos["Pastisset"] = 1.05
productos["Galetes"] = 1.35
productos["Suc"] = 0.95

# Se solicita al usuario que ingrese un nombre de producto.
producto = input("Introduce un producto: ")
# Se solicita al usuario que ingrese una cantidad (se espera que sea un número entero).
cantidad = int(input("Introduce una cantidad: "))
# Se verifica si el producto ingresado está en el diccionario.
if producto in productos:
    # Si el producto está en el diccionario, se imprime el total de la compra.
    print(f"El total de la compra de {producto} es:", productos[producto] * cantidad)
else:
    # Si el producto no está en el diccionario, se muestra un mensaje de error.
    print("Error, el producto no está en el diccionario")
