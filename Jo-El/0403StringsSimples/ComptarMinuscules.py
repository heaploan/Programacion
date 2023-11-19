# Obtener el número de casos de prueba
casos = int(input())
# Iterar a través de cada caso de prueba
for i in range(casos):
    # Leer la palabra
    palabra = input()
    # Inicializar contador para letras minúsculas
    minuscules = 0
    # Contar letras minúsculas en la palabra
    for letra in palabra:
        if letra.islower():
            minuscules += 1
    # Imprimir la cantidad de letras minúsculas en la palabra actual
    print(minuscules)