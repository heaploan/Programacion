# Se solicita al usuario ingresar un número entero y se almacena en la variable K
K = int(input())
# Se crea una lista vacía llamada 'array' para almacenar datos posteriormente
array = []
# Se utiliza un bucle for para iterar K veces y recopilar datos del usuario
for i in range(K):
    # Se solicita al usuario ingresar un dato y se almacena en la variable 'dato'
    dato = input()
    # Se agrega el dato a la lista 'array'
    array.append(dato)
# Se solicita al usuario ingresar otro número entero y se almacena en la variable N
N = int(input())
# Se utiliza un bucle for para imprimir cada cadena en la lista 'array'
for cadena in array:
    print(cadena)
# Se intenta imprimir el elemento en la posición N de la lista 'array'
print(array[N])
