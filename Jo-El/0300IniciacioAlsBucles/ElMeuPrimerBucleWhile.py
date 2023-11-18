#creamos la variable num con su int,input vacio
num = int(input())
#el while lo creamos y ponemos la variable num diferente a 0
while num != 0:
    #creamos la variable result y le asignamos el resultado de num + 1
    result = num + 1
    #imprimimos result
    print(result)
    #volvemos a pedir que introduzca otro número para salir del bucle infinito, si no, se queda repitiendo el mismo numero sin parar.
    num = int(input())