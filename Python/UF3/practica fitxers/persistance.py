import os
import validator as v

# Este modulo está hecho para gestionar los ficheros, su creación y su contenido.

folderName = "./dades"
roomsFile = folderName + "/habitacions.txt"
bookingsFile = folderName + "/reserves.txt"

# Esta función está creada para leer los archivos y pasarel contenido al diccionario
# Si no existe la carpeta, la crea
# Finalmente devuelve el diccionario ya con los datos introducidos en este
# También depende de qué mención se haya hecho en la linea de comandos, si 'habitacio' o 'reserva', leerá los respectivos. 
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
                    dict[int(roomNum)] = {'cap': int(data[1]), 'price': float(data[2]), 'disp': data[3]}
            elif type == "reserva":
                if len(data) >= 5:
                    roomNum = data[0]
                    dict[int(roomNum)] = {'name': data[1], 'last': data[2], 'dni': data[3], 'phone': data[4]}   
        f.close()
    return dict

#Comprueba si la habitación está guardada en el archivo 'habitacions'
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

# Agrega la habitación al archivo de texto separado por comas.
# Si no existe la carpeta, la crea, si tampoco existe el archivo, lo crea y añade la información
def addRoomToFile(roomNum, cap, price):
    if not os.path.exists(folderName):
        os.mkdir(folderName)
    if not os.path.exists(roomsFile):
        f = open(roomsFile, "a")
        f.write(f"{roomNum},{cap},{price},DISPONIBLE\n")
        f.close()
    elif os.path.exists(roomsFile):  # Crea el archivo si no existe
        if not isRoomInFile(roomNum):
            f = open(roomsFile, "a")
            f.write(f"{roomNum},{cap},{price},DISPONIBLE\n")
            f.close()

# Verifica si la reserva está en el archivo
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

# Agrega la reserva al archivo de texto, si la carpeta y el archivo no existen, los crea
def addBookingToFile(roomNum, name, lastName, dni, phone):
    if not os.path.exists(folderName):
        os.mkdir(folderName)
    if not os.path.exists(bookingsFile):  # Crea el archivo si no existe   
        if isRoomInFile(int(roomNum)):
            f = open(bookingsFile, "a")
            f.write(f"{roomNum},{name},{lastName},{dni},{phone}\n")
            f.close()
    elif os.path.exists(bookingsFile):
        if isRoomInFile(int(roomNum)):
            if not isbookingInFile(int(roomNum)):
                if v.verificacioNif(dni):
                    if v.verTelefon(phone):
                        f = open(bookingsFile, "a")
                        f.write(f"{roomNum},{name},{lastName},{dni},{phone}\n")
                        f.close()
                else:
                    print("ERROR: DNI incorrecto")

# Verifica la disponibilidad de la habitación, en caso de estar disponible, devolverá True, en caso contrario, False
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
        print("ERROR: No existe una habitación con el número indicado")

# Actualiza el estado de la habitación dependiendo de lo que se le introduzca ('DISPONIBLE', 'OCUPADA', 'BRUTA')
def updateRoomStatus(roomNum,newStatus):
    f = open(roomsFile, "r")
    lines = f.readlines()
    f.close()
    f = open(roomsFile, "w")
    for line in lines:
        data = line.strip().split(',')
        if int(data[0]) == roomNum:
            f.write(f"{roomNum},{data[1]},{data[2]},{newStatus}\n")
        else:
            f.write(line)
    f.close()

# Actualiza el archivo de reservas, reescribiendo todo menos el número de habitación que se ingresó.
def updateBookingsFile(roomNum):
    f = open(bookingsFile, "r")
    lines = f.readlines()
    f.close()
    f = open(bookingsFile, "w")
    for line in lines:
        data = line.strip().split(',')
        if int(data[0]) != roomNum:
            f.write(line)
    f.close()

