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
# Itera a través de los elementos en la lista 'conRep'
for i in conRep:
    # Imprime el valor actual de 'i' seguido de un espacio en la misma línea
    print(i, end=" ")

# Imprime una línea en blanco para separar la lista de números sin repeticiones
print("\nLlista de numeros sense repeticions")
#imprimimos la lista sin forma de dicha sino, solo numeros con espacio
for i in sinRep:
    #imprimimos i porque es el contenido de la lista sinRep y end para que termine en espacio
    print(i, end=" ")