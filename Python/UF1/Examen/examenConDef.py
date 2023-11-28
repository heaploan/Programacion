def altaModul(moduls):
    modul = input("Introdueix el nom del mòdul: ")
    if modul in moduls:
        print("ERROR: El nom del mòdul ja està registrat.")
    else:
        moduls[modul] = {}
        print("Mòdul registrat correctament.")

def altaNotaUf(moduls):
    if not moduls:
        print("ERROR: no s'ha trobat cap mòdul")
    else:
        nomModul = input("Introdueix el mòdul al que vols afegir notes: ")
        if nomModul in moduls:
            nomUf = input("Introdueix el nom de la UF: ")
            if nomUf in moduls[nomModul]:
                print("ERROR: la UF ja està registrada.")
            else:
                nota = int(input("Introdueix la nota de la UF: "))
                if 0 < nota <= 10:
                    moduls[nomModul][nomUf] = nota
                    print(f"UF i nota registrades correctament.")

def veureDadesModul(moduls):
    if not moduls:
        print("ERROR: no s'ha trobat cap mòdul.")
    else:
        mostrar = input("Introdueix el nom del mòdul que vols veure: ")
        if mostrar in moduls:
            print(f"Mòdul: {mostrar}")
            for atributo, valor in moduls[mostrar].items():
                print(f"{atributo}: {valor}")
                sumaNotes = 0
                totalNotes = 0
                for ufDict in moduls.values():
                    for valor in ufDict.values():
                        sumaNotes += valor
                        totalNotes += 1
                    media = sumaNotes / totalNotes
            print(f"Media de les notes: {media:.2f}\nTotal de notes ingresades: {totalNotes}")

def percentatgeAprovat(moduls):
    if not moduls:
        print("ERROR: no s'ha trobat cap mòdul.")
    else:
        totalUf = 0
        totalAprovades = 0
        for modul, ufDict in moduls.items():
            totalUfModul = 0
            totalAprovadesModul = 0
            for nota in ufDict.values():
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

moduls = {}

opcion = int(input("*** Expedient acadèmic ***\n1. Alta de mòdul\n2. Alta de nota d'unitat formativa\n3. Veure dades del mòdul\n4. Percentatge aprovat\n5. Sortir\nIndica una opció: "))

while opcion != 5:
    if opcion == 1:
        altaModul(moduls)
    elif opcion == 2:
        altaNotaUf(moduls)
    elif opcion == 3:
        veureDadesModul(moduls)
    elif opcion == 4:
        percentatgeAprovat(moduls)
    
    opcion = int(input("*** Expedient acadèmic ***\n1. Alta de mòdul\n2. Alta de nota d'unitat formativa\n3. Veure dades del mòdul\n4. Percentatge aprovat\n5. Sortir\nIndica una opció: "))
