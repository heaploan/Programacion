#creamos sum para que tenga el contenido de la suma que se hará a num
sum=0
#num será la variable que tenga el rango marcado
num=0
while num<=100:
    #a sum se le suma num, sum coge el valor de num para sumarselo.
    sum+=num
    #num se le suma 1
    #este if es para que en cuanto la suma llegue al 100, se muestre el igual para mostrar el resultado total
    if num==100:
        print(num, end="=")
    else:
        #en todos los casos diferentes se muestra el simbolo de suma.
        print(num,end="+")
    num+=1
#el print se pone fuera del while para que se muestre solo una vez el resultado del bucle
print(sum)