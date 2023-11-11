casos = int(input())
for i in range(casos):
    cartas = int(input())
    piso = 0
    cartasUsadas = 0
    menos = 0
    cartasTotales = cartas
    while cartas > 0:
        piso += 1
        cartasUsadas += piso * 2 + piso - 1 
        menos = piso * 2 + piso - 1
        cartas -= menos
    if cartasTotales == cartasUsadas:
        print(piso, cartasTotales-cartasUsadas)
    else:
        cartasUsadas -= piso * 2 + piso - 1
        piso -= 1
        print(piso, cartasTotales-cartasUsadas)