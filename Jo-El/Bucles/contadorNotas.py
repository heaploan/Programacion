#creamos la variable de notas
notas = 0
#creamos lista
lista = []
#creamos la variable para sumar las notas totales
notasTotales = 0
#mientras notas sea diferente a -1
while notas != -1:
    #pedira las notas
    notas = int(input())
    #si notas es igual o mayor a 0 e igual o menor a 10
    if 0 <= notas <= 10:
        #agregamos los valores de notas a lista
        lista.append(notas)
        #sumamos 1 a notas Totales.
        notasTotales += 1
#creamos la variable suma para guardar el calulo
suma = 0
#si cantidad la encontramos en lista
for cantidad in lista:
    #sumamos a suma cantidad
    suma += cantidad
#creamos la variable de la media y hacemos la division de suma entre las notasTotales    
media= suma/notasTotales
#para mirar el contenido que esta dentro del rango de excelentes o las notas que pongamos se hace asi:
excelentes = len([nota for nota in lista if nota in [9, 10]])
notables = len([nota for nota in lista if nota in [7, 8]])
bien = len([nota for nota in lista if nota == 6])
suficientes = len([nota for nota in lista if nota == 5])
insuficientes = len([nota for nota in lista if nota in [4, 3]])
muyDeficientes = len([nota for nota in lista if 0 <= nota <= 3])
print(f"NOTES: {notasTotales} MITJANA: {media} E: {excelentes} N: {notables} B: {bien} S: {suficientes} I: {insuficientes} MD: {muyDeficientes}")