# Pedimos al usuario que ingrese la cantidad de casos
casos = int(input())
# Pedimos al usuario que ingrese los números separados por espacios y los almacenamos en una lista
numeros = input().split()
# Iteramos a través de cada valor en la lista de números
for valor in numeros:
    # Convertimos cada valor a punto flotante (float)
    valorFloat = float(valor) * 100
    # Calculamos el porcentaje multiplicando el valor por 100
    # Imprimimos el porcentaje con un solo decimal y seguido de un espacio en la misma línea
    print(f"{valorFloat:.1f}%", end=" ")
