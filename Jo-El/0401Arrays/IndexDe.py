# Leemos el numero de casos de prueba.
casos = int(input())
# Iteramos a través de cada caso de prueba
for i in range(casos):
    # Leemos el valor de K que representa la longitud de la lista.
    k = int(input())
    # Leemos la lista de números como cadena y la convertimos en una lista de enteros. 
    numbers = input().split()
    # Leemos el valor del folio que estamos buscando.
    foli = int(input())
    # Inicializamos la posicion como -1, indicando que no se ha encontrado.
    posicio = -1
    # Iteramos sobre la lista para encontrar la posición del folio.
    for j in range(k):
        if int(numbers[j]) == foli and posicio == -1:
            posicio = j
        # Sumamos + 1 a j.    
        j += 1
    # Imprimimos la posición del folio (o -1 si no se encontró.).
    print(posicio)