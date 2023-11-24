# Leer el número de casos
casos = int(input())
# Iterar a través de cada caso
for i in range(casos):
    # Leer el número de líneas para el caso actual
    numeroLineas = int(input())
    # Inicializar un diccionario vacío para almacenar pares país-capital
    diccionario = {}
    # Leer las líneas y construir el diccionario
    for j in range(numeroLineas - 1):
        # Leer la entrada para un par país-capital y dividirla en una lista
        entrada = input().split("-")
        # Extraer el país y la capital de la entrada
        pais = entrada[0]
        capital = entrada[1]
        # Almacenar el par país-capital en el diccionario
        diccionario[pais] = capital
    # Leer la capital buscada
    capitalBuscada = input()
    # Imprimir el contenido del diccionario en formato {key1=value1, key2=value2, ...}
    print("{", end="")
    first_item = True
    for key, value in sorted(diccionario.items()):
        if not first_item:
            print(", ", end="")
        print(f"{key}={value}", end="")
        first_item = False
    print("}")
    # Imprimir el país correspondiente a la capital buscada
    for key, value in diccionario.items():
        if value == capitalBuscada:
            print(key)