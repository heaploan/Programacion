# Pedimos al usuario que ingrese el número de casos a evaluar
casos = int(input())
# Iteramos sobre cada caso
for i in range(casos):
    # Para cada caso, solicitamos la cantidad de números
    k = int(input())
    # Leemos los números como una cadena y los dividimos para obtener una lista de números
    numbers = input().split()
    # Pedimos el número a buscar
    m = int(input())
    # Inicializamos una bandera para verificar si el número buscado está presente
    encontrado = False
    # Iteramos sobre cada número en la lista
    for j in range(k):
        # Convertimos el número de cadena a entero
        talla = int(numbers[j])   
        # Verificamos si el número actual es igual a m, m-1 o m+1
        if talla == m or talla == m - 1 or talla == m + 1:
            # Si encontramos un número que cumple la condición, actualizamos la bandera
            encontrado = True
    # Verificamos si hemos encontrado un número que cumple la condición
    if encontrado:
        # Si sí, imprimimos "SI"
        print("SI")
    else:
        # Si no, imprimimos "NO"
        print("NO")
