nombre=input("Ingrese su nombre completo: ")
#hace una lista con ambos introducidos.
o=nombre.split(" ")
#imprime nombre en minusculas
print(nombre.lower())
#imprime nombre en mayusculas.
print(nombre.upper())
#si queremos que ponga la primera mayuscula de los dos tanto apellido como nombre, creamos este for.
for i in o:
    #dentro de los valores que pilla i de o, se pone en mayuscula la primera letra de cada y termina en espacio para que se muestre espacio entre ellas.
    print(i.capitalize(), end=" ")