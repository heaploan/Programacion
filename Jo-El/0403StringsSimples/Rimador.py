# Pedimos al usuario que ingrese la cantidad de casos que desea evaluar
casos = int(input())
# Iteramos sobre el número de casos
for i in range(casos):
    # Para cada caso, solicitamos al usuario que ingrese dos frases separadas por una coma
    frases = input().split(",")
    # Almacenamos cada frase por separado
    frase1, frase2 = frases[0], frases[1]
    # Comparamos las longitudes de ambas frases y asignamos el tamaño mínimo a la variable 'tamaño'
    if len(frase1) > len(frase2):
        tamaño = len(frase2)
    else:
        tamaño = len(frase1)
    # Inicializamos una cadena vacía llamada 'rima' que se utilizará para almacenar la parte común al final de ambas frases
    rima = ""
    # Inicializamos un índice 'j' que se usará para recorrer las frases desde el final hacia el principio
    j = 0
    # Inicializamos una bandera 'seguir' que determinará si continuamos buscando la rima
    seguir = True
    # Iniciamos un bucle while que se ejecutará mientras 'seguir' sea True
    while seguir:
        # Comparamos los caracteres en la posición correspondiente desde el final de ambas frases
        if frase1[len(frase1) - j - 1] == frase2[len(frase2) - j - 1]:
            # Si los caracteres son iguales, los agregamos a la cadena 'rima'
            rima = frase1[len(frase1) - j - 1] + rima
        else:
            # Si encontramos caracteres diferentes, cambiamos la bandera 'seguir' a False para salir del bucle
            seguir = False
        # Incrementamos el índice 'j' para avanzar al siguiente par de caracteres
        j += 1
    # Después de salir del bucle, verificamos si hay alguna rima y la imprimimos, de lo contrario, imprimimos '#'
    if rima:
        print(rima)
    else:
        print("#")