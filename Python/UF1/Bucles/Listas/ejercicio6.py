#importamos random
import random
#creamos lista vacía
lista=[]
#creamos for para poner el rango de veces que se generará el random
for i in range(10):
    #agregamos a la lista los valores que generó random, un total de 10
    lista.append(random.randint(1,100))
#ordenamos la lista de mayor a menor.
lista.sort(reverse=True)
#imprimimos la lista.
print(lista)