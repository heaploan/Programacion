import datetime
from datetime import date

# Para darle el formato de dia-mes-año y no salgan las horas
fechaActual = datetime.date.today()
fechaActual2 = datetime.strftime(fechaActual,'%Y-%m-%d')
diaActual = datetime.day().day
mesActual = datetime.month().month
añoActual = datetime.year().year


print(fechaActual2)
