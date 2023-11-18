# Se solicita al usuario ingresar un número entero y se almacena en la variable 'k'
k = int(input())
# Se solicita al usuario ingresar una línea de números separados por espacios y se almacenan en la variable 'numeros'
numeros = input().split()
# Se solicita al usuario ingresar otro número entero y se almacena en la variable 'n'
n = int(input())
# Se utiliza un bucle for para iterar sobre cada índice en el rango de 'k'
for i in range(k):
    # Se convierte el elemento en la posición 'i' de 'numeros' a entero y se le suma 'n'
    numeros[i] = int(numeros[i]) + n
    # Se imprime el elemento modificado seguido de un espacio, utilizando end=" "
    print(numeros[i], end=" ")