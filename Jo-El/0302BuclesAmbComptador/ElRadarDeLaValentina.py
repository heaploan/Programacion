casos = int(input())
for i in range(casos):
    mediciones = input().split()
    categoria = "H"
    for medicion in mediciones:
        medicion = int(medicion)
        if medicion >= 10000:
            categoria = "M"
            break
        elif medicion >= 1000:
            categoria = "B"
    print(categoria)