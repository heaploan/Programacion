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
        
    print(piso, cartasTotales-cartasUsadas)
# 2
# 1
# 4
# 2
# 6
# 3
# 8
# 4