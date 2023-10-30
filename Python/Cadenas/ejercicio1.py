nombre=input("Ingrese su nombre completo: ")
#hace una lista con ambos introducidos.
o=nombre.split(" ")
print(nombre.lower())
print(nombre.upper())
#si queremos que ponga la primera mayuscula de los dos tanto apellido como nombre, creamos este for.
for i in o:
    print(i.capitalize(), end=" ")