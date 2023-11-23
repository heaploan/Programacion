casos = int(input())
for i in range(casos):
    palabra1 = input()
    palabra2 = input()
    if len(palabra1) > len(palabra2):
        maxLongitud = len(palabra1)
        minLongitud = len(palabra2)
    else:
        maxLongitud = len(palabra2)
        minLongitud = len(palabra1)
    contador = 0
    for j in range(minLongitud):
        if palabra1[j] == palabra2[j]:
            contador += 1
    if maxLongitud / 2 <= contador:
        print("GRACIES WEBCASTELLER")
    else:
        print("WEBCASTELLER ESTA TRAVIESO HOY")