# Solicita al usuario que ingrese la cantidad de caramelos
caramels = int(input())
# Solicita al usuario que ingrese la cantidad de niños
nens = int(input())
# Calcula el sobrante de caramelos después de distribuir entre los niños
sobren = caramels % nens
# Imprime el resultado, que es la cantidad de caramelos sobrantes
print(sobren)
