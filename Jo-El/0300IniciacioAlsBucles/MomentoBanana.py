#creamos la variable data para introducir el numero de casos que se presentan
data=int(input())
#este for lo creamos para crear el rango poniendo data como tal.
for i in range(data):
    #creamos el split para poner los dos numeros de vida y daño
    entrada=input()
    datos=entrada.split(" ")
    n1=int(datos[0])
    n2=int(datos[1])
    #comprobamos que si n2 es mayor que n1, entonces imprime Nope.
    #en caso de que n1 sea igual a n2, tambien imprime Nope.
    if n1<n2 or n1==n2 or n1*0.2>=n2:
        print("Nope")
    #calculamos el 20% de n1 y ponemos el n2 como el numero del daño
    elif n1*0.2 < n2:
        #en caso de que n2 sea mayor al 20% del numero introducido, se imprimira momento banana.
        print("Momento Banana")