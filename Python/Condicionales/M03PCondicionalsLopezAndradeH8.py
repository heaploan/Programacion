
#Aqui pido los costados del triángulo usando float para que puedan tener decimales.
a=float(input("Inserte la primer medida para un costado de un triángulo: "))
b=float(input("Inserte la segunda medida para un costado de un triángulo: "))
c=float(input("Inserte la tercer medida para un costado de un triángulo: "))

#Con estos if es para verificar los triángulos sumando dos de sus lados.
if a+b>c and a+c>b and b+c>a:
    #este if es para saber si sus tres lados son iguales, entonces es un triángulo equilátero
    if a==b and b==c:
        print("El triángulo es equilátero.")
    #este es si dos de sus ángulos son iguales entonces es un isósceles.
    elif a==b or b==c or a==c:
        print("El triángulo es isósceles.")
    #este else es para decir que si todos los lados son diferentes, entonces es escaleno
    else:
        print("El triángulo es escaleno.")
#con este else es para indicar que si ninguna de las condiciones se cumple, entonces no es un triángulo válido.
else:
    print("No es un triángulo válido.")