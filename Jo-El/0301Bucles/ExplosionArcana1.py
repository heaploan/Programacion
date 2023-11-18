#creamos variable ini con su input
ini =int(input())
#creamos la variable q con su input
q = int(input())
#creamos variable dañoTotal para luego guardar los calculos.
dañoTotal = 0
#creamos for para el rango de q
for i in range(q):
    #creamos variable de dañoActual para calcular ini + i(que es lo que se mueve y lee las veces que se repetirían los daños) * ini 
    dañoActual = ini + (i * ini)
    #variable dañoTotal sumando el daño actual
    dañoTotal += dañoActual
print(dañoTotal)
