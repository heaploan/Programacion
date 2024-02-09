import os
import validator as v
# Este modulo está hecho para gestionar los ficheros y su contenido.
folderName = "./dades"
roomsFile = folderName + "/habitacions.txt"
bookingsFile = folderName + "/reserves.txt"

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
                        dict[roomNum] = {'name': data[1], 'lastName': data[2], 'dni': data[3], 'phone': data[4]}   
    return dict

def isRoomInFile(roomNum):
    # Abrimos el archivo en modo de lectura
    if os.path.exists(roomsFile):
        f = open(roomsFile, "r")
        # Iteramos sobre cada línea del archivo
        for line in f:
            # Dividimos la línea en sus partes separadas por comas
            data = line.strip().split(',')
            # Verificamos que la línea tenga al menos un elemento, que el primer elemento sea un número y que coincida con el número de habitación buscado
            if len(data) >= 1 and data[0].isdigit() and int(data[0]) == roomNum:
                # Si encontramos la habitación, cerramos el archivo y devolvemos True
                f.close()
                return True
        # Si no encontramos la habitación, cerramos el archivo y devolvemos False
        f.close()
    return False

def addRoomToFile(roomNum, cap, price):
    if not os.path.exists(folderName):
        os.mkdir(folderName)
    if not os.path.exists(roomsFile):
        f = open(roomsFile, "a")
        f.write(f"{roomNum},{cap},{price},DISPONIBLE\n")
        f.close()
    elif os.path.exists(roomsFile):  # Crea el archivo si no existe
        if not isRoomInFile(int(roomNum)):
            f = open(roomsFile, "a")
            f.write(f"{roomNum},{cap},{price},DISPONIBLE\n")
            f.close()



def isbookingInFile(roomNum):
    # Abrimos el archivo en modo de lectura
    f = open(bookingsFile, "r")
    # Iteramos sobre cada línea del archivo
    for line in f:
        # Dividimos la línea en sus partes separadas por comas
        data = line.strip().split(',')
        # Verificamos que la línea tenga al menos un elemento, que el primer elemento sea un número y que coincida con el número de habitación buscado
        if len(data) >= 1 and data[0].isdigit() and int(data[0]) == roomNum:
            # Si encontramos la habitación, cerramos el archivo y devolvemos True
            f.close()
            return True
    # Si no encontramos la habitación, cerramos el archivo y devolvemos False
    f.close()
    return False

def addBookingToFile(roomNum, name, lastName, dni, phone):
    if not os.path.exists(folderName):
        os.mkdir(folderName)
    if not os.path.exists(bookingsFile):  # Crea el archivo si no existe   
        f = open(bookingsFile, "w")
        f.write(f"{roomNum},{name},{lastName},{dni},{phone}\n")
        f.close()
    elif os.path.exists(bookingsFile):
        if isRoomInFile(int(roomNum)):
            if not isbookingInFile(int(roomNum)):
                if v.verTelefon(phone):
                    f = open(bookingsFile, "a")
                    f.write(f"{roomNum},{name},{lastName},{dni},{phone}\n")
                    f.close()

def verAvailability(roomNum):
    rooms = loadData("habitacio")
    if roomNum in rooms:
        status = rooms[roomNum]['disp']
        if status == "DISPONIBLE":
            return True
        else:
            print("ERROR: La habitación no está disponible para reservas")
            return False
    else:
        print("ERROR: la habitación no existe")
        
def updateRoomStatus(roomNum):
    f = open(roomsFile, "r")
    lines = f.readlines()
    f = open(roomsFile, "w")
    for line in lines:
        data = line.strip().split(',')
        if data[0] == roomNum:
            f.write(f"{roomNum},{data[1]},{data[2]}, OCUPADA\n")
        else:
            f.write(line)
    f.close()



