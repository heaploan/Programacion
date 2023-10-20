#creamos la variable numero para introducir el dato con int(input)
numero=int(input())
#creamos el if para indicar el caso de que siempre que el numero sea mayor a 0
if numero>=0:
    #creamos el for con su variable y ponemos la variable numero,-1,-1 para que se haga la cuenta atrás.
    for i in range(numero,-1,-1):
        #imprimimos la variable i.
        print(i)