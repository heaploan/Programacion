# Lee el número de casos de prueba
n = int(input())
# Itera sobre cada caso de prueba
for i in range(n):
    # Lee el tamaño del array para el caso actual
    k = int(input())
    # Lee los números como cadenas y crea una lista
    numbers = input().split()
    # Inicializa la variable que indica si hay duplicados
    duplicate = False
    # Itera sobre la lista de números (como cadenas)
    for j in range((len(numbers)) - 1):
        # Compara si el número actual es igual al siguiente después de convertirlos a enteros
        if int(numbers[j]) == int(numbers[j + 1]):
            duplicate = True
    # Imprime "SI" si se encontraron duplicados, "NO" en caso contrario
    if duplicate:
        print("SI")
    else:
        print("NO")