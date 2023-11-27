#creamos la variable a con solo comillas para que pueda tener contenido
a=" "
#este while marca que mientras a sea diferente a sortir, repita el imput
while a!="sortir":
    a=input("Introduce cualquier cosa para repetirlo y sortir para terminar: ")
    #el if es para hacer que si el a es diferente a sortir, siga repitiendo el input y si es salir, deje de hacer print
    if a!="sortir":
        print(a)
    else:
        print("Adios")