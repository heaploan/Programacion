moduls = {}

opcion = int(input("*** Expedient acadèmic ***\n1. Alta de mòdul\n2. Alta de nota d'unitat formativa\n3. Veure dades del mòdul\n4. Percentatge aprovat\n5. Sortir\nIndica una opció: "))

while opcion != 5:
    if opcion == 1:
        modul = input("Introdueix el nom del mòdul: ")
        if modul in moduls:
            print("Error: El nom mòdul ja està registrat.")
        else:
            moduls[modul] = {}
            print("Mòdul afegit correctament")
    elif opcion == 2:
        if not moduls:
            print("ERROR: no s'ha trobat cap modul.")
        else:
            nomModul = input("Introdueix el mòdul al que vols afegir nota: ")
            if nomModul in moduls:
                nomUF = input("Introdueix el nom de la UF: ")
                if nomUF in moduls[nomModul]:
                    print("ERROR: la UF ja està registrada.")
                else:
                    nota = int(input("Introdueix la nota de la UF: "))
                    if 0 < nota <= 10:
                        moduls[nomModul][nomUF] = nota
                        sumaNotes = 0
                        totalNotes = 0
                        for ufDict in moduls.values():
                            for valor in ufDict.values():
                                sumaNotes += valor
                                totalNotes += 1
                        media = sumaNotes / totalNotes
                        print(f"UF i nota registrades correctament.\nTotal de notes ingresades: {totalNotes}")
                    else:
                        print("ERROR: la nota no pot ser 0 o major a 10")
            else:
                print("Error: no s'ha trobat el mòdul")
    elif opcion == 3:
        if not moduls:
            print("Error: no s'ha trobat cap mòdul.")
        else:
            mostrar = input("Introdueix el nom del mòdul que vols veure: ")
            if mostrar in moduls:
                print(f"Mòdul: {mostrar}")
                for atributo, valor in moduls[mostrar].items():
                    print(f"{atributo}: {valor}")
                print(f"Media de les notes: {media:.2f}")
            else:
                print("Error: no s'ha trobat el mòdul")
    elif opcion == 4:
        if not moduls:
            print("ERROR: no s'ha trobat cap mòdul")
        else:
            totalUf = 0
            totalAprovades = 0
            for modul, ufdict in moduls.items():
                totalUfModul = 0
                totalAprovadesModul = 0
                for nota in ufdict.values():
                    totalUfModul += 1
                    if nota >= 5:
                        totalAprovadesModul += 1
                totalUf += totalUfModul
                totalAprovades += totalAprovadesModul
            if totalUf > 0:
                percentatge = (totalAprovades / totalUf) * 100
            else:
                percentatge = 0
            print(f"Percentatge d'UFs aprovades: {percentatge}")

    opcion = int(input("1. Alta de mòdul\n2. Alta de nota d'una unitat formativa d'un modul\n3. Veure dades d'un mòdul\n4. Veure percentatge d'unitats formatives aprovades.\n5. Sortir\nIndica una opció: "))
