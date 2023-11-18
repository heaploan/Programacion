#ejercicios 1, 2 y 3
num1= int(input("Introduce un número entero entre el 1 y el 100: "))
num2= int(input("Introduce otro número entero entre el 1 y el 100: "))
#la f es para llamar la variable y se pone al principio pero fuera de las comillas, las variables
#se ponen en {} para ser detectadas como tal.
print(f"El primer numero introducido es: {num1}")
print(f"El segundo numero introducido es: {num2}")
#he colocado el rango de los numeros que se piden para que el programa envie el mensaje.
if 1<=num1<=100:
    print("El numero esta dentro del rango indicado!")
#una vez colocado el rango esto indica que si no esta dentro, salte el mensaje indicando el error.
else: 
    print("No esta dentro del rangoindicado!")
if 1<=num2<=100:
    print("El numero esta dentro del rango indicado!")
else:
    print("No esta dentro del rango indicado!")
#el % es para indicar si el residuo de la division entre dos es 0 e indique que es un numero par
#los == juntos es para indicar que es igual, un solo = es una asignacion, no comparacion.
if num2 % 2==0:
    print("El segundo numero es par")
#el != es para saber si el residuo de la division entre 2 es diferente a 0 es un numero impar
if num1 % 2!=0:
    print("El primer numero es impar")
if num2 % 2!=0:
    print("El primer numero es impar")