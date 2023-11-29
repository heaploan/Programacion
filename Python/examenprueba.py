# Crear diccionario vacío
modulos = {"M3": {"UF": 1}}
# Pedimos opciones al usuario.
opciones = int(input("***** Expedient Academic *****\n1) Alta de un modulo\n2) Alta nota de una unidad\n3) Ver datos de un modulo\n4) Porcentaje de UF aprobadas\n5) Salir\nIntroduce una opcion: "))
# Valoramos que las opciones estén dentro del rango del 1 al 4 y 5 para salir.
while opciones != 5:
    # Si opciones es 1, pedimos los datos del módulo y agregamos al diccionario si es correcto.
    if opciones == 1:
        modulo = input("Introduce el nombre del modulo: ").upper()
        # Si el módulo que queremos añadir ya está en el diccionario, muestra mensaje de error.
        if modulo in modulos:
            print("ERROR: El modulo ya esta registrado.")
        else:
            # En caso de que no esté aún, se agrega al diccionario.
            modulos[modulo] = {}
            print("Modulo registrado correctamente")
    # Si opciones es 2 pedimos los datos del módulo al que se le  quiere añadir la nota.
    elif opciones == 2:
        # En caso de que no haya ningún módulo registrado en el diccionario, mostramos mensaje de error. 
        if not modulos:
            print("ERROR: No hay ningun modulo registrado")
        else:
            # En caso de haber modulos, pedimos el nombre del módulo.
            mostrar = input("Introduce el modulo al que quieres agregar notas: ").upper()
            # Si no existe el nombre del módulo introducido, mostramos mensaje de error
            if not mostrar:
                print("ERROR: El modulo no existe")
            else:
                # En caso de estar, pedimos el nombre de la UF.
                nombreUf = input("Introduce el nombre de la UF: ")
                # Si la UF ya está en los módulos, mostramos mensaje de error.
                if nombreUf in modulos[modulo]:
                    print("ERROR: La UF ya esta registrada.")
                else:
                    # En caso contrario, pedimos la nota.
                    nota = int(input("Introduce la nota de la UF: "))
                    # Valoramos que la nota sea mayor a 0 y menor o igual a 10
                    if 0 < nota <= 10:
                        # En caso de ser así, la agregamos al diccionario y su modulo correspondiente.
                        modulos[mostrar][nombreUf] = nota
                        print("Modulo registrado correctamente.")
                    else:     
                        # De no ser así, mostramos mensaje de error.
                        print("ERROR: La nota no puede ser menor a 0 o mayor a 10")
            
    elif opciones == 3:
        if not modulos:
            print("ERROR: No hay modulos registrados.")
        else:
            mostrar = input("Introduce el nombre del modulo que quieres ver: ").upper()
            if mostrar in modulos:
                print(f"Nombre: {mostrar}")
                for atributo, valor in modulos[mostrar].items():
                    print(f"{atributo}: {valor}")
                
        

    opciones = int(input("***** Expedient Academic *****\n1) Alta de un modulo\n2) Alta nota de una unidad\n3) Ver datos de un modulo\n4) Porcentaje de UF aprobadas\n5) Salir\nIntroduce una opcion: "))
