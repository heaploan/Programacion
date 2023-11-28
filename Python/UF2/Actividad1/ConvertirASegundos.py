# Recibe tres parámetros y calcula cuantos segundos son en total
# Multiplica horas * 3600 (total de segundos por hora)
# Multiplica minutos por 60 (total de segundos por minuto)
def Convertir_A_Segons(h, m, s):
    s += h * 3600
    s += m * 60
    return s

SegonsTotals = Convertir_A_Segons(5,2,2)
print(SegonsTotals)