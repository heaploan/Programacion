# Solicita la cantidad de casos de prueba
casos = int(input())
# Itera a través de cada caso de prueba
for i in range(casos):
    # Para cada caso, solicita la cantidad de números en la lista (k)
    k = int(input())
    # Lee la lista de números como una cadena y la divide en una lista de cadenas
    numbers = input().split()
    # Solicita el valor por el cual multiplicar cada número en la lista (p)
    p = int(input())
    # Itera a través de cada número en la lista
    for num in numbers:
        # Multiplica el número por el valor p y almacena el resultado en 'resultado'
        resultado = int(num) * p
        # Imprime el resultado, seguido de un espacio en la misma línea
        print(resultado, end=" ")
    # Después de imprimir todos los resultados para un caso, agrega un salto de línea
    print()