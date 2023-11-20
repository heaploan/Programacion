# Solicita al usuario que ingrese el número de casos
casos = int(input())
# Itera a través de cada caso
for i in range(casos):
    # Lee las dimensiones para el caso actual y las almacena en la lista 'dimensions'
    dimensions = input().split()   
    # Convierte las dimensiones a enteros y las almacena en las variables 'files' y 'columnes'
    files = int(dimensions[0])
    columnes = int(dimensions[1])
    # Determina la dimensión mínima entre 'files' y 'columnes'
    if files < columnes:
        dimMin = files
    else:
        dimMin = columnes
    # Inicializa la variable 'quadrats' en 0
    quadrats = 0
    # Itera a través de las dimensiones, calculando cuadrados y actualizando 'quadrats'
    for j in range(1, dimMin + 1):
        quadrats += (files - j + 1) * (columnes - j + 1)
    # Imprime el resultado para el caso actual
    print(quadrats)
