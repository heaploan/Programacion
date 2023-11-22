# Definir las vocales y obtener el número de casos del usuario
vocales = "aeiou"
casos = int(input())
# Iterar a través de cada caso
for i in range(casos):
    # Inicializar contadores para cada vocal
    contadores = [0, 0, 0, 0, 0]
    # Obtener la frase del usuario
    frase = input()
    # Iterar a través de cada letra en la frase
    for letra in frase:
        # Verificar si la letra es una vocal
        if letra in vocales:
            # Obtener la posición de la vocal en el conjunto de vocales
            posicio = vocales.find(letra)        
            # Incrementar el contador correspondiente a la vocal encontrada
            contadores[posicio] += 1
    # Encontrar la vocal con la mayor frecuencia
    maximo = 0
    posicionMaxima = 0
    # Iterar a través de los contadores para encontrar la vocal ganadora
    for i in range(len(contadores)):
        if contadores[i] > maximo:
            maximo = contadores[i]
            posicionMaxima = i
    # Imprimir la vocal ganadora para la frase actual
    print("Vocal guanyadora:", vocales[posicionMaxima])
