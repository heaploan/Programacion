# Recibe un parámetro 'any' y calcula si es bisiesto
# Si es divisible por 4 y no lo es por 100 es bisiesto.
def EsBisiesto(any):
    if any % 4 == 0 and any % 100 != 0:
        return True
    else:
        return False

resultado = EsBisiesto(2020)
print(resultado)