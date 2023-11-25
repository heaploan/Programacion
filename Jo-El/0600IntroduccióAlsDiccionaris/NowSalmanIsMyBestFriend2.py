# Se lee la cantidad de casos que se van a evaluar
casos = int(input())
# Se itera sobre cada caso
for i in range(casos):
    # Se lee el número de amistades que se van a ingresar
    k = int(input())
    # Se crea un diccionario vacío para almacenar las relaciones de amistad
    diccionario = {}
    # Se itera sobre cada amistad, excepto la última
    for j in range(k - 1):
        # Se lee la entrada que representa una relación de amistad
        amistad = input().split()
        # Se agrega al diccionario, donde el primer elemento es el amigo 1 y el segundo es el amigo 2
        # Además, se invierte la relación y se agrega al diccionario también
        diccionario[amistad[0]] = amistad[1]
        diccionario[amistad[1]] = amistad[0]
    # Se lee el amigo que se está buscando en la cadena de amistades
    amigoBuscado = input()
    # Se imprime el amigo asociado al amigo buscado en el diccionario (si existe)
    print(diccionario.get(amigoBuscado))