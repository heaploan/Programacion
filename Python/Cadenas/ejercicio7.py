#creamos la variable z con valor True
z=True
#mientras z sea True entramos en bucle
while z == True:
    #creamos la variable numero con input
    numero=input("Escribe un numero entero positivo: ")
    #si el contenido de numero es numerico
    if numero.isnumeric():
        #el input de numero se convierte en int(input())
        numero=int(numero)
        #si numero es mayor a 0
        if numero > 0:
            #si el contenido de numero dividido entre 1 es igual a 0
            if numero % 1 == 0:
                #la condición se cumple, entonces imprimimos el mensaje
                print("¡Muy bien, me has hecho caso!")
                #z deja de ser True y salimos del bucle
                z=False
            else:
                print("No has puesto un numero entero.")
        else: 
            print("El numero no es entero positivo")            
    else:
        print("El numero no es entero positivo.")