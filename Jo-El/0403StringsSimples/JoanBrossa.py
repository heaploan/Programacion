# Obtener el número de casos de prueba
casos = int(input())
# Iterar a través de cada caso de prueba
for z in range(casos):
    # Leer la frase y convertirla a minúsculas
    frase = input().lower()
    # Inicializar contadores para cada vocal
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    # Contar la frecuencia de cada vocal en la frase
    for vocal in frase:
        if vocal == "a":
            a += 1
        elif vocal == "e":
            e += 1
        elif vocal == "i":
            i += 1
        elif vocal == "o":
            o += 1
        elif vocal == "u":
            u += 1
    # Inicializar la vocal ganadora y su frecuencia
    ganadora = "a"
    frecuencia = a
    # Comparar la frecuencia de cada vocal
    if e > frecuencia:
        ganadora = "e"
        frecuencia = e
    if i > frecuencia:
        ganadora = "i"
        frecuencia = i
    if o > frecuencia:
        ganadora = "o"
        frecuencia = o
    if u > frecuencia:
        ganadora = "u"
        frecuencia = u
    # Imprimir la vocal ganadora para el caso actual
    print(f"Vocal guanyadora: {ganadora}")

    