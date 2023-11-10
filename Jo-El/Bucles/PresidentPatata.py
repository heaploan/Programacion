#Introducimos el numero de casos de prueba.
entry=int(input())
#Entramos en un bucle que se repetirá el numero de veces ingresado en "entry".
for i in range(entry):
    #para cada caso de prueba leemos el numero de veces que el usuario desea realizar.
    repetition=int(input())
    #entramos en otro bucle que se repetirá las veces introducidas en "repetition"
    for z in range(repetition):
        #imprimimos la frase ingresada en print usando "repetition" como rango.
        print("No ofendre al president patata")