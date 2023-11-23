casos = int(input())
for i in range(casos):
    palabra1 = input()
    palabra2 = input()
    lenPalabra1 = len(palabra1)
    lenPalabra2 = len(palabra2)
    maxLongitud = lenPalabra1
    if lenPalabra2 > lenPalabra1:
        maxLongitud = lenPalabra2
    palabra1 += " " * (maxLongitud - lenPalabra1)
    palabra2 += " " * (maxLongitud - lenPalabra2)
    coincidencias = 0
    for j in range(maxLongitud):
        if palabra1[j] == palabra2[j]:
            coincidencias += 1
    if lenPalabra2 > lenPalabra1:
        print("WEBCASTELLER ESTA TRAVIESO HOY")
    else:
        if coincidencias >= maxLongitud / 2:
            print("GRACIES WEBCASTELLER")