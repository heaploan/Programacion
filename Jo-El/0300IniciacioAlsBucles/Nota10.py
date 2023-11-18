a=0
#creamos la variable n para el int,input y poder ingresar las notas
n=0
#creamos las variables para el conteo de las notas
notas10=0
notas=0
#mientras que sea true, se hace el bucle con este while
while a==0:
    #ponemos la variable n con su int,input
    n=int(input())
    #si n es 10 se contara en notas10 sumando 1
    if n==10:
        notas10+=1
    #si n entra en el rango de 0 a 10 se cuenta como notas sumando 1
    if 0<=n<=10:
        notas+=1
    #si n es -1 se rompe el bucle
    if n==-1:
        a=1
#ponemos el print fuera de los if para mostrar el total de ambas variables.
print(f"TOTAL NOTES: {notas} NOTES10: {notas10}")
