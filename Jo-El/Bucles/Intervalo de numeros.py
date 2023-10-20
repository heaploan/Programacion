#creamos la variable n para meter el input
n = input()
#la variable num le asignamos la separacion de la variable n
num = n.split(" ")
#creamos la svariables num1 y num2 con sus respectivos int(num[0]) y (num[1]) empezando desde 0.
num1 = int(num[0])
num2 = int(num[1])
#creamos if con ambas variables especificando que mientras num1 sea mayor que num2 se haga el intervalo
if num1 >= num2:
    #ponemos el -1,-1 para que se cuente del mayor al menor.
    for i in range(num1, num2-1, -1):
        print(i)
#en caso de que no sea menor el num2 que el num1 salta el mensaje diciendo el problema.
else:
    print("El segon numero no es mes petit que el primer")