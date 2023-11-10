#creamos variable antes del for para insertar el numero del rango.
num=int(input())
#i coge los valores que se ponen en el rango
for i in range(1,num+1):
    #se empieza por i, se excluye el 0 y el -1 indica la cuenta atras.
    for z in range(i,0,-1):
        #imprimimos z ya que coge el valor del rango de i con end="" sin espacio entre las comillas.
        print(z,end="")