casos = int(input())
for i in range(casos):
    k = int(input())
    diccionario = {}
    for j in range(k - 1):
        amistad = input().split()
        diccionario[amistad[0]] = amistad[1]
        diccionario[amistad[1]] = amistad[0]
    amigoBuscado = input()
    print(diccionario.get(amigoBuscado))