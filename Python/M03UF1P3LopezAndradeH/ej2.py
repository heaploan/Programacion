#Importamos la librería de random
import random
#creamos la variable donde pediremos las veces a tomar en cuenta.
veces = int(input("Introdueix un numero entre 10 i 50: "))
#Creamos lista para rellenarla mas tarde con datos.
lista = []
#Mientras veces este en un rango de 10 a 50 se llevará a cabo el bucle
while veces < 10 or veces > 50:
    #En caso de no ser así, pedimos que vuelva a introducir un numero mostrando un mensaje de error.
    print("Numero incorrecto, fuera del rango indicado.")
    veces = int(input("Introdueix un numero entre 10 i 50: "))
#Creaamos este for para añadir los numeros random a la lista.
for i in range(veces):
    numeroAleatorio = random.randint(1,4)
    lista.append(numeroAleatorio)
#Creamos este for para encontrar el numero que se repite
for numeros in lista:
    print(numeros, end=" ")
#creamos este for para contar las veces que se repite el numero
for repetidos in lista:
    conteo = 0
    for cantidad in lista:
        if repetidos == cantidad: 
            conteo += 1
            repetido = cantidad
#Imprimimos el numero repetido y las veces que este se ha repetido.
print(f"\nEl numero que ha sortit mes vegades es el {repetido}, amb {conteo} aparicions.")
#Creamos esta variable para almacenar los datos de suma después.
suma = 0
#creamos este ultimo for para contar la media de todos los numeros dentro de la lista. 
for cantidad in lista:
    suma += cantidad
media= suma/veces
#imprimimos la media.
print(f"La media de los numeros es: {media}")