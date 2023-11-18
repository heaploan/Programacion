#creamos la variable de alumnos para pedir la informacion
alumnes=int(input("Ingresa el número de alumnos: "))
#hacemmos los if con los diferentes valores referentes a la cantidad de alumnos utilizando elif
#se coloca una multiplicacion del precio por la cantidad de alumnos para saber el total a pagar
if alumnes>=100:
    print("El coste por alumno es de 65, el total seria de: ",65*alumnes)
elif 50<=alumnes<=99:
    print("El coste por alumno es de 70 euros, el total seria de: ", 70*alumnes)
elif 30<=alumnes<=49:
    print("El coste por alumno es de 95 euros, el total seria de: ", 95*alumnes)
elif alumnes<30 and alumnes>=1:
    print("La renta del autobus es de 4000 sin importar la cantidad de alumnos")
else:
    print("Los datos introducidos no son validos")