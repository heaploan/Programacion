from biblioteca import * 

fechaActual = datetime.today()
# Para darle el formato de dia-mes-año y no salgan las horas
fechaActual2 = datetime.strftime(fechaActual,'%Y-%m-%d')
diaActual = datetime.today().day
mesActual = datetime.today().month
añoActual = datetime.today().year
iniciPrestec = fechaActual.date()
ahora = fechaActual.date()
fiPrestec = ahora + dt.timedelta(days=15)
print(fiPrestec)

# fechaInicio = fechaActual2
# diaFinal = diaActual + 15 
# if diaFinal > 31:
#     diaFinal -= 31
# else:
#     diaFinal = diaFinal
# mesFinal = mesActual
# if mesFinal > 12:
#     mesFinal == 1
#     añoActual += 1
# else:
#     mesFinal = mesFinal

# fechafinal = añoActual, mesFinal, diaFinal
# fechaFinal = ()

# print(fechaActual2)
# print(fechafinal)
