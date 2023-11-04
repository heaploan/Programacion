aparcar = True
while aparcar:
    longitudCoche = int(input())
    mejorPlaza = 0
    encontradaPlaza = False
    if longitudCoche == 0:
        aparcar = False
    else:
        buscarPlaza = True
        contadorPlaza = 0
        while buscarPlaza:
            posiblePlaza = input()
            if posiblePlaza == "0":
                buscarPlaza = False
            else:
                parking = posiblePlaza.split(" ")
                longitudPlaza = int(parking[1])-int(parking[0])
                contadorPlaza += 1
                if (longitudCoche * 1.5) <= longitudPlaza:
                    if mejorPlaza > longitudPlaza or encontradaPlaza == False:
                        encontradaPlaza = True
                        plaza = contadorPlaza
                        mejorPlaza = longitudPlaza
        if not encontradaPlaza:
            print("NO")
        else:
            print(f"SI {plaza}")