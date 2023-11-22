# Se lee el número de casos que se van a evaluar
casos = int(input())
# Se itera sobre cada caso
for i in range(casos):
    # Se lee una línea que contiene el número de opciones seguido de los valores de esas opciones
    nums = input().split()   
    # Se obtiene el número de opciones
    opciones = int(nums[0])  
    # Se inicializan variables para la opción ganadora y el índice máximo
    opcionGanadora = 0
    indiceMax = 0 
    # Se itera sobre los valores de las opciones
    for j in range(1, opciones + 1):
        # Se obtiene el valor actual
        actual = int(nums[j])   
        # Se verifica si el valor actual es mayor que el índice máximo
        if actual > indiceMax:
            # Si es mayor, se actualiza la opción ganadora y el índice máximo
            opcionGanadora = j
            indiceMax = actual 
    # Se imprime la opción ganadora para este caso
    print(opcionGanadora)