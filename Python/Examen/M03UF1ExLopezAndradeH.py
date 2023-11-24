# Examen 
moduls = {}
opcion = int(input("*** Expedient acadèmic ***\n1. Alta de mòdul\n2. Alta de nota d'unitat formativa\n3. Veure dades del mòdul\n4. Percentatge aprovat\n5. Sortir\nIndica una opció: "))
while opcion != 5:
    if opcion == 1:
        ufs = {}
        modul = input("Introdueix el nom del mòdul: ")
        if modul in moduls:
            print("Error: El nom mòdul ja està registrat.")
        moduls[modul] = modul
        print("Mòdul afegit correctament")
    elif opcion == 2:
        if moduls == {}:
            print("ERROR: no s'ha trobat cap modul.")
        else: 
            nomUF = input("Introdueix el nom de la UF: ")
            if nomUF in ufs:
                print("ERROR: la UF ja està registrada.")
            else:
                ufs[nomUF] = nomUF
                ufs["Nota"] = int(input("Introdueix la nota de la UF: "))
            moduls[modul] = ufs
            print("UF i nota registrades correctament.")
    elif opcion == 3:
        if moduls == {}:
            print("Error: no s'ha trobat cap mòdul.")
        else:
            mostrar = input("Introdueix el nom del mòdul que vols veure: ")
            if mostrar in moduls:
                print(f"Mòdul: {mostrar}")
                for atributo, valor in moduls[mostrar].items():
                    print(f"{atributo}: {valor}", end=" ")
                print()
            else:
                print("Error: no s'ha trobat el mòdul")
    elif opcion == 4:
        if moduls == {}:
            print("ERROR: no s'ha trobat cap mòdul")
        else:
            print("")
    opcion = int(input("1. Alta de mòdul\n2. Alta de nota d'una unitat formativa d'un modul\n3. Veure dades d'un mòdul\n4. Veure percentatge d'unitats formatives aprovades.\n5. Sortir\n"))
