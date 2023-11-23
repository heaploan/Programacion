# Leemos el número de casos de prueba.
casos = int(input())
# Iteramos a través de cada caso de prueba
for i in range(casos):
    # Leemos el valor K que representa la longitud de la lista.
    k = int(input())
    # Leemos la lista de números como cadena y la convertimos en una lista de enteros. 
    nombres = input().split()
    # Leemos los valores p1 y p2
    numbers = input().split()
    p1 = int(numbers[0])
    p2 = int(numbers[1])
    # Iteramos sobre la lista de números y reemplazamos los valores p1 por p2
    for j in range(k):
        if int(nombres[j]) == p1:
            nombres[j] = p2
    # Imprimimos la lista modificada en una sola línea.
    print(*nombres)