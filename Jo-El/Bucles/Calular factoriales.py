#creamos la variable x con su int,input para poner cuantas veces se ingresaran los datos.
x=int(input())
#creamos el while para comprovar que mientras x sea mayor que 0, haga el factorial
while x>0:
    #con la variable n pedimos los numeros de los cuales se haran las factoriales.
    n=int(input())
    factorial=1
    #mientras n sea diferente a 0 se llevara a cabo el for.
    if n!=0:
        #como las factoriales empiezan en 1, el rango empieza en 1 y el n+1 para que incluya el numero.
        for i in range (1,n+1):
            #el factorial seria el numero de la factorial por i
            factorial*=i
    #hacemos el print fuera del for para que imprima solamente el resultado total
    print(factorial)
    #sin esta x el bucle se hara infinito.
    x-=1
