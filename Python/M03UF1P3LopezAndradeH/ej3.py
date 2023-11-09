#importamos la libreria de random.
import random
#creamos lista
lista = []
#creamos este for con rango de 30
for i in range(30):
    #agregamos un valor random del 0 al 29 a lista
    lista.append(random.randint(0,29))
#imprimimos la lista con los valores.
print(lista)
#creamos la variable repeticiones.
repeticiones = 0
#creamos este for para recorrer la lista en rango 30.
for repetido in range(30):
    #si repetido es igual al valor introducido en lista y su posicion.
    if repetido == lista[repetido]:
        #sumamos 1 a repeticiones
        repeticiones += 1
        #imprimimos el numero repetido y su posicion en la lista. 
        print(f"El numero {repetido} esta en la lista en la posiscion {lista[repetido]}")
#si repeticiones es 0
if repeticiones == 0:
    #entonces ningun numero ha coincidido con su numero de posicion en la lista. 
    print("Cap numero ha coincidit amb la seva posicio.")