# Pedir al usuario que ingrese el número de casos
casos = int(input())
# Inicializar una lista para almacenar las líneas de texto
lineas = []
# Ingresar las líneas de texto según el número de casos
for i in range(casos):
    linea = input()
    lineas.append(linea)
# Procesar cada línea e imprimir el resultado
for linea in lineas:
    # Inicializar una cadena vacía para almacenar el resultado
    resultado = ""
    # Inicializar una variable que indica si la siguiente letra debe ser mayúscula o minúscula
    mayuscula = False
    # Iterar sobre cada caracter en la línea
    for caracter in linea:
        # Verificar si el caracter es alfabético (una letra)
        if caracter.isalpha():
            # Agregar el caracter a la cadena resultado, alterando entre mayúsculas y minúsculas
            if mayuscula:
                resultado += caracter.upper()
            else:
                resultado += caracter.lower()
            # Cambiar el estado de mayúscula para el próximo caracter
            mayuscula = not mayuscula
        else:
            # Si el caracter no es alfabético, simplemente agregarlo a la cadena resultado
            resultado += caracter
    # Imprimir el resultado para la línea actual
    print(resultado)