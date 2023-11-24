# Leer el número de casos
casos = int(input())
# Iterar a través de cada caso
for i in range(casos):
    # Leer el número de líneas para el caso actual
    numeroLineas = int(input())
    # Inicializar un diccionario vacío para almacenar pares país-capital
    diccionario = {}
    # Iterar a través de cada línea del caso, excepto la última
    for j in range(numeroLineas - 1):
        # Leer la entrada para un par país-capital, separarla en una lista
        entrada = input().split("-")
        # Extraer país y capital de la entrada
        pais = entrada[0]
        capital = entrada[1]
        # Almacenar el par país-capital en el diccionario
        diccionario[pais] = capital
    # Leer la última línea del caso (el país para el cual queremos encontrar la capital)
    capitalBuscada = input()
    # Verificar si el país está en el diccionario
    if capitalBuscada in diccionario:
        # Imprimir la capital correspondiente si se encuentra
        print(diccionario[capitalBuscada])
    else:
        # Imprimir "NO HO SE" si el país no se encuentra
        print("NO HO SE")