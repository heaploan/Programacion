import datetime as dt
from datetime import datetime

misiones = {}

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
    if not checkMissions(command[1]):
        misiones.pop(command[1])
        print("Mision eliminada.")
    else:
        print("ERROR: No hay misiones registradas")

def checkYear(command):
    if command[1] == '' or command[1] == ' ':
        print("ERROR: Año no indicado")
    else:
        if misiones == {}:
            print("ERROR: no hay misiones registradas.")
        else:
            año = command
            encontrado = True
            for code, info in misiones.items(): 
                print(f"AÑO: {command[1]}")   
                print(f"{info['fecha']} {code}")
            if not encontrado:
                print(f"No ay misiones con fecha '{año}' registradas")

