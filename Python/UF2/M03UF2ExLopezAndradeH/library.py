import datetime as dt
from datetime import datetime, timedelta

misiones = {}

#Comprobamos la longitud del comando, si no es correcta, mostrará el error.
def checkParametros(command, n):
    if len(command) == n:
        return True
    else:
        print(f"ERROR: Número de argumentos incorrecto.")
        return False

#Guardamos los valores en el diccionario misiones.
def missionsUpdate(title, place, date):
    misiones[title] = {'lugar': place, 
                       'fecha': date}

#miramos que la mision indicada esté en el diccionario
def checkMissions(command):
    if command not in misiones:
        return True
    else:
        return False

#recibimos la fecha en string y le damos formato de fecha.
def checkDate(command):
    if checkParametros(command, 4):
        if checkMissions(command[1]):
            d_m_y = command[3].split('/')
            d = int(d_m_y[0])
            m = int(d_m_y[1])
            y = int(d_m_y[2])
            fechaDeseada = dt.date(y, m, d)
            selectedDate = fechaDeseada.strftime("%d-%m-%Y")
            missionsUpdate(command[1], command[2], selectedDate)
            print('Mision registrada')
        else:
            print('ERROR: Ya existe una misión con ese título.')
    
def titleCheck(command):
    if command not in misiones:
        return True
    else:
        return False
        
def missionDelete(command):
    if checkParametros(command, 2):        
        if not checkMissions(command[1]):
            misiones.pop(command[1])
            print("Mision eliminada.")
        else:
            print("ERROR: No hay misiones registradas")

def checkYear(command):
    if checkParametros(command, 2):
        if command[1] == '' or command[1] == ' ':
            print("ERROR: Año no indicado")
        else:
            targetYear = int(command[1])
            matchingMissions = []
            if misiones == {}:
                print("ERROR: no hay misiones registradas.")
            else:
                for code, info in misiones.items():
                    missionYear = int(info['fecha'].split('-')[2])
                    if missionYear == targetYear:
                        matchingMissions.append((info['fecha'], code))
                if matchingMissions:
                    print(f"AÑO: {command[1]}")
                    for date, title in matchingMissions:
                        print(f"{date} {title}")
                else:
                    print(f"No hay misiones con fecha '{command[1]}' registradas")

def checkWeek(command):
    if checkParametros(command, 1):
    # Obtener la fecha actual
        currentDate = datetime.now().date()
    # Calcular la fecha límite para la próxima semana
        limitDate = currentDate + timedelta(days=7)
    # Mostrar las misiones en el rango de 7 días a partir de la fecha actual
        for title, missionInfo in misiones.items():
            missionDate = datetime.strptime(missionInfo['fecha'], "%d-%m-%Y").date()
        # Verificar si la misión está en el rango de 7 días a partir de la fecha actual
            if currentDate <= missionDate <= limitDate:
                print(f"{title}: {missionInfo['fecha']} en {missionInfo['lugar']}")

