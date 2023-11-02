#creamos la variable pidiendo una frase.
frase=input("Ingresa una frase: ")
#creamos la variable vocales con valor a 0 para llevar conteo de estas
vocales=0
#creamos un for in frase para recorrer el contenido
for i in frase:
    #si dentro del recorrido de frase "i" estan las vocales
    if i in "aeiou":
        #sumar 1 a vocales.
        vocales+=1
#imprimimos la cantidad de vocales.
print(f"La frace tiene {vocales} vocales.")