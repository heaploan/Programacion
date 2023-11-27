# Inicialización del diccionario que contendrá los personajes
personajes = {}
# Variable de control para continuar o salir del bucle
continuar = True
# Bucle principal
while continuar:
    # Solicitar al usuario que ingrese una opción
    opcion = input("1) Agregar personaje.\n2) Borrar personaje\n3) Mostrar personaje.\n4) Mostrar todo.\n5) Mostrar un tipo.\n6) Salir.\nEscoge una opcion: ")
    # Verificar si la opción ingresada es un número
    if opcion.isdigit():
        opcion = int(opcion)
        # Verificar si la opción está en el rango del 1 al 6
        if 1 <= opcion <= 6:
            # Opción 1: Agregar personaje
            if opcion == 1:
                # Inicializar un diccionario para almacenar los datos del personaje
                datos = {}
                # Solicitar al usuario que ingrese el nombre del personaje
                personaje = input("Introduce el nombre del personaje: ")
                # Verificar si el nombre del personaje ya está registrado
                if personaje in personajes:
                    print("ERROR: el nombre del personaje ya está registrado")
                else:
                    # Solicitar al usuario que ingrese los atributos del personaje
                    datos["Fuerza"] = int(input("Introduce su fuerza: "))
                    datos["Resistencia"] = int(input("Introduce su resistencia: "))
                    datos["Vida"] = int(input("Introduce su vida: "))
                    # Solicitar al usuario que ingrese el tipo del personaje (mago o guerrero)
                    tipo = input("Introduce el tipo (mago o guerrero): ")
                    datos["Tipo"] = tipo.lower()
                    # Validar que el tipo sea mago o guerrero
                    while datos["Tipo"] != "mago" and datos["Tipo"] != "guerrero":
                        print("ERROR: ¡Solo pueden ser magos o guerreros!")
                        tipo = input("Introduce el tipo (mago o guerrero): ")
                        datos["Tipo"] = tipo.lower()
                    # Solicitar atributo adicional dependiendo del tipo
                    if datos["Tipo"] == "guerrero":
                        datos["Armadura"] = int(input("Introduce el valor de su armadura: "))
                    elif datos["Tipo"] == "mago":
                        datos["Mana"] = int(input("Introduce la cantidad de mana que tiene: "))
                    # Agregar el personaje al diccionario de personajes
                    personajes[personaje] = datos
                    print("¡Personaje añadido correctamente!")
            # Opción 2: Borrar personaje
            elif opcion == 2:
                # Verificar si no hay personajes registrados
                if personajes == {}:
                    print("ERROR: ¡No hay personajes registrados!")
                else:
                    # Solicitar al usuario que ingrese el nombre del personaje a eliminar
                    eliminar = input("Introduce el nombre del personaje que deseas eliminar: ")
                    # Verificar si el personaje existe y eliminarlo
                    if eliminar in personajes:
                        personajes.pop(eliminar)
                        print("¡Personaje eliminado correctamente!")
                    else:
                        print("ERROR: ¡Personaje no encontrado!")
            # Opción 3: Mostrar personaje específico
            elif opcion == 3:
                # Verificar si no hay personajes registrados
                if personajes == {}:
                    print("ERROR: ¡No hay personajes registrados!")
                else:
                    # Solicitar al usuario que ingrese el nombre del personaje a mostrar
                    mostrar = input("Introduce el nombre del personaje que deseas ver: ")
                    # Verificar si el personaje existe y mostrar sus atributos
                    if mostrar in personajes:
                        print(f"Nombre: {mostrar}")
                        for atributo, valor in personajes[mostrar].items():
                            print(f"{atributo}: {valor}", end=" ")
                        print("\n--------------------------------------------------------------------------------------------------")
                    else:
                        print("ERROR: ¡Personaje no encontrado!")
            # Opción 4: Mostrar todos los personajes
            elif opcion == 4:
                # Verificar si no hay personajes registrados
                if personajes == {}:
                    print("ERROR: ¡No hay personajes registrados!")
                else:
                    # Mostrar todos los personajes y sus atributos
                    for personaje, datos in personajes.items():
                        print(f"Nom: {personaje}")
                        for atributo, valor in datos.items():
                            print(f"{atributo}: {valor}", end=" ")
                        print("\n---------------------------------------------------------------------------------------------------")
            # Opción 5: Mostrar personajes de un tipo específico
            elif opcion == 5:
                # Verificar si no hay personajes registrados
                if personajes == {}:
                    print("ERROR: ¡No hay personajes registrados!")
                else:
                    # Solicitar al usuario que ingrese el tipo a mostrar
                    mostrarTipo = input("Ingresa la clase a mostrar: ")
                    mostrarTipo = mostrarTipo.lower()
                    
                    # Validar que el tipo sea mago o guerrero
                    if mostrarTipo not in ["mago", "guerrero"]:
                        print("ERROR: ¡La clase introducida no existe!")
                    else:
                        encontrado = False
                        # Mostrar personajes del tipo especificado
                        for personaje, datos in personajes.items():
                            if datos["Tipo"] == mostrarTipo:
                                encontrado = True
                                print(f"Nombre: {personaje}")
                                for atributo, valor in datos.items():
                                    print(f"{atributo}: {valor}", end=" ")
                                print("\n---------------------------------------------------------------------------------------------------")
                        # Mostrar mensaje si no se encontraron personajes del tipo especificado
                        if not encontrado:
                            print(f"No hay personajes del tipo {mostrarTipo}")
            # Opción 6: Salir del bucle
            elif opcion == 6:
                continuar = False
        else:
            print("ERROR: Por favor, ingresa una opción válida del 1 al 6.")
    else:
        print("ERROR: Por favor, ingresa una opción válida (número entero).")
# Mensaje de despedida al salir del bucle
print("¡Hasta luego!")