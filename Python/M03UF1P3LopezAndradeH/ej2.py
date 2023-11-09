<<<<<<< HEAD
#Importamos la libreria de random
import random
#creamos la variable veces para introducir un numero entre el rango mencionado.
veces = int(input("Introdueix un numero entre 10 i 50: "))
#creamos una lista para luego introducir sus valores. 
lista = []
#creamos el while para que mientras veces sea menor a 10 o mayor a 50 muestre el mensaje de error y vuelva a pedir el rango.
=======
#Importamos la librería de random
import random
#creamos la variable donde pediremos las veces a tomar en cuenta.
veces = int(input("Introdueix un numero entre 10 i 50: "))
#Creamos lista para rellenarla mas tarde con datos.
lista = []
#Mientras veces este en un rango de 10 a 50 se llevará a cabo el bucle
>>>>>>> refs/remotes/origin/main
while veces < 10 or veces > 50:
    #En caso de no ser así, pedimos que vuelva a introducir un numero mostrando un mensaje de error.
    print("Numero incorrecto, fuera del rango indicado.")
    veces = int(input("Introdueix un numero entre 10 i 50: "))
<<<<<<< HEAD
#creamos este for para que el valor que se coloque en veces, agregue el valor random entre 1 y 4 a lista.
for i in range(veces):
    numeroAleatorio = random.randint(1,4)
    lista.append(numeroAleatorio)
#creamos este for para que los numeros dentro de la lista se muestren con espacios y no la lista en si.
for numeros in lista:
    print(numeros, end=" ")
#creamos este for para contar los numeros repetidos en lista
=======
#Creaamos este for para añadir los numeros random a la lista.
for i in range(veces):
    numeroAleatorio = random.randint(1,4)
    lista.append(numeroAleatorio)
#Creamos este for para encontrar el numero que se repite
for numeros in lista:
    print(numeros, end=" ")
#creamos este for para contar las veces que se repite el numero
>>>>>>> refs/remotes/origin/main
for repetidos in lista:
    conteo = 0
    #creamos este for para que recorra los valores dentro de lista
    for cantidad in lista:
        #si repetidos es igual que cantidad, se suma 1 a conteo
        if repetidos == cantidad: 
            conteo += 1
            #creamos la variable repetido guardando el valor de cantidad. 
            repetido = cantidad
<<<<<<< HEAD
#imprimimos el numero repetido y las veces que se repite. 
print(f"\nEl numero que ha sortit mes vegades es el {repetido}, amb {conteo} aparicions.")
#creamos este for para calcular la media de los valores dentro de la lista. 
=======
#Imprimimos el numero repetido y las veces que este se ha repetido.
print(f"\nEl numero que ha sortit mes vegades es el {repetido}, amb {conteo} aparicions.")
#Creamos esta variable para almacenar los datos de suma después.
>>>>>>> refs/remotes/origin/main
suma = 0
#creamos este ultimo for para contar la media de todos los numeros dentro de la lista. 
for cantidad in lista:
    suma += cantidad
media= suma/veces
#imprimimos la media.
print(f"La media de los numeros es: {media}")