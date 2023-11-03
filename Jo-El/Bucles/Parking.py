longitud=int(input())
eleccion=0
contador=0
inicio=-1
longitud_sitio=0
minimo=9000000
entrada=input()
while longitud != 0:
    contador+=1
    while longitudEspacio != 0:
        datos=entrada.split()
        inicio=int(datos[0])
        final=int(datos[1])
        if inicio != 0:
            longitudEspacio=final-inicio
            if longitudEspacio>longitud*1.5:
                if minimo > longitudEspacio:
                    minimo=longitudEspacio
                    eleccion=contador
    entrada=input()
if minimo == 9000000:
    print("NO")
else:
    print(f"SI {eleccion}")
        
    