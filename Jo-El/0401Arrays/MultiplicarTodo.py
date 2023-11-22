# Solicita al usuario ingresar la cantidad de casos de prueba
casos = int(input())
# Itera a través de cada caso de prueba
for i in range(casos):
    # Solicita al usuario ingresar la cantidad de números en la lista para el caso actual (k)
    k = int(input())
    # Lee la lista de números como una cadena y la divide en una lista de cadenas, utilizando espacios como separadores
    numbers = input().split(" ")
    # Solicita al usuario ingresar el valor por el cual multiplicar cada número en la lista (p)
    p = int(input())  
    # Itera a través de cada número en la lista
    for num in numbers:
        # Multiplica el número (convertido a entero) por el valor p y lo imprime, seguido de un espacio en la misma línea
        print(int(num) * p, end=" ")
    # Después de imprimir todos los resultados para un caso, agrega un salto de línea para pasar al siguiente caso
    print()