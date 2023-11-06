numeros = int(input("Introdueix un numero (numero negativo para salir): "))

sinRep = []
conRep = []

while numeros >= 0:
    if numeros not in sinRep:
        sinRep.append(numeros)
    conRep.append(numeros)
    numeros = int(input("Introdueix un numero (numero negativo para salir): "))
print("Llista de numeros")

for i in conRep:
    print(i, end=" ")
print("\nLlista de numeros sense repeticions")

for i in sinRep:
    print(i, end=" ")