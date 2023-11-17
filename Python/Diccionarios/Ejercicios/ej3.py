# Inicializamos un diccionario vacío para representar la cesta de compras.
cesta = {}
# Solicitamos al usuario que introduzca el nombre del artículo o 'fin' para terminar.
article = input("Introduce el nombre del articulo o 'fin' para terminar: ")
# Inicializamos una variable para llevar un seguimiento del total de la compra.
total = 0

# Iniciamos un bucle while que continuará hasta que el usuario introduzca 'fin'.
while article != "fin":
    # Verificamos si el artículo ya está en la cesta.
    if article in cesta:
        print("Error: este articulo ya esta en la cesta. Introduce otro articulo o 'fin' para terminar.")
    else:
        # Si el artículo no está en la cesta, solicitamos al usuario que ingrese el precio.
        preu = float(input("Introduce el precio del articulo: "))        
        # Añadimos el artículo y su precio a la cesta.
        cesta[article] = preu        
        # Sumamos el precio al total de la compra.
        total += preu
    # Solicitamos al usuario que introduzca el nombre del próximo artículo o 'fin' para terminar.
    article = input("Introduce el nombre del articulo (o fin para terminar): ")

# Iteramos sobre los artículos en la cesta e imprimimos cada artículo y su precio.
for articulo in cesta:
    print(f"{articulo}: {cesta[articulo]:.2f}")
# Imprimimos el total de la compra.
print(f"Total: {total}")

