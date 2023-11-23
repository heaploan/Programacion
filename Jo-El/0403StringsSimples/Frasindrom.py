# Se solicita al usuario que ingrese palabras, separadas por espacios, y se almacenan en una lista llamada 'palabras'.
palabras = input().split()
# Se inicia un bucle while que se ejecutará mientras la primera palabra ingresada no sea un punto ".".
while palabras[0] != ".":
    # 'v' almacena el índice del último elemento en la lista 'palabras'.
    v = len(palabras) - 1
    # 'c' se utiliza para contar las diferencias entre las palabras en la lista.
    c = 0
    # Se inicia un bucle for que recorre la lista 'palabras'.
    for i in range(len(palabras)):
        # Se compara la palabra en la posición 'v' con la palabra en la posición 'i'.
        if palabras[v] != palabras[i]:
            # Si las palabras son diferentes, se incrementa el contador 'c'.
            c += 1
        # Se decrementa 'v' para comparar la siguiente palabra en la siguiente iteración del bucle.
        v -= 1
    # Después de comparar todas las palabras, se evalúa si el contador 'c' es igual a cero.
    if c == 0:
        # Si no hay diferencias entre las palabras, se imprime "SI".
        print("SI")
    else:
        # Si hay al menos una diferencia, se imprime "NO".
        print("NO")
    # Se solicita al usuario que ingrese una nueva lista de palabras.
    palabras = input().split()
# Cuando el usuario ingresa un punto ".", el bucle while termina y el programa finaliza.
