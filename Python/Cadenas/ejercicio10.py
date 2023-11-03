#creamos la variable entry vacia con comillas para indicar texto
entry=""
#mientras entry sea diferente a si entramos en bucle
while entry != "si":
    #pedimos la respuesta con un input.
    entry = input("Vols sortir? (si/no): ")
    #convertimos lo introducido a minusculas
    entry = entry.lower()  
    #si entry es igual a no, continuamos
    if entry == "no":
        print("¡Al infinito y mas alla!")
    #si entry es diferente a si, se pone algo al azar, imprime el mensaje de error.
    elif entry != "si":
        print("Por favor, responde 'si' o 'no'.")
#si se cumple que entry es igual a Si, termina el bucle mostrando este mensaje.
print("¡Hasta luego!'")