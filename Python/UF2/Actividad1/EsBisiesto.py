# Recibe un parámetro 'year' y calcula si es bisiesto
# Si es divisible por 4 y no lo es por 100 es bisiesto.
def EsBisiesto(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

result = EsBisiesto(2020)
print(result)