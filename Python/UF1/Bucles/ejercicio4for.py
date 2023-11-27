sum=0
#creamos for con la variable num y ponemos el rango, incluimos el 0 para poder marcar el multiple de 3
for num in range(0,101,3):
    #aqui hacemos la sumas de todos los multiplos de 3
    sum+=num
    if num==99:
        print(sum, end="=")
    else:
        print(sum, end="+") 
#ponemos el print fuera del for para que muestre el resultado total de todas las sumas del bucle
print(sum)