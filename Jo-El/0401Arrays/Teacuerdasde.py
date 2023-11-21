# Se ingresa el número de iteraciones
entry = int(input())
# Itera 'entry' veces
for i in range(entry):
    # Se ingresa la longitud de la lista
    k = int(input())
    # Se ingresa una lista de números separados por espacios y se divide en una lista de cadenas
    numbers = input().split()
    # Se ingresa la posición deseada en la lista
    position = int(input())
    # Verifica si la posición está dentro del rango válido (de 0 a k-1)
    if 0 <= position < k:
        # Obtiene el número en la posición especificada en la lista y lo convierte a un entero
        result = int(numbers[position])

        # Imprime el resultado
        print(result)