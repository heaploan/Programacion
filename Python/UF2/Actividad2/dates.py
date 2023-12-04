# importamos la biblioteca de datetime.
import datetime
# Importamos la biblioteca locale para cambiar el idioma de la date que mostraremos
import locale
from datetime import date
# Para cambiar el idioma de la date usamos la biblioteca de locale
# se pone primero locale, ponemos setlocale para definirlo
# dentro del parentesis se pone lo siguiente.
locale.setlocale(locale.LC_ALL,'ca_ES.UTF-8')

# a)
# Creamos la funcion 'avui'
# nos regresará la date con formato %d %B %Y y lo traducioms a catalán
def avui():
    return datetime.date.today().strftime("Avui és %d de %B del %Y");

# b)
# Creamos la funcion 'properAniversari' 
# miraremos cuanto falta para el proximo cumpleaños
def properAniversari(date):
    date = date.split("/")
    dia = date[0]
    mes = date[1]
    año = date[2]
    diaActual = datetime.date.today().day
    mesActual = datetime.date.today().month
    añoActual = datetime.date.today().year
    if diaActual >= dia and mesActual >= mes:
        añoActual += 1
    return (f"El proper aniversari es {datetime.date(añoActual, mes, dia).strftime("%d/%m/%Y")}")
