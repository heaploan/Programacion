personajes = {}
opcion = int(input("1. Afegir personatge\n2. Esborrar personatge.\n3. Mostrar personatge\n4. Mostrar totes les dades de tots els personatges.\n5. Mostrar les dades d'un tipus de personatge\n6. Sortir.\nTria una opció: "))
while opcion != 6:

    if opcion == 1:
        data = {}
        personaje = input("Introdueix el nom del personatge: ")
        if personaje in personajes:
            print("Error: El personaje ya esta en la lista.")
        else:     
            data["Força"] = int(input("Introdueix la seva força: "))  
            data["Resistencia"] = int(input("Introdueix la seva resistencia: "))
            data["Vida"] = int(input("Introdueix la seva vida: "))
            tipus = input("Introdueix el tipus mag o guerrer: ")
            data["Tipus"] = tipus.lower()
            while data["Tipus"] != "mag" and data["Tipus"] != "guerrer":
                print("Error: solsament pot ser mag o gerrer")
                tipus = input("Introdueix el tipus mag o guerrer: ")
                data["Tipus"] = tipus.lower() 
            if data["Tipus"] == "guerrer":
                data["Armadura"] = int(input("Introdueix el valor de l'armadura: "))
            elif data["Tipus"] == "mag":
                data["Mana"] = int(input("Introdueix el valor del mana: "))
            personajes[personaje] = data
            print("Personaje añadido correctamente")  
                    
    elif opcion == 2:
        if personajes == {}:
            print("Error: no s'ha trobat cap personatge.")
        else:
            eliminar = input("Introdueix el nom del personatge a esborrar: ")
            if eliminar in personajes:
                personajes.pop(eliminar)
                print("Personaje eliminado correctamente.")
            else:
                print("Error: personaje no encontrado")            

    elif opcion == 3:
        if personajes == {}:
            print("Error: no s'ha trobat cap personatge.")
        else:
            mostrar = input("Introdueix el nom del personatge a mostrar: ")
            if mostrar in personajes:
                for mostrar in personajes:
                    print(f"Nom: {mostrar}")
                    for dada in personajes[mostrar]:
                        print(dada, personajes[personaje][dada], end=" ")
                    print()
            else:
                print("Error: presonatge no trobat.")

    elif opcion == 4:
        
        print("a")
    elif opcion == 5:
        print("a")
    else:
        print("Opcion incorrecta, introduce alguna de las que estan en el menú.")
    
    opcion = int(input("1. Afegir personatge\n2. Esborrar personatge.\n3. Mostrar personatge\n4. Mostrar totes les dades de tots els personatges.\n5. Mostrar les dades d'un tipus de personatge\n6. Sortir.\nTria una opció: "))