#creamos ambas variables de positivos y negativos para llevar el conteo.
positivos = 0
negativos = 0
#creamos booleano de contar con valor True
contar = True
#mientras contar sea True
while contar:
    #pediremos el numero
    numero = int(input())
    #si numero es igual a 0
    if numero == 0:
        #contar se convierte a False
        contar = False
    #si numero es mayor a 0
    if numero > 0:
        #sumamos 1 a positivos
        positivos += 1
    #si numero es menor a 0
    elif numero < 0:
        #sumamos 1 a negativos
        negativos += 1
#si positivos es mayor a negativos
if positivos > negativos:
    #imprimimos positivos
    print("POSITIUS")
#si positivos es menor que negativos
elif positivos < negativos:
    #imprimimos negativos
    print("NEGATIUS")
#en caso de que ambos sean iguales
else:
    #imprimimos iguales.
    print("IGUALS")


