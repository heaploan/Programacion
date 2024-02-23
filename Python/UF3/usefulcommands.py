import sys
import os
import datetime as dt
#Verifica la longitud del comando.
dictionary = {}

def commandVal(args, n):
    if len(args) == n:
        return True
    else:
        print('ERROR: número de argumentos incorrecto')

#Verifica si el diccionario está vacío o no.
def checkContent():
    if dictionary == {}:
        return True
    return False
    
#Cuenta el largo del contenido del diccionario y lo devuelve.
def getLen():
    if dictionary:
        return len(dictionary)
    return 0

#detectar fin de fichero
def fileEnd():
    EOF = False
    while not EOF:
        #character = file.read(1) 
        #if character == "": #Si el elemento está vacío
            EOF = True

# Función que se encarga de comprobar los digitos del teléfono.
def verTelefon(telefon):
    if len(telefon) == 9 and telefon.isdigit():
            return True
    return False

# Función que se encarga de verificar si el DNI es válido
def verificacioNif(nif):
    letrasValidas = 'TRWAGMYFPDXBNJZSQVHLCKE'
    letra = nif[-1].upper()
    if len(nif) != 9 and (not nif[:-1].isdigit() or not letra.isalpha()):
        print("ERROR: DNI incorrecto")
        return False
    controlLetra = int(nif[:-1]) % 23
    if letra != letrasValidas[controlLetra]:
        print("ERROR: DNI incorrecto")
        return False
    return True

folderName = "./dades"
roomsFile = folderName + "/habitacions.txt"
bookingsFile = folderName + "/reserves.txt"

# funcion que se encarga de crear la carpeta y el archivo si no existen
# dependiendo de lo que se pase de información, habitacio o reserva se crearan archivos de habitacions o reserves
# también dependiendo de la palabra leerá uno u otro archivo y pasará la información correspondiente a dict y devolverá dict.
def loadData(type):
    folderName = "./dades"
    if not os.path.exists(folderName):
        os.mkdir(folderName)
    if type == "habitacio":
        filePath = folderName + "/habitacions.txt"
    elif type == "reserva":
        filePath = folderName + "/reserves.txt"
    dict = {}
    if os.path.exists(filePath):
        f = open(filePath, "r")
        for line in f:
            data = line.strip().split(",")    
            if type == "habitacio":
                if len(data) >= 4:
                    roomNum = data[0]   
                    dict[roomNum] = {'cap': data[1], 'price': data[2], 'disp': data[3]}
            elif type == "reserva":
                if len(data) >= 5:
                    roomNum = data[0]
                    dict[roomNum] = {'name': data[1], 'last': data[2], 'dni': data[3], 'phone': data[4]}   
    return dict

# Calcula si el año es bisiesto
def isLeap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# convierte la fecha a un formato
def convertDate(date):
    d, m, y = date.split('-')
    if d.isdigit() and m.isdigit() and y.isdigit() and 0 < int(y) and 0 < int(m) < 13:
        d, m, y = int(d), int(m), int(y)
        m_days = isLeap(y)
        if 0 < d <= m_days[m-1]:
            start = dt.date(y, m, d).strftime("%d-%m-%Y")
            return start
        else:
            return False
    else:
        return False

# divide la fecha por dia, mes y año y le da formato de datetime
def dateFormat(date):
    date = date.split("-")
    d = int(date[0])
    m = int(date[1])
    y = int(date[2])
    return dt.date(y,m,d)

# mira la mision mas antigua y la imprime.
def transcurseDays(start, today):
    day = today - start
    day = day.days
    if day == 0:
        print("Hoy es la mision mas antigua.")
    else:
        print(f"Han passat {day} dies.")

# Recibe año, coge la información de la fecha en el diccionario, coge el año en concreto
# Compara el que recibe con el obtenido del diccionario e imprime solo las misiones de ese año.
def checkAndListYearMision(year):
    check = 0
    for mision in misiones:
        date = misiones[mision]["fecha"].split("-")
        y = date[2]
        if y == year:
            check += 1
            print(f"{misiones[mision]['fecha']}\t{mision}")
    if check == 0:
        print("El año introducido no tiene misiones.")

# Funcion que mira las misiones durante una semana, la de hoy y la de mañana.
def checkMisionesSemana(today, seven):
    check = 0
    dema = today + dt.timedelta(days = 1)
    for mision in misiones:
        misiondate = dateFormat(misiones[mision]["fecha"])
        if today <= misiondate <= seven:
            check += 1
            if misiondate == today:
                print(f"=> * AVUI *\t{mision}\t{misiones[mision]['lugar']}")
            elif misiondate == dema:
                print(f"=> DEMÀ\t{mision}\t{misiones[mision]['lugar']}")
            else:
                print(f"{misiones[mision]['fecha']} :\t{mision}\t{misiones[mision]['lugar']}")
    if check == 0:
        print("No hay misiones para esta semana.")

# Funcion que mira la fecha más antigua. 
def oldestMision():
    first = 0
    today = dt.date.today()
    for mision in misiones:
        fecha = dateFormat(misiones[mision]["fecha"])
        if first == 0:
            first = 1
            oldest = mision
            oldestdate = fecha
        else:
            if fecha < oldestdate:
                oldest = mision
                oldestdate = fecha


fecha = dt.date(y, m, d).strptime("%d-%m-%Y") #pasa la fecha de string a fecha
fecha = dt.date(y,m,d).strftime("%d-%m-%Y") # pasa pasa la fecha de fecha a string