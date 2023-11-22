# Lee el número de casos de prueba
n = int(input())
# Itera sobre cada caso de prueba
for j in range(n):
    # Lee el tamaño del array
    k = int(input())
    # Lee los números como cadenas y crea una lista
    numbers = input().split()
    # Inicializa la variable que indica si hay duplicados
    duplicate = False
    # Inicializa el índice para recorrer el array
    i = 0
    # Itera sobre el array hasta el penúltimo elemento
    while i < k - 1 and not duplicate:
        # Convierte los elementos a enteros y verifica si son iguales
        duplicate = int(numbers[i]) == int(numbers[i + 1])
        # Incrementa el índice
        i += 1
    # Imprime "SI" si se encontraron duplicados, "NO" en caso contrario
    if duplicate:
        print("SI")
    else:
        print("NO")