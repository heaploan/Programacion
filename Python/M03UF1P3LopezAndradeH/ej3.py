#importamos la librería de random
import random
#creamos una lista para guardar después datos en esta
lista = []
#creamos este for para que en un rango de 30
for i in range(30):
    #se añaden 30 valores a lista poniendo de 0 a 29.
    lista.append(random.randint(0,29))
#imprimimos la lista
print(lista)
#creamos esta variable con valor a 0 para guardar datos despues
repeticiones = 0
#creamos este for con rango de 30 para recorrer la lista
for repetido in range(30):
    #si repetido es igual an contenido de lista en rango
    if repetido == lista[repetido]:
        #sumamos uno a repeticiones
        repeticiones += 1
        print(f"El numero {repetido} esta en la lista en la posiscion {lista[repetido]}")
#si la variable repeticiones es 0, se imprime que no hay ninguna coincidencia de numero en la posicion de la lista.
if repeticiones == 0:
    print("Cap numero ha coincidit amb la seva posicio.")