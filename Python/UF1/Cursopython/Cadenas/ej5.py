# Escribir un programa que pida al usuario que introduzca una frase en la consola
# y una vocal en minúscula, después muestre por pantalla la misma frase
# pero con la vocal introducida en mayúscula.
frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ")
# En este print reemplazamos la vocal llamándola primero y luego convirtiéndola en mayúscula. 
print(frase.replace(vocal, vocal.upper()))
