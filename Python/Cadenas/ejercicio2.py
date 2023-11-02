#Creamos la cadena con un input.
cadena=input("Introduce una frase: ")
#creamos el input para caracter. 
caracter=input("Introduce un caracter: ")
#Mientras la longitud de caracter sea diferente a 1
while len(caracter) != 1:
    #imprimira el error conforme que ha introducido mas de un caracter. 
    print("Has introducido mas de un caracter.")
    #vuelve a pedir un caracter.
    caracter=input("Introduce un caracter: ")
#creamos la variable veces para hacer el conteo de veces que aparece el caracter en la cadena.
veces=0
#creamos for para recorrer la variable cadena.
for i in cadena:
    #si el caracter es igual a i
    if caracter == i:
        #se suma 1 a veces
        veces+=1
#imprimimos el caracter y la suma de veces.
print(f"El caracter {caracter} aparece {veces} veces.")