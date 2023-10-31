#se importa valor de random
import random
#creamos lista
lista=[]
#creamos las columnas con este for en rango indicado.
for columnas in range(5):
    #creamos lista2
    lista2=[]
    #creamos las filas que tendra al final lista.
    for filas in range(5): 
        #le agregamos los 5 valores a la lista
        lista2.append(random.randint(1,5))
    #se le agrega cada fila a lista con los valores
    lista.extend([lista2])
#l coge los valores que hay en lista
for l in lista:
    #creamos la variable suma.
    suma=0
    #creamos este for para que z vaya recorriendo acada valor de l
    for z in l:
        #se hace la suma de cada valor de z en horizontal.
        suma+=z
        print(z, end="\t")
    print("=\t", suma, end="\n")
for i in range(5):
    print("=", end="\t")
print()
#creamos este for para recorrer 5 valores
for i in range(5):
    suma=0
    #creamos este for para recorrer 5 valores
    for w in range(5):
        #se hace la suma de lista en forma vertical, invirtiendo el movimiento poniendo w primero e i segundo
        #w va desplazandose por cada valor y la i cada columna, al poner la w primero, invertimos de horizontal a vertical.
        suma+=lista[w][i]
    print(suma, end="\t")     