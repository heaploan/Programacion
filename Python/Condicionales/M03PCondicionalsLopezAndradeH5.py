#he creado la variable jugador1 y jugador2 para guardar la informacion de las palabras que pedimos
jugador1=input("introduce las opciones siguientes (pedra, paper, tisoras): ")
if jugador1=="pedra" or jugador1=="tisoras" or jugador1 =="paper":
    jugador2=input("introduce las opciones siguientes (pedra, paper, tisoras): ")
    if jugador2=="pedra" or jugador2=="tisoras" or jugador2 =="paper":
    #este if es para indicar el empate, que dice que si el valor de jugador1 y jugador2 es igual, entonces es empate.
        if jugador1==jugador2:
            print("Empate")
        #colocandolos elif podemos insertar los valores diferentes posibles
        elif jugador1=="pedra" and jugador2=="paper":
            print("Gana jugador2")
        elif jugador1=="pedra" and jugador2=="tisoras":
            print("Gana jugador1")
        elif jugador1=="paper" and jugador2=="tisoras":
            print ("Gana el jugador2")
        elif jugador1=="paper" and  jugador2=="pedra":
            print ("Gana el jugador1") 
        elif jugador1=="tisoras" and jugador2=="pedra":
            print("Gana el jugador2")
        elif jugador1=="tisoras" and jugador2=="paper":
            print("Gana el jugador1")
    else:
        print("Error, Adios")
else:
    print("Error,Adios")
 