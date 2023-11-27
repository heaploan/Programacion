#creamos random con el import para que genere un numero random.
import random
numeroAleatorio = random.randint(1, 50)
#esta variable es para los intentos actuales.
intentoActual = 1
#esta es el maximo de intentos
maxIntentos = 5
#esta variable es para el int,input y que se guarde el valor itroducido.
numeroIntroducido = 0
#mientras intentoActual sea menor o igual a maxIntentos seguiremos preguntando.
while intentoActual <= maxIntentos:
    numeroIntroducido = int(input("Intenta adivinar el numero en un rango del 1 al 50: "))
    #si numeroIntroducido es mayor que numero aleatorio diremos esto.
    if numeroIntroducido > numeroAleatorio:
        #restaremos el maxIntentos e intentoActual para obtener los intentos restantes.
        print(f"Numero mayor, intenta de nuevo. Te quedan: {maxIntentos - intentoActual}.")
    #si numeroIntroducido es menor que numeroAleatorio diremos esto.
    elif numeroIntroducido < numeroAleatorio:
        print(f"Numero menor, intenta de nuevo. Te quedan: {maxIntentos - intentoActual}.")
    #con este else si se acierta se termina el bucle.
    else:
        print("Se te acabaron los intentos.")
    #con esta variable se le suma 1 a intentoActual cada vez que se ingresa un número.
    intentoActual += 1
#Con este if se avisa que se ha adivinado el número aleatorio.
if numeroIntroducido == numeroAleatorio:
    print("¡Felicidades, has acertado!")
