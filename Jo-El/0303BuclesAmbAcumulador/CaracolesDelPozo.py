# Obtener el número de casos de prueba
entry = int(input())
# Iterar a través de cada caso de prueba
for i in range(entry):
    # Obtener los datos de entrada para cada caso y dividirlos en una lista
    data = input().split()
    # Extraer valores de la lista y convertirlos a enteros
    profundidad = int(data[0])  # profundidad del pozo
    subida = int(data[1])       # distancia que se sube por día
    bajada = int(data[2])       # distancia que se baja por noche
    metrosSubidos = 0  # variable para llevar el seguimiento de la distancia subida
    dias = 0           # variable para llevar el seguimiento del número de días
    # Verificar si es imposible salir del pozo
    # Esta condición cubre casos donde la distancia de subida es menor que la de bajada
    # o las distancias de subida y bajada son iguales, pero el pozo es más profundo que la distancia de subida
    if subida < bajada or (subida == bajada and profundidad > subida):
        print("NO")
    else:
        # Bucle hasta que el escalador alcance o supere la profundidad del pozo
        while metrosSubidos < profundidad:
            dias += 1  # incrementar el número de días
            metrosSubidos += subida  # subir durante el día
            # Verificar si el escalador ha alcanzado la profundidad, si no, bajar durante la noche
            if metrosSubidos < profundidad:
                metrosSubidos -= bajada
        # Verificar si el escalador bajó demasiado después de alcanzar la profundidad
        # Si es así, es imposible salir, así que imprimir "NO"
        if metrosSubidos < 0:
            print("NO")
        else:
            # Si el escalador logró salir, imprimir el número de días que tomó
            print(dias)
