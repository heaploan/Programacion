#creamos aparcar como booleano en True
aparcar = True
#mientras aparcar sea True se entra en el bucle
while aparcar:
    #creamos la variable para introducir la longitud del coche.
    longitudCoche = int(input())
    #creamos una variable para mas tarde introducir datos.
    mejorPlaza = 0
    #creamos esta variable como booleano en False para mas tarde cambiarlo.
    encontradaPlaza = False
    #si longitudCoche es igual a 0
    if longitudCoche == 0:
        #aparcar pasa a ser falso.
        aparcar = False
    #mientras no sea falso
    else:
        #buscar plaza con booleano en True
        buscarPlaza = True
        #creamos contador de plazas
        contadorPlaza = 0
        #mientras buscarPlaza sea True
        while buscarPlaza:
            #introducimos valores a posiblePlaza
            posiblePlaza = input()
            #si posiblePlaza es igual a 0 en texto (porque le input es texto)
            if posiblePlaza == "0":
                #buscarPlaza es falso
                buscarPlaza = False
            #mientras no sea falso
            else:
                #introducimos los valores en split a parking
                parking = posiblePlaza.split(" ")
                #la longitudPlaza es igual al final menos el inicio del tamaño del parking (si fuera al revés, podría ser negativo el valor y no queremos eso.)
                longitudPlaza = int(parking[1])-int(parking[0])
                #se suma 1 a contadorPlaza
                contadorPlaza += 1
                #si la longitudCoche por 50% mas es menor o igual a longitudPlaza
                if (longitudCoche * 1.5) <= longitudPlaza:
                    #si mejorPlaza es mayor a LongitudPlaza o encontradaPlaza es igual a falso
                    if mejorPlaza > longitudPlaza or encontradaPlaza == False:
                        #encontrada plaza es igual a verdadero
                        encontradaPlaza = True
                        #creamos la variable plaza que guarda el valor del contadorPlaza
                        plaza = contadorPlaza
                        #mejor plaza coge el valor de longitudPlaza
                        mejorPlaza = longitudPlaza
        #si encontradaPlaza es falso (no se ha encontrado)
        if not encontradaPlaza:
            #imprimimos NO
            print("NO")
        #en caso de haber encontrado plaza (encontradaPlaza es True)
        else:
            #imprimimos SI y la variable plaza (el contenido de esta)
            print(f"SI {plaza}")