import random

veces = int(input("Introdueix un numero entre 10 i 50: "))
lista = []

while veces < 10 or veces > 50:
    print("Numero incorrecto, fuera del rango indicado.")
    veces = int(input("Introdueix un numero entre 10 i 50: "))

for i in range(veces):
    numeroAleatorio = random.randint(1,4)
    lista.append(numeroAleatorio)

for numeros in lista:
    print(numeros, end=" ")

for repetidos in lista:
    conteo = 0
    for cantidad in lista:
        if repetidos == cantidad: 
            conteo += 1
            repetido = cantidad

print(f"\nEl numero que ha sortit mes vegades es el {repetido}, amb {conteo} aparicions.")

suma = 0
for cantidad in lista:
    suma += cantidad
media= suma/veces
print(f"La media de los numeros es: {media}")