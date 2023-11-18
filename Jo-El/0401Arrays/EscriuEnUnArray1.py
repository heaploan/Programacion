# Solicitamos al usuario que ingrese un número entero K que representa el tamaño del array.
k = int(input())
# Solicitamos al usuario que ingrese una línea de números separados por espacios.
num = input().split()
# Inicializamos una lista vacía para almacenar los elementos del array.
lista = []
# Iteramos sobre los primeros K elementos de la lista ingresada.
for i in range(k):
    # Convertimos cada elemento a entero y lo añadimos a la lista.
    datos = int(num[i])
    lista.append(datos)
# Solicitamos al usuario que ingrese un número entero N, que representa la posición en el array.
n = int(input())
# Imprimimos los elementos de la lista separados por espacios.
print(*lista)
# Imprimimos el elemento en la posición N del array.
print(lista[n])