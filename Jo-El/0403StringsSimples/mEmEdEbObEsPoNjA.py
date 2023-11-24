casos = int(input())
lineas = []
for i in range(casos):
    linea = input()
    lineas.append(linea)
for linea in lineas:
    resultado = ""
    mayuscula = False
    for caracter in linea:
        if caracter.isalpha():
            if mayuscula:
                resultado += caracter.upper()
            else:
                resultado += caracter.lower()

            mayuscula = not mayuscula
        else:
            resultado += caracter
    print(resultado)