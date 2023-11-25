# Se lee la cantidad de casos que se van a evaluar
casos = int(input())
# Se itera sobre cada caso
for i in range(casos):
    # Se crea un diccionario vacío para almacenar las amistades
    diccionario = {}
    # Se lee el número de amistades que se van a ingresar
    k = int(input())
    # Se itera sobre cada amistad, excepto la última
    for j in range(k - 1):
        # Se lee la entrada que representa una relación de amistad
        amistad = input().split()
        # Se agrega al diccionario, donde el primer elemento es el amigo 1 y el segundo es el amigo 2
        diccionario[amistad[0]] = amistad[1]
    # Se lee el último amigo en la secuencia
    ultimoAmigo = input()
    # Mientras el último amigo esté en el diccionario, se actualiza con su nuevo amigo
    while ultimoAmigo in diccionario:
        ultimoAmigo = diccionario[ultimoAmigo]
    # Se imprime el último amigo en la cadena de amistades
    print(ultimoAmigo)