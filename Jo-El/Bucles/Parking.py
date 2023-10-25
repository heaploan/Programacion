longitud_coche=int(input())
caso=1
while longitud_coche !=0:
    inicio_espacio=0
    espacio_final=0
    espacio_libre=0
    espacio_pequeño=-1
    n_espacio=1
    longitud_espacio=-1
    while longitud_espacio !=0:
        entrada=input().split()
        inicio_espacio=int(entrada[0])
        espacio_final=int(entrada[1])
        longitud_espacio=inicio_espacio
        if longitud_espacio!=0:
            longitud_espacio=espacio_final-inicio_espacio
            if longitud_espacio>=longitud_coche*1.5:
                if espacio_pequeño==-1 or longitud_espacio<espacio_pequeño:
                    espacio_pequeño=longitud_espacio
                    espacio_elegido=n_espacio
                    n_espacio+=1
            if espacio_pequeño==-1:
                print("NO")
            else:
                print(f"SI {espacio_elegido}")
            longitud_coche=int(input())