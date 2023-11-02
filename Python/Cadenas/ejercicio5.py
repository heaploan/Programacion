#creamos input de frase.
frase=input("Introduce una frase: ")
#creamos mitad para que coja los valores de frase 
mitad=""
#creamos variable n con valor de 0
n = 0
#creamos for en frase
for i in frase:
    #si n es igual a 0
    if n == 0:
        #a mitad se le agrega i que coje los valores de frase
        mitad += i
        #entonces n = 1, que lo que hace es ir cogiendo un valor si, uno no.
        n=1
    else:
        n=0
#imprimimos la variable mitad para mostrar lo que se ha hecho.
print(mitad)