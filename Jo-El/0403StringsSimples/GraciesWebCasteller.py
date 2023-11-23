# Pedimos al usuario que ingrese el número de casos
casos = int(input())
# Iteramos a través de cada caso
for i in range(casos):
    # Pedimos al usuario que ingrese las dos palabras para el caso actual
    palabra1, palabra2 = input(), input()
    # Comparamos las longitudes de las dos palabras
    if len(palabra1) > len(palabra2):
        maxLongitud, minLongitud = len(palabra1), len(palabra2)
    else:
        maxLongitud, minLongitud = len(palabra2), len(palabra1)
    # Inicializamos un contador para contar cuántos caracteres coinciden en la misma posición en ambas palabras
    contador = 0
    # Iteramos a través de los caracteres de ambas palabras hasta la longitud de la palabra más corta
    for j in range(minLongitud):
        # Comparamos los caracteres en la misma posición
        if palabra1[j] == palabra2[j]:
            # Incrementamos el contador si los caracteres son iguales
            contador += 1
    # Comparamos el contador con la mitad de la longitud de la palabra más larga
    if maxLongitud / 2 <= contador:
        # Si la condición es verdadera, imprimimos "GRACIES WEBCASTELLER"
        print("GRACIES WEBCASTELLER")
    else:
        # Si la condición es falsa, imprimimos "WEBCASTELLER ESTA TRAVIESO HOY"
        print("WEBCASTELLER ESTA TRAVIESO HOY")
