#creamos lista vacía
lista=[]
#creamos variable num con valor 0 para ponerle valor despues
num=0
#mientras que num sea mayor o igual a 0 pedirá introducir numeros.
while num >= 0:
    #pedimos valor a num.
    num=int(input())
    #si num es mayor o igual a 0 se añade el valor a la lista
    if num >=0:
        #añadimos los valores de num a la lista.
        lista.append(num)
#imprimimos lista.
print(lista)
