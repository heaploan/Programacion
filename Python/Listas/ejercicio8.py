#creamos las tres listas vacias para asignarles valor.
lista1=[]
lista2=[]
lista3=[]
#creamos 3 for, 2 para agregar 5 numeros para lista1 y lista2
for i in range(5):
    #pedimos 5 numeros para agregar a lista 1
    num=int(input("Introduce cinco numeros aleatorios para la primer lista: "))
    lista1.append(num)
    #pedimos otros 5 numeros para agregar a lista 2
    num2=int(input("Introduce cinco numeros aleatorios para la segunda lista: "))
    lista2.append(num2)
    #suma es igual a lista1 con rango i mas lista2 con rango i para sumar los valores de cada mismo lugar en ambas listas.
    suma=lista1[i]+lista2[i]
    #colocamos los valores totales de la suma en lista3
    lista3.append(suma)
#imprimimos las 3 listas.
print(f"{lista1}\n{lista2}\n{lista3}")