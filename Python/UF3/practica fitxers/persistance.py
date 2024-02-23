import os
import validator as v

# Este modulo está hecho para gestionar los ficheros, su creación y su contenido.

# le damos el nombre a la carpeta que queremos crear y luego usamos la misma variable para poder crear el archivo con su nombre y tipo.
folderName = "./dades"
roomsFile = folderName + "/habitacions.txt"
bookingsFile = folderName + "/reserves.txt"

# Recibimos 'habitacion' o 'reserva' y dependiendo de eso hará lo correspondiente a cada fichero.
# En caso de no existir la carpeta, la crea igual que con el archivo.
# Cargamos los datos al diccionario dependiendo de la palabra mencionada seran los datos de habitacions.txt o reserves.txt
def loadData(type):
    folderName = "./dades"
    if not os.path.exists(folderName):
        os.mkdir(folderName)
    if type == "habitacio":
        filePath = folderName + "/habitacions.txt"
    elif type == "reserva":
        filePath = folderName + "/reserves.txt"
    dicc = {}
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
    return dicc



# Recibimos numero de habitacion y comprobamos que exista el archivo y validamos el contenido.
def isRoomInFile(roomNum):
    if os.path.exists(roomsFile):
        f = open(roomsFile, "r")
        for line in f:
            data = line.strip().split(',')
            if len(data) >= 1 and data[0].isdigit() and int(data[0]) == roomNum:
                f.close()
                return True
        f.close()
    return False

# Recibimos el numero de habitación, capacidad y precio.
# Comprobamos la existencia de la carpeta y el archivo, en caso de no existir lo creamos y añadimos la información
# Guardamos los datos en el archivo .txt
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

# Recibimos el numero de habitación, separamos la información que abrimos de bookings y la separamos, comprobando que exista en el diccionario.
# En caso de no existir la habitación regresamos 'False'
def isbookingInFile(roomNum):
    f = open(bookingsFile, "r")
    for line in f:
        data = line.strip().split(',')
        if len(data) >= 1 and data[0].isdigit() and int(data[0]) == roomNum:
            f.close()
            return True
    f.close()
    return False

# Recibimos el número de habitación, nombre, apellido, dni y teléfono.
# si la carpreta no existe, la crea, si el archivo no existe, lo crea y agrega la información.
# si el archivo existe, agrega la información y hace sus respectivas comprobaciones
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

# Recibe numero de habitacion
# carga el archivo 'habitacions.txt'
# Si la disponibilidad de la habitación indicada es 'disponible' devuelve True
# En caso contrario, devuelve False e imprime los respectivos errores. 
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

# Recibe numero de habitación y el nuevo estado
# lee el archivo de habitaciones y al encontrar la habitación indicada, sobreescribe la disponibilidad por la que le hemos pasado. 
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

# reecibe numero de habitación
# Lee el archivo y si encuentra la habitación, no la escribe y todas las que no coinciden, son reescritas.
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