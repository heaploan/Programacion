# Se crea un diccionario vacío para almacenar los módulos y las notas de las unidades formativas (UF).
moduls = {}
# Se lee la opción del usuario desde la entrada estándar.
opcion = int(input("*** Expedient acadèmic ***\n1. Alta de mòdul\n2. Alta de nota d'unitat formativa\n3. Veure dades del mòdul\n4. Percentatge aprovat\n5. Sortir\nIndica una opció: "))
# Se inicia un bucle while que continuará hasta que el usuario seleccione la opción 5 (Salir).
while opcion != 5:
    # Se verifica la opción seleccionada por el usuario y se ejecuta la acción correspondiente.
    if opcion == 1:
        # Alta de módulo
        modul = input("Introdueix el nom del mòdul: ")
        if modul in moduls:
            print("Error: El nom mòdul ja està registrat.")
        else:
            # Se agrega el módulo al diccionario de módulos como una clave con un diccionario vacío como valor.
            moduls[modul] = {}
            print("Mòdul afegit correctament")
    elif opcion == 2:
        # Alta de nota de unidad formativa
        # Se verifica si hay módulos registrados.
        if not moduls:
            print("ERROR: no s'ha trobat cap modul.")
        else:
            # Se solicita al usuario que ingrese el nombre del módulo al que quiere agregar una nota.
            nomModul = input("Introdueix el mòdul al que vols afegir nota: ")
            # Se verifica si el módulo está registrado.
            if nomModul in moduls:
                # Se solicita al usuario que ingrese el nombre de la UF a la que quiere agregar una nota.
                nomUF = input("Introdueix el nom de la UF: ")
                # Se verifica si la UF ya tiene una nota registrada.
                if nomUF in moduls[nomModul]:
                    print("ERROR: la UF ja està registrada.")
                else:
                    # Se solicita al usuario que ingrese la nota de la UF.
                    nota = int(input("Introdueix la nota de la UF: "))
                    # Se verifica que la nota esté en el rango permitido (entre 1 y 10).
                    if 0 < nota <= 10:
                        # Se agrega la UF y su nota al diccionario del módulo.
                        moduls[nomModul][nomUF] = nota
                        # Se calcula la media de todas las notas ingresadas.
                        # Se inicializa la suma de las notas y el total de notas a cero.
                        sumaNotes = 0
                        totalNotes = 0
                        # Se itera sobre cada diccionario de UF en los módulos y cada valor (nota) en esos diccionarios.
                        for ufDict in moduls.values():
                            for valor in ufDict.values():
                                # Se suma el valor (nota) a la suma total de notas.
                                sumaNotes += valor
                                # Se incrementa el contador de total de notas.
                                totalNotes += 1
                        # Se calcula la media de las notas.
                        media = sumaNotes / totalNotes

                        print(f"UF i nota registrades correctament.\nTotal de notes ingresades: {totalNotes}")
                    else:
                        print("ERROR: la nota no pot ser 0 o major a 10")
            else:
                print("Error: no s'ha trobat el mòdul")
    elif opcion == 3:
        # Ver datos del módulo
        # Se verifica si hay módulos registrados.
        if not moduls:
            print("Error: no s'ha trobat cap mòdul.")
        else:
            # Se solicita al usuario que ingrese el nombre del módulo del que quiere ver los datos.
            mostrar = input("Introdueix el nom del mòdul que vols veure: ")
            # Se verifica si el módulo está registrado.
            if mostrar in moduls:
                print(f"Mòdul: {mostrar}")
                # Se imprime cada UF y su nota en el módulo.
                for atributo, valor in moduls[mostrar].items():
                    print(f"{atributo}: {valor}")
                # Se imprime la media de todas las notas en el expediente académico.
                print(f"Media de les notes: {media:.2f}")
            else:
                print("Error: no s'ha trobat el mòdul")
    elif opcion == 4:
        # Calcular porcentaje aprobado
        # Se verifica si hay módulos registrados.
        if not moduls:
            print("ERROR: no s'ha trobat cap mòdul")
        else:
            # Se inicializan contadores para el total de UF y el total de UF aprobadas.
            # Se inicializan contadores para el total de UF y el total de UF aprobadas.
            totalUf = 0
            totalAprovades = 0
            # Se itera sobre cada módulo y sus UF.
            for modul, ufdict in moduls.items():
                # Se inicializan contadores para el total de UF y el total de UF aprobadas en el módulo actual.
                totalUfModul = 0
                totalAprovadesModul = 0
                # Se itera sobre las notas (valores) de las UF en el módulo actual.
                for nota in ufdict.values():
                    # Se incrementa el contador de total de UF en el módulo actual.
                    totalUfModul += 1
                    # Se verifica si la nota es mayor o igual a 5 para contarla como aprobada.
                    if nota >= 5:
                        totalAprovadesModul += 1
                # Se suman los totales del módulo actual a los totales generales.
                totalUf += totalUfModul
                totalAprovades += totalAprovadesModul
            # Se calcula el porcentaje de UF aprobadas en el expediente académico.
            if totalUf > 0:
                percentatge = (totalAprovades / totalUf) * 100
            else:
                percentatge = 0
            # Se imprime el porcentaje de UF aprobadas.
            print(f"Percentatge d'UFs aprovades: {percentatge}")
    # Se vuelve a solicitar al usuario que ingrese una opción.
    opcion = int(input("1. Alta de mòdul\n2. Alta de nota d'una unitat formativa d'un modul\n3. Veure dades d'un mòdul\n4. Veure percentatge d'unitats formatives aprovades.\n5. Sortir\nIndica una opció: "))
