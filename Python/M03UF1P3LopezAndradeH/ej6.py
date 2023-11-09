# Creamos una lista vacía llamada 'palabras' para almacenar las palabras.
palabras = []
# Solicitamos al usuario que elija una opción del menú.
opcion = int(input("1. Afegir paraula.\n2. Comptar.\n3. Modificar\n4. Eliminar.\n5. Mostrar.\n6. Sortir.\nElige una opción: "))
# Comenzamos un bucle que se ejecuta mientras la opción no sea 6 (Salir).
while opcion != 6:
    # Si la opción es 1, el usuario quiere añadir una palabra a la lista.
    if opcion == 1:
        palabra = input("Introduce una palabra: ")
        # Añadimos la palabra a la lista 'palabras'.
        palabras.append(palabra)  
    # Si la opción es 2, el usuario quiere contar cuántas veces aparece una palabra en la lista.
    elif opcion == 2:
        palabra = input("Introduce una palabra para el contador: ")
        # Si la palabra esta en la lista 'palabras' entramos en el bucle
        if palabra in palabras:
            # Creamos la variable contador
            contador = 0
            # Creamos este for para contar por toda la lista la palabra repetida
            for i in range(len(palabras)):
                # Se palabra es igual a palabras y posicion de esta
                if palabra == palabras[i]:
                    # Se cuenta la palabra repetida
                    contador += 1
            print(f"{palabra} aparece {contador} veces en la lista")
        else:
            # En caso de que la palabra no se encuentre en la lista.
            print("La palabra introducida no está en la lista.")
    # Si la opción es 3, el usuario quiere modificar una palabra en la lista.
    elif opcion == 3:
        modificacion = input("Introduce la palabra a modificar: ")
        nuevaPalabra = input("Introduce la nueva palabra: ")
        if modificacion in palabras:
            for i in range(len(palabras)):
                # Si la palabras y su posicion son iguales a la palabra introducida en modificacion
                if palabras[i] == modificacion:
                    # Reemplazamos la palabra antigua por la nueva.
                    palabras[i] = nuevaPalabra  
                    print("Palabra modificada.")
        else:
            # En caso de que la palabra no se encuentre en la lista.
            print("La palabra introducida no está en la lista.")
    # Si la opción es 4, el usuario quiere eliminar una palabra de la lista.
    elif opcion == 4:
        eliminar = input("Escribe la palabra a eliminar: ")
        # Si la palabra introducida en eliminar se encuentra en la lista 'palabras'
        if eliminar in palabras:
            # Mientras la palabra introducida en eliminar este en la lista 'palabras'
            while eliminar in palabras:
                # Eliminamos todas las instancias de la palabra. 
                palabras.remove(eliminar)
                print("Palabra eliminada.")
        else:
            print("La palabra introducida no está en la lista.")
    # Si la opción es 5, el usuario quiere mostrar todas las palabras de la lista.
    elif opcion == 5:
        # En caso de que la lista este vacia, mostrara este error.
        if len(palabras) == 0:
            print("La lista esta vacia, no se pudo imprimir.")
        else:
            lista = "" 
            # Itera a través de los elementos en la lista 'palabras'
            for i in palabras:
            # Asigna el valor actual de 'i' a la variable 'lista'
                lista = i
            # Imprime el valor de 'lista' seguido de un tabulador ('\t') en la misma línea
            print(lista, end="\t")
            print()
    # Pedimos al usuario que elija otra opción antes de volver a evaluar el bucle.
    opcion = int(input("1. Afegir paraula.\n2. Comptar.\n3. Modificar\n4. Eliminar.\n5. Mostrar.\n6. Sortir.\nElige una opción: "))
# Cuando el usuario elige la opción 6 (Salir), el bucle termina y se muestra un mensaje de despedida.
print("¡Hasta luego!")