#creamos la variable casos para introducir las veces que queremos realizar el bucle.
casos = int(input("Inserta un numero de casos a considerar: "))
# Mientras casos sea menor a 0, entra en el bucle.
# En caso de ser número negativo, se vuelve a pedir un número.
# En caso de ser 0, se sale del bucle.
while casos < 0:
    print("Por favor, inserta un numero mayor a 0.")
    casos = int(input("Inserta un numero de casos a considerar: "))
# Creamos un bucle for para que se considere el número de veces introducido en casos.
for i in range(casos):
    # Solicita al usuario una frase y la divide en palabras.
    frase = input("Inserta una frase: ").split()  
    # Inicializamos una variable para construir la frase modificada.
    frasePuntos = ""  
    # Iteramos a través de las palabras en la frase.
    for l in range(len(frase)):  
        # Obtenemos la palabra actual.
        palabraActual = frase[l]  
        # Agregamos la palabra actual a la frase modificada.
        frasePuntos += palabraActual  
        # Verificamos si no es la última palabra en la frase.
        if l < len(frase) - 1:  
            # Obtenemos la palabra siguiente.
            palabraSiguiente = frase[l + 1]  
            # Comparamos la longitud de la palabra actual con la siguiente.
            if len(palabraActual) < len(palabraSiguiente):
                # Si la actual es más corta, agregamos puntos suspensivos.
                frasePuntos += "... "  
            else:
                # Si la actual es igual o más larga, agregamos un espacio.
                frasePuntos += " "  
     # Imprimimos la frase modificada.
    print(f"Frase modificada: {frasePuntos}") 

