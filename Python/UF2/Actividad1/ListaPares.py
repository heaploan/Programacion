# Recibe una lista y calcula si los numeros dentro de ella son pares.
# Añade los numeros que son pares en la lista 'pares'
def pares(lista):
    pares = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            pares.append(lista[i])
    return pares

myList = [-12, 84, 13, 20, -33, 101, 9]
result = pares(myList)
print(result)