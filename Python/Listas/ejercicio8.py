#creamos las tres listas vacias para asignarles valor.
lista1=[]
lista2=[]
lista3=[]
#creamos 3 for, 2 para agregar 5 numeros para lista1 y lista2
for i in range(5):
    num=int(input("Introduce cinco numeros aleatorios para la primer lista: "))
    lista1.append(num)
for i in range(5):
        num2=int(input("Introduce cinco numeros aleatorios para la segunda lista: "))
        lista2.append(num2)
#este tercer for es el que hará el calculo de lista1 y lista2
for i in range(5):
    #suma es igual a lista1 con rango i mas lista2 con rango i para sumar los valores de cada mismo lugar en ambas listas.
    suma=lista1[i]+lista2[i]
    #colocamos los valores totales de la suma en lista3
    lista3.append(suma)
#imprimimos las 3 listas.
print(f"{lista1}\n{lista2}\n{lista3}")
