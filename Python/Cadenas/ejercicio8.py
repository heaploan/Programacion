#creamos la variable frase con input
frase=input("Introduce una frase: ")
#creamos la variable consonante con "" sin espacio para indicar que es texto el contenido
con=""
#creamos la variable for para recorrer los valores de frase
for i in frase:
    #si los valores de frase "i" no son aeiou
    if i.lower() not in "aeiou":    
        #se le suman los valores de frase "i" a con
        con+=i
#se imprime con y se mostrarían solo las consonantes.
print(con)