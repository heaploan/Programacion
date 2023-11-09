<<<<<<< HEAD
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
=======
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
>>>>>>> refs/remotes/origin/main
        repeticiones += 1
        #imprimimos el numero repetido y su posicion en la lista. 
        print(f"El numero {repetido} esta en la lista en la posiscion {lista[repetido]}")
<<<<<<< HEAD
#si repeticiones es 0
=======
#si la variable repeticiones es 0, se imprime que no hay ninguna coincidencia de numero en la posicion de la lista.
>>>>>>> refs/remotes/origin/main
if repeticiones == 0:
    #entonces ningun numero ha coincidido con su numero de posicion en la lista. 
    print("Cap numero ha coincidit amb la seva posicio.")