#Importamos la libreria de random
import random
#creamos la variable veces para introducir un numero entre el rango mencionado.
veces = int(input("Introdueix un numero entre 10 i 50: "))
#creamos una lista para luego introducir sus valores. 
lista = []
#creamos el while para que mientras veces sea menor a 10 o mayor a 50 muestre el mensaje de error y vuelva a pedir el rango.
while veces < 10 or veces > 50:
    print("Numero incorrecto, fuera del rango indicado.")
    veces = int(input("Introdueix un numero entre 10 i 50: "))
#creamos este for para que el valor que se coloque en veces, agregue el valor random entre 1 y 4 a lista.
for i in range(veces):
    numeroAleatorio = random.randint(1,4)
    lista.append(numeroAleatorio)
#creamos este for para que los numeros dentro de la lista se muestren con espacios y no la lista en si.
for numeros in lista:
    print(numeros, end=" ")
#creamos este for para contar los numeros repetidos en lista
for repetidos in lista:
    conteo = 0
    #creamos este for para que recorra los valores dentro de lista
    for cantidad in lista:
        #si repetidos es igual que cantidad, se suma 1 a conteo
        if repetidos == cantidad: 
            conteo += 1
            #creamos la variable repetido guardando el valor de cantidad. 
            repetido = cantidad
#imprimimos el numero repetido y las veces que se repite. 
print(f"\nEl numero que ha sortit mes vegades es el {repetido}, amb {conteo} aparicions.")
#creamos este for para calcular la media de los valores dentro de la lista. 
suma = 0
for cantidad in lista:
    suma += cantidad
media= suma/veces
#imprimimos la media.
print(f"La media de los numeros es: {media}")