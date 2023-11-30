import datetime
def validarEdad():
    age = int(input("Introduce tu edad (de 0 a 130): "))
    while age < 0 or age > 130: 
        print("Edad incorrecta, ingresa una dentro del rango")
        age = int(input("Introduce tu edad: "))
    return age

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

def demanarNaixament():
    dia = int(input("Introduce tu dia de nacimiento: "))
    
    
    while dia < 0 or dia > 31:
        print("ERROR: El dia no existe, introduce un día válido.")
        dia = int(input("Introduce tu dia de nacimiento: "))

    mes = int(input("Introduce el número de tu mes de nacimiento: "))
    while mes < 1 or mes > 12:
        print("ERROR: El mes no es correcto, introduce un mes válido")
        mes = int(input("Introduce el número de tu mes de nacimiento: "))
    # any = int(input("Introduce tu año de nacimiento: "))


demanarNaixament()
