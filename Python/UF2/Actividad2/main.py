from user import *
from dates import *
dictionary = {}

options = int(input("1. Registrar usuario\n2. Login\n3. Mostrar datos de un usuario\n4. Salir\nIntroduce una opción: "))

while options != 4:
    if options == 1:
        user = input("Introduce tu nombre de usuario (debe tener al menos 4 letras): ")
        if user in dictionary:
            print("ERROR: Usuario ya registrado")
        else:
            key = input("Crear contraseña (debe tener al menos 6 caracteres y al menos una vocal): ")
            if validarUsuario(user, key): 
                dictionary[user] = {}
                dictionary[user]["password"] = key
                dictionary[user]["age"] = pedirEdad()
                dictionary[user]["birthdate"] = pedirNacimiento()
                print("Usuari registrat correctament!")
            else:
                print("ERROR: El usuario o contraseña no cumplen con los requisitos indicados.")

    elif options == 2:
        user = input("Introduce tu nombre de usuario: ")
        key = input("Introduce tu contraseña: ")
        if login(dictionary, user, key):
            print(f"¡Bienvenido, {user}!")
            print(avui())
            if aniversari(dictionary[user]["birthdate"]):
                print("¡Es el mes de tu cumpleaños!")
            else:
                print("Este mes no es tu cumpleaños.")
            print(quantFalta(dictionary[user]["birthdate"]))
        else:
            print("ERROR: El usuario o la contraseña son incorrectos.")
    
    elif options == 3:
        user = input("Introduce el usuario que quieres ver: ")
        if user in dictionary:
            print(f"Datos de {user}")
            print("Edad:", dictionary[user]["age"])
            print("Próximo cumpleaños:", properAniversari(dictionary[user]["birthdate"]))
        else:
            print("ERROR: No existe dicho usuario.")

    else:
        print("ERROR: ¡La opción no es correcta!")

    options = int(input("1. Registrar usuario\n2. Login\n3. Mostrar datos de un usuario\n4. Salir\nIntroduce una opción: "))