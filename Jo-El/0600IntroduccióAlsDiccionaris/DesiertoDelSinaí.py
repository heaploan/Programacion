# Leer el número de casos
casos = int(input())
# Iterar a través de cada caso
for i in range(casos):
    # Leer el número de votos para el caso actual
    # Inicializar un diccionario para contar los votos de cada mapa
    # Inicializar variables para el ganador y la cantidad máxima de votos
    votos, diccionario, ganador, maxVotos = int(input()), {}, "", 0
    # Iterar a través de cada voto
    for j in range(votos):
        # Leer el nombre del mapa para el voto actual
        mapa = input()
        # Contar el voto para el mapa actual en el diccionario
        if mapa in diccionario:
            diccionario[mapa] += 1
        else:
            diccionario[mapa] = 1
        # Actualizar el ganador y la cantidad máxima de votos si es necesario
        if diccionario[mapa] > maxVotos:
            maxVotos, ganador = diccionario[mapa], mapa
    # Imprimir el nombre del mapa ganador para el caso actual
    print(ganador)