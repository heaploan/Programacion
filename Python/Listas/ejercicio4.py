#creamos una lista vacia para añadirle los valores después
lista=[]
#creamos un for con un rango de 5 para solo meter 5 numeros.
for i in range(5):
    #pedimos los valores 
    notas=int(input("Introduce 5 notas del 0 al 10: "))
    #introducimos los valores que pedimos a lista
    lista.append(notas)
    #creamos la variable suma para mas adelante hacer un calculo
    suma=0
    #creamos esta variable para saber el rango de lista  y una vez se complete, dejar de sumar.
    p=0
    for n in lista:
        #sumamos n que serian los numeros que estan en la lista
        suma+=n
        #cada vez que se hace una suma, se añade 1 a p.
        p+=1
        #creamos la variable media para hacer la suma dividido por p que es la cantidad de numeros que hay en lista.
        media=suma/p
    #creamos la variable maximo con lista en primera posición.
    maximo=lista[0]
    #creamos el for para saber el numero maximo
    for max in lista:
        #si max es mayor a maximo se modifica el numero y se queda siempre el mayor. 
        if max > maximo:
            maximo = max
    #creamos la variable minimo con la lista en primera posición.
    minimo=lista[0]
    #creamos este for para saber el numero minimo
    for min in lista:
        #si min es menor que minimo, se modifica el numero y se queda siempre el menor
        if min < minimo:
            minimo = min        
print(f"Notas: {lista}, Media: {media}, Menor nota: {minimo}, Maxima nota: {maximo}")
    