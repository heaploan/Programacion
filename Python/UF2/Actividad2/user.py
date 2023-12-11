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
# Comprobamos tambimén que el mes introducido tenga los días introducidos.
def demanarNaixament():
    meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    check = True
    while check:
        day = int(input("Introduce tu day de nacimiento: "))
        while day < 0 or day > 31:
            print("ERROR: El day no existe, introduce un día válido.")
            day = int(input("Introduce tu day de nacimiento: "))

        month = int(input("Introduce el número de tu month de nacimiento: "))
        while month < 1 or month > 12:
            print("ERROR: El month no es correcto, introduce un month válido")
            month = int(input("Introduce el número de tu month de nacimiento: "))

        year = int(input("Introduce tu año de nacimiento (entre 1900 y 2001): "))
        while year < 1900 or year > 2001:
            print("ERROR: año incorrecto, introduce uno dentro del rango.")
            year = int(input("Introduce tu año de nacimiento (entre 1900 y 2001): "))    
        if day <= meses[month -1]:
            check = False
        else:
            print("El mes no tiene tantos días.")
    return datetime.date(year, month, day).strftime("%d/%m/%y")

# d)
# Creamos una funcion que recibirá tres valores
# Se comprobará que el usuario y la clave correspondan a un usuario del diccionario.
def login(diccionario, usuario, key):
    if usuario in diccionario:
        if diccionario[usuario]['password'] == key:
            return True
        else:
            return False
  
# diccionario = {}
# usuario = input()
# diccionario[usuario] = {}
# contraseña = input()
# diccionario[usuario]['password'] = contraseña