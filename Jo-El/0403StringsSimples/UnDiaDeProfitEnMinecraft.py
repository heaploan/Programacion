# Pedimos al usuario que ingrese el número de casos de prueba
casos = int(input())
# Iteramos a través de cada caso de prueba
for i in range(casos):
    # Para cada caso de prueba, obtenemos el número de corredores
    numeroCorredores = int(input())
    # Inicializamos un contador para el número total de diamantes en el caso actual
    contador = 0
    # Iteramos a través de cada corredor en el caso actual
    for j in range(numeroCorredores):
        # Obtener el camino del corredor actual, donde los diamantes pueden estar ocultos
        corredor = input()
        # Iteramos a través de cada posición en el camino del corredor
        for k in range(len(corredor) - 1):
            # Verificamos si hay un diamante entre la posición actual y la siguiente posición
            if corredor[k] == "{" and corredor[k + 1] == "}":
                # Si encontramos un diamante, incrementamos el contador
                contador += 1
    # Imprimimos el número total de diamantes encontrados en el caso actual
    print(contador)