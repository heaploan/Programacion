# Creamos 'aparcar' como un booleano en True
aparcar = True
# Mientras 'aparcar' sea True, se entra en el bucle
while aparcar:
    # Creamos la variable para introducir la longitud del coche
    longitudCoche = int(input())   
    # Creamos una variable para más tarde introducir datos
    mejorPlaza = 0   
    # Creamos esta variable como booleano en False para cambiarla más tarde
    encontradaPlaza = False    
    # Si la longitud del coche es igual a 0
    if longitudCoche == 0:
        # 'aparcar' pasa a ser False
        aparcar = False
    # Mientras no sea False
    else:
        # Buscar plaza con un booleano en True
        buscarPlaza = True        
        # Creamos un contador de plazas
        contadorPlaza = 0      
        # Mientras 'buscarPlaza' sea True
        while buscarPlaza:
            # Introducimos valores a 'posiblePlaza'
            posiblePlaza = input()           
            # Si 'posiblePlaza' es igual a "0" (como texto porque la entrada es texto)
            if posiblePlaza == "0":
                # 'buscarPlaza' es False
                buscarPlaza = False
            # Mientras no sea False
            else:
                # Introducimos los valores separados por espacio en 'parking'
                parking = posiblePlaza.split(" ")                
                # La 'longitudPlaza' es igual al final menos el inicio del tamaño del parking
                # (si fuera al revés, podría ser negativo y no queremos eso)
                longitudPlaza = int(parking[1]) - int(parking[0]) 
                # Se suma 1 a 'contadorPlaza'
                contadorPlaza += 1              
                # Si la 'longitudCoche' por el 50% más es menor o igual a 'longitudPlaza'
                if (longitudCoche * 1.5) <= longitudPlaza:
                    # Si 'mejorPlaza' es mayor a 'longitudPlaza' o 'encontradaPlaza' es igual a False
                    if mejorPlaza > longitudPlaza or not encontradaPlaza:
                        # 'encontradaPlaza' es igual a True
                        encontradaPlaza = True                       
                        # Creamos la variable 'plaza' que guarda el valor de 'contadorPlaza'
                        plaza = contadorPlaza                       
                        # 'mejorPlaza' toma el valor de 'longitudPlaza'
                        mejorPlaza = longitudPlaza  
        # Si 'encontradaPlaza' es False (no se ha encontrado una plaza)
        if not encontradaPlaza:
            # Imprimimos "NO"
            print("NO")
        # En caso de haber encontrado una plaza ('encontradaPlaza' es True)
        else:
            # Imprimimos "SI" y la variable 'plaza' (su contenido)
            print(f"SI {plaza}")
