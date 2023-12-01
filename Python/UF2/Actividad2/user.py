# Los imports siempre se ponen al principio del documento
import datetime 

# a)
# Creamos una función para validar una edad que se le pide al usuario
# Si la edad está dentro del rango mencionado, devuelve la edad.
def validarEdad():
    age = int(input("Introduce tu edad (de 0 a 130): "))
    while age < 0 or age > 130: 
        print("Edad incorrecta, ingresa una dentro del rango")
        age = int(input("Introduce tu edad: "))
    return age

# b)
# Creamos una funcion para validar que el usuario es de la longitud adecuada
# y si la llave tiene al menos una vocal y su longitud es al menos de 6 digitos.
def validarUsuario(user, key):
    comprobacion = []
    if len(user) < 4:
        return False
    else:
        comprobacion.append(True)
    vocal = 0
    if len(key) < 6:
        return False
    else:
        for i in key:
            if i.lower() in "aeiou":
                vocal += 1
        if vocal == 0:
            comprobacion.append(False)
        elif vocal >= 1:
            comprobacion.append(True)
        resultado = 0
        for condicion in comprobacion:
            if condicion == True:
                resultado += 1
        if resultado == 2:
            return True
        else:
            return False

# c)
# creamos una variable donde pedimos la fecha de nacimiento y la mostramos en formato dd/mm/yyyy
# para el formato importamos la librería de datetime
def demanarNaixament():
    dia = int(input("Introduce tu dia de nacimiento: "))
    while dia < 0 or dia > 31:
        print("ERROR: El dia no existe, introduce un día válido.")
        dia = int(input("Introduce tu dia de nacimiento: "))

    mes = int(input("Introduce el número de tu mes de nacimiento: "))
    while mes < 1 or mes > 12:
        print("ERROR: El mes no es correcto, introduce un mes válido")
        mes = int(input("Introduce el número de tu mes de nacimiento: "))

    any = int(input("Introduce tu año de nacimiento (entre 1900 y 2001): "))
    while any < 1900 or any > 2001:
        print("ERROR: año incorrecto, introduce uno dentro del rango.")
        any = int(input("Introduce tu año de nacimiento (entre 1900 y 2001): "))    
    
    return datetime.date(any, mes, dia).strftime("%d/%m/%y")

# d)
# Creamos una funcion que recibirá tres valores
# Se comprobará que el usuario y la clave correspondan a un usuario del diccionario.
def login(diccionario, usuario, key):
    if usuario in diccionario:
        if diccionario[usuario] == key:
            return True
        else:
            return False