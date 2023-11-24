casos = int(input())
for i in range(casos):
    diccionario = {}
    k = int(input())
    for j in range(k - 1):
        amistad = input().split()
        diccionario[amistad[0]] = amistad[1]
    ultimoAmigo = input()
    while ultimoAmigo in diccionario:
        ultimoAmigo = diccionario[ultimoAmigo]
    print(ultimoAmigo)
