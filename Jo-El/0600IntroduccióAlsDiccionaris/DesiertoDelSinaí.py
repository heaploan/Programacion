# Leer el número de casos
casos = int(input())
# Iterar a través de cada caso
for i in range(casos):
    # Leer el número de votos para el caso actual
    votos = int(input())
    # Inicializar un diccionario para contar los votos de cada mapa
    diccionario = {}
    # Inicializar variables para el ganador y la cantidad máxima de votos
    ganador = ""
    maxVotos = 0
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
            maxVotos = diccionario[mapa]
            ganador = mapa
    # Imprimir el nombre del mapa ganador para el caso actual
    print(ganador)