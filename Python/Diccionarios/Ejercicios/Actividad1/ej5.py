# Se crea un diccionario vacío llamado 'personajes' para almacenar información sobre los personajes.
personajes = {}
# Se solicita al usuario que elija una opción del menú.
opcion = int(input("1. Afegir personatge\n2. Esborrar personatge.\n3. Mostrar personatge\n4. Mostrar totes les dades de tots els personatges.\n5. Mostrar les dades d'un tipus de personatge\n6. Sortir.\nTria una opció: "))
# Inicio de un bucle while que se ejecuta mientras la opción ingresada no sea 6 (Salir).
while opcion != 6:
    # Opción 1: Agregar un personaje.
    if opcion == 1:
        # Se crea un diccionario vacío para almacenar los atributos del personaje.
        data = {}
        # Se solicita al usuario el nombre del personaje.
        personaje = input("Introdueix el nom del personatge: ")
        # Verificar si el personaje ya está en la lista.
        if personaje in personajes:
            print("Error: El nom del personatge ja està registrat")
        else:
            # Recopilar información sobre el personaje.
            data["Força"] = int(input("Introdueix la seva força: "))
            data["Resistencia"] = int(input("Introdueix la seva resistencia: "))
            data["Vida"] = int(input("Introdueix la seva vida: "))
            tipus = input("Introdueix el tipus mag o guerrer: ")
            data["Tipus"] = tipus.lower()
            # Validar que el tipo sea 'mag' o 'guerrer'.
            while data["Tipus"] != "mag" and data["Tipus"] != "guerrer":
                print("Error: solsament pot ser mag o guerrer")
                tipus = input("Introdueix el tipus mag o guerrer: ")
                data["Tipus"] = tipus.lower()
            # Solicitar información adicional según el tipo de personaje.
            if data["Tipus"] == "guerrer":
                data["Armadura"] = int(input("Introdueix el valor de l'armadura: "))
            elif data["Tipus"] == "mag":
                data["Mana"] = int(input("Introdueix el valor del mana: "))
            # Agregar el personaje al diccionario 'personajes'.
            personajes[personaje] = data
            print("Personatge afegit correctament")
    # Opción 2: Eliminar un personaje.
    elif opcion == 2:
        # Verificar si no hay personajes en la lista.
        if personajes == {}:
            print("Error: no s'ha trobat cap personatge.")
        else:
            # Solicitar al usuario el nombre del personaje a eliminar.
            eliminar = input("Introdueix el nom del personatge a esborrar: ")
            # Verificar si el personaje a eliminar existe y eliminarlo.
            if eliminar in personajes:
                # Elimina el personaje con la clave 'eliminar' del diccionario 'personajes'
                # Busca el nombre que se introduzca para eliminar todos los datos de dicho personaje.
                personajes.pop(eliminar)
                print("Personatge eliminat correctament.")
            else:
                print("Error: no s'ha trobat el personatge")
    # Opción 3: Mostrar información de un personaje específico.
    elif opcion == 3:
        # Verificar si no hay personajes en la lista.
        if personajes == {}:
            print("Error: no s'ha trobat cap personatge.")
        else:
            # Solicitar al usuario el nombre del personaje a mostrar.
            mostrar = input("Introdueix el nom del personatge a mostrar: ")
            # Verificar si el personaje a mostrar existe y mostrar sus atributos.
            if mostrar in personajes:
                print(f"Nom: {mostrar}")
                for atributo, valor in personajes[mostrar].items():
                    print(f"{atributo}: {valor}", end=" ")
                print()
            else:
                print("Error: no s'ha trobat el personatge")
    # Opción 4: Mostrar todas las características de todos los personajes.
    elif opcion == 4:
        # Verificar si no hay personajes en la lista.
        if personajes == {}:
            print("Error: no s'ha trobat cap personatge.")
        else:
            # Iterar sobre cada personaje y sus atributos.
            for personaje, datos in personajes.items():
                print(f"\nNom: {personaje}")
                for atributo, valor in datos.items():
                    print(f"{atributo}: {valor}", end=" ")
                print()
                print("------------------------------------------------------------------")
    # Opción 5: Mostrar información de un tipo específico de personaje.
    elif opcion == 5:
        # Verificar si no hay personajes en la lista. 
        if personajes == {}:
            print("Error: no s'ha trobat cap personatge.")
        else: 
            # Solicitar al usuario el tipo de personaje a mostrar.
            mostrarTipus = input("Introdueix el tipus a mostrar: ")
            mostrarTipus = mostrarTipus.lower()
            # Verificar si el tipo ingresado es válido.
            if mostrarTipus not in ["mag", "guerrer"]:
                print("Error: tipus no valid.")
            else:
                # Variable booleana para rastrear si se ha encontrado al menos un personaje del tipo especificado.
                encontrado = False
                # Iterar sobre cada personaje y mostrar solo los del tipo especificado.
                for personaje, datos in personajes.items():
                    if datos["Tipus"] == mostrarTipus:
                        # Se encontró al menos un personaje del tipo especificado
                        encontrado = True
                        print(f"\nNom: {personaje}")
                        for atributo, valor in datos.items():
                            print(f"{atributo}: {valor}", end=" ")
                        print()
                        print("------------------------------------------------------------------")
                # Si no se encontraron personajes del tipo especificado, imprimir un mensaje.
                if not encontrado:
                    print(f"No hi ha cap personatge del tipus {mostrarTipus}")
    # Opción inválida.
    else:
        print("Opcion incorrecta, introduce alguna de las que estan en el menú.")
    # Solicitar nuevamente al usuario que elija una opción del menú.
    opcion = int(input("\n1. Afegir personatge\n2. Esborrar personatge.\n3. Mostrar personatge\n4. Mostrar totes les dades de tots els personatges.\n5. Mostrar les dades d'un tipus de personatge\n6. Sortir.\nTria una opció: "))