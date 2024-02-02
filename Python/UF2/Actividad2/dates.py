# importamos la biblioteca de datetime.
import datetime
# Importamos la biblioteca locale para cambiar el idioma de la date que mostraremos
import locale
import datetime
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
    dia = int(date[0])
    mes = int(date[1])
    diaActual = datetime.date.today().day
    mesActual = datetime.date.today().month
    actualYear  = datetime.date.today().year
    if mesActual > mes or (diaActual >= dia and mesActual >= mes):
        actualYear  += 1
    return (f"El proper aniversari es: {datetime.date(actualYear , mes, dia).strftime('%d/%m/%Y')}")

# c)
# Con esta funcion calcularemos cuantos días quedan para el siguiente cumpleaños.
def quantFalta(fecha):
    # reemplazamos el texto de la funcion de proper aniersari y nos quedamos solo con la fecha, creando una lista de esta dividida por "/".
    fecha = properAniversari(fecha).replace("El proper aniversari es: ", "").split("/")
    # Guardamos en cada posición el día, el mes y el año separado por /
    day = int(fecha[0])
    month = int(fecha[1])
    year = int(fecha[2])
    # Guardamos los valores del día actual utilizando la funcion con su metodo de today.
    actualDay = datetime.date.today().day
    actualMonth = datetime.date.today().month
    # Si el dia actual es igual al dia y el mes actual es igual al mes, es la fecha indicada!
    if actualDay == day and actualMonth == month:
        return "¡Felicidades, Es tu cumpleaños!"
    else:
        # en caso de no ser así, calculamos los días llamando la libreria de datetime.date especificando el año, mes y dia
        # restamos eso con el día actual con el metodo .today()    
        daysLeft = datetime.date(year, month, day) - datetime.date.today()
        return f"Faltan {daysLeft.days} dias para tu cumpleaños." #ponemos el .days para pedir solo días y que no ponga nada más.
# d) 
# En esta función miramos si el mes proporcionado coincide con el mes actual y devolvemos un bool.
def aniversari(date):
    date = date.split("/")
    month = int(date[1])
    actualMonth = datetime.date.today().month
    if month == actualMonth:
        return True
    else: 
        return False

