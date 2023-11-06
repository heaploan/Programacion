casos = int(input("Introdueix el nombre de casos a considerar: "))
for i in range(casos):
    numeros=input().split(" ")
    posicion = 0
    suma = 0
    for i in numeros:
        if posicion != 0:
            suma += int(i)
        else:
            posicion += 1
        print(suma)