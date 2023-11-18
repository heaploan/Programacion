#creamos lista vacia
lista=[]
#creamos el random
import random
#creamos un rango de 10
for i in range(10):
    #agregamos los valores de ranom a lista y colocamos el rango del 1 al 10
    lista.append(random.randint(1,10))
    #imprimimos la lista para que muestre los valores usando la variable i
    #ponemos **2 para hacer el cuadrado y **3 para hacerlo al cubo.
    print(lista[i],lista[i]**2, lista[i]**3)
    