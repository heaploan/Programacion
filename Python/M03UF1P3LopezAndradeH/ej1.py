<<<<<<< HEAD
#creamos la variabl enumeros para introducirle un numero.
numeros = int(input("Introdueix un numero (numero negativo para salir): "))
#creamos listas una sin repeticiones y otra con repeticiones pero vacias. 
sinRep = []
conRep = []
#creamos este while para que mientras sea mayor o igual a 0 entre en bucle
while numeros >= 0:
    #si numeros no esta en la lista sin repeticiones, se introduce el valor
    if numeros not in sinRep:
        sinRep.append(numeros)
    #se agregan todos los valores introducidos en la variable numeros.
    conRep.append(numeros)
    #volvemos a pedir numeros
    numeros = int(input("Introdueix un numero (numero negativo para salir): "))
print("Llista de numeros")
#imprimimos la lista sin forma de dicha si no, solo numeros con espacio
=======
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
>>>>>>> refs/remotes/origin/main
for i in conRep:
    #ponemos i porque es el contenido de la lista conRep y end para que termine en espacio
    print(i, end=" ")
print("\nLlista de numeros sense repeticions")
<<<<<<< HEAD
#imprimimos la lista sin forma de dicha sino, solo numeros con espacio
=======
#creamos este for para imprimir la lista sinRep.
>>>>>>> refs/remotes/origin/main
for i in sinRep:
    #imprimimos i porque es el contenido de la lista sinRep y end para que termine en espacio
    print(i, end=" ")