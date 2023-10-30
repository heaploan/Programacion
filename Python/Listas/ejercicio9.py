nombres=[]
edades=[]
nom=""
while nom != "*":
    nom=input("Introduce el nombre del alumno: ")
    if nom != "*":
        nombres.append(nom)
        edad=int(input("Introduce su edad: "))
        edades.append(edad)
maximo=edades[0]
mayor=nombres[0]
print("Alumnos mayores de edad: ")
for posicio in range(len(edades)):
    if edades[posicio] > maximo:
        mayor = nombres[posicio]
        maximo = edades[posicio]
    if edades[posicio] >= 18:
        print(nombres[posicio], edades[posicio])
print(f"El alumno mayor es: {mayor} con {maximo} años de edad.")