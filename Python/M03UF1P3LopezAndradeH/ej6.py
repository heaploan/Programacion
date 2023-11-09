palabras = []
opcion = int(input("1. Afegir paraula.\n2. Comptar.\n3. Modificar\n4. Eliminar.\n5. Mostrar.\n6. Sortir.\nElige una opcion: "))
while opcion != 6:
    if opcion == 1:
        palabra = input("Introduce una palabra: ")
        palabras.append(palabra)
    
    elif opcion == 2:
        palabra = input("Introduce una palabra para contador: ")
        if palabra in palabras:
            contador = 0
            for i in range(len(palabras)):
                if palabra == palabras[i]:
                    contador += 1    
            print(f"{palabra} aparece {contador} veces en la lista")
        else:
            print("La palabra introducida no esta en la lista.")
    
    elif opcion == 3:
        modificacion = input("Introduce la palabra a modificar: ")
        nuevaPalabra = input("Introduce la nueva palabra: ")
        if modificacion in palabras:
            for i in range(len(palabras)):    
                if palabras[i] == modificacion:
                    palabras[i] = nuevaPalabra
                    print("Palabra modificada.")
        else:
            print("La palabra introducida no esta en la lista.") 

    elif opcion == 4:
        eliminar = input("Escribe la palabra a eliminar: ")
        if eliminar in palabras:
            while eliminar in palabras:
                palabras.remove(eliminar)  
                print("Palabra eliminada.")
        else:
            print("La palabra introducida no esta en la lista.")
    
    elif opcion == 5:
        lista = ""
        for i in palabras:
            lista = i   
            print(lista, end="\t")

    opcion = int(input("1. Afegir paraula.\n2. Comptar.\n3. Modificar\n4. Eliminar.\n5. Mostrar.\n6. Sortir.\nElige una opcion: "))
print("¡Hasta luego!")

            
                

