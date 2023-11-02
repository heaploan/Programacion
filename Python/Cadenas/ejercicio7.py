z=True
while z == True:
    numero=input("Escribe un numero entero positivo: ")
    if numero.isnumeric():
        numero=int(numero)
        if numero > 0:
            if numero % 1 == 0:
                print("¡Muy bien, me has hecho caso!")
                z=False
            else:
                print("No has puesto un numero entero.")
        else: 
            print("El numero no es entero positivo")            
    else:
        print("El numero no es entero positivo.")