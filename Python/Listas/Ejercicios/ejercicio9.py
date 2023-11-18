nombres=[]
edades=[]
nom=""
#creamos while para que mientras el valor de nom sea diferente a * se haga el bucle
#si es * deja de hacerse el bucle.
while nom != "*":
    nom=input("Introduce el nombre del alumno: ")
    if nom != "*":
        nombres.append(nom)
        edad=int(input("Introduce su edad: "))
        edades.append(edad)
#una vez se ha terminado de introducir los datos.
maximo=edades[0]
mayor=nombres[0]
print("Alumnos mayores de edad: ")
#generamos este for para mover la posicion en el rango de la longitud de edades.
for posicio in range(len(edades)):
    #si edades es mayor que maximo
    if edades[posicio] > maximo:
        #mayor es igual a la posicion en nombres
        mayor = nombres[posicio]
        #mayor es igual a la posicion en edades
        maximo = edades[posicio]
    #si edades es igual o mayor a 18
    if edades[posicio] >= 18:
        #imprimimos la posicion de los nombres y edades.
        print(nombres[posicio], edades[posicio])
#imprimimos el alumno mayor de todos y su edad. 
print(f"El alumno mayor es: {mayor} con {maximo} años de edad.")