z=True
while z == True:
    numero=input("Escribe un numero entero positivo: ")
    #si numero es numerico
    if numero.isnumeric():
        #el input de la variable numero se convierte en int(input())
        numero=int(numero)
        #si numero es mayor a 0
        if numero > 0:
            #si la division de numero 
            if numero % 1 == 0:
                print("¡Muy bien, me has hecho caso!")
                z=False
            else:
                print("No has puesto un numero entero.")
        else: 
            print("El numero no es entero positivo")            
    else:
        print("El numero no es entero positivo.")