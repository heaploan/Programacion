#creamos la variable numeros para guardar lveces que te pedirá un numero.
numeros = int(input("Introdueix un numero (numero negativo para salir): "))
#creamos dos listas, con repeticiones y sin repeticiones
sinRep = []
conRep = []
#creamos este while para entrar en el bucle de pedir el numero hasta que sea 0
while numeros >= 0:
    #si los numeros no están en sinRep, se añaden
    if numeros not in sinRep:
        sinRep.append(numeros)
    #los numeros que se introducen se agregan todos aunque estén repetidos
    conRep.append(numeros)
    #volvemos a pedir el numero para poder terminar el bucle
    numeros = int(input("Introdueix un numero (numero negativo para salir): "))
print("Llista de numeros")
#creamos este for para imprimir la lista con repeticiones
for i in conRep:
    #ponemos i porque es el contenido de la lista conRep y end para que termine en espacio
    print(i, end=" ")
print("\nLlista de numeros sense repeticions")
#creamos este for para imprimir la lista sinRep.
for i in sinRep:
    #imprimimos i porque es el contenido de la lista sinRep y end para que termine en espacio
    print(i, end=" ")