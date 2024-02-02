#para restar días a una fecha.
import datetime as dt

#para restar días a una fecha: 
ahora = dt.datetime.today().date()
print(ahora)
ayer = ahora - dt.timedelta(days=1)
print(f"ayer: {ayer}")

#para sumar días a una fecha.
ahora = dt.datetime.today().date()
print(ahora)
mañana = ahora + dt.timedelta(days=1)
print(f"mañana: {mañana}")

#para dar formato a la fecha de hoy:
formatoFecha = dt.date.today().strftime("%d/%m/%Y")
print(formatoFecha)

# Ejemplo de entrada
entrada = "27-03-2024"
# Dividir la entrada por '-' y en caso de ser con '/' se cambiaría el símbolo a '/'
d_m_y = entrada.split('-')
d = int(d_m_y[0])
m = int(d_m_y[1])
y = int(d_m_y[2])
# Crear un objeto datetime.date con el nuevo formato
#dt.date (datetime.date) solo da información día, mes, año sin incluir horas, minutos y segundos.
selectedDate = dt.date(d, m, y)
# dar formato a la fecha deseada
fechaFormateada = selectedDate.strftime("%Y/%m/%d")
print(f"Fecha formateada: {fechaFormateada}")
