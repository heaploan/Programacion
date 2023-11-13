casos = int(input())  # Número de casos
for i in range(casos):
    cartas = int(input())  # Número total de cartas
    piso = 0  # Inicializa el número de pisos
    cartasUsadas = 0  # Inicializa el número de cartas utilizadas
    menos = 0  # Inicializa la variable menos
    cartasTotales = cartas  # Almacena el número total de cartas para su posterior referencia
    # Bucle para calcular el número de pisos necesarios
    while cartas > 0:
        piso += 1  # Incrementa el número de pisos
        cartasUsadas += piso * 2 + piso - 1  # Calcula el número de cartas utilizadas en el piso actual
        menos = piso * 2 + piso - 1  # Almacena el valor de cartas utilizadas en el piso actual
        cartas -= menos  # Resta las cartas utilizadas en el piso actual al total
    # Verifica si el número total de cartas es igual al número de cartas utilizadas
    if cartasTotales == cartasUsadas:
        print(piso, cartasTotales - cartasUsadas)
    else:
        # Ajusta el resultado si el total de cartas no coincide con las cartas utilizadas
        cartasUsadas -= piso * 2 + piso - 1
        piso -= 1
        print(piso, cartasTotales - cartasUsadas)