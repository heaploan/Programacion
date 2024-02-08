import os
import hotel as h  # Importamos el módulo hotel donde se encuentra definido el diccionario h.rooms
import interpreter as i
# Ruta del archivo donde se guardan los datos de las habitaciones

roomFilePath = "./dades/habitacions.txt"
bookingFilePath = "./dades/reserves.txt"

# Función para cargar las habitaciones desde el archivo
def loadRoomsFromFile():
    rooms = {}
    # Verificamos si el archivo existe
    if os.path.exists(roomFilePath):
        # Abrimos el archivo en modo de lectura
        f = open(roomFilePath, "r")
        # Iteramos sobre cada línea del archivo
        for line in f:
            # Dividimos la línea en sus partes separadas por comas
            data = line.strip().split(',')
            # Verificamos que la línea tenga datos y que el primer elemento sea un número
            if data and data[0].isdigit():
                # Extraemos los datos de la habitación de la línea
                roomNum = int(data[0])
                cantidad = int(data[1])
                precio = float(data[2])
                estado = data[3].strip()  # Eliminamos los espacios en blanco alrededor del estado
                # Creamos un diccionario con los datos de la habitación y lo agregamos al diccionario de habitaciones en el módulo hotel
                rooms[roomNum] = {'cantidad': cantidad, 
                                    'precio': precio, 
                                    'estado': estado}
        # Cerramos el archivo después de leerlo
        f.close()
        return rooms

def loadbookingFromFile():
    # Verificamos si el archivo existe
    if os.path.exists(bookingFilePath):
        # Abrimos el archivo en modo de lectura
        f = open(bookingFilePath, "r")
        # Iteramos sobre cada línea del archivo
        for line in f:
            # Dividimos la línea en sus partes separadas por comas
            data = line.strip().split(',')
            # Verificamos que la línea tenga datos y que el primer elemento sea un número
            if data and data[0].isdigit():
                # Extraemos los datos de la habitación de la línea
                roomNum = int(data[0])
                nom = data[1]
                cognom = (data[2])
                dni = data[3]
                telefon = int(data[4].strip())  # Eliminamos los espacios en blanco alrededor del telefono
                # Creamos un diccionario con los datos de la habitación y lo agregamos al diccionario de habitaciones en el módulo hotel
                h.bookings[roomNum] = {'nom': nom, 
                                    'cognom': cognom, 
                                    'dni': dni,
                                    'telefon': telefon}
        # Cerramos el archivo después de leerlo
        f.close()

# Función para verificar si una habitación está en el archivo
def isRoomInFile(roomNum):
    # Abrimos el archivo en modo de lectura
    f = open(roomFilePath, "r")
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

def isbookingInFile(roomNum):
    # Abrimos el archivo en modo de lectura
    f = open(bookingFilePath, "r")
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

def addRoomToFile(command):
    roomNum = int(command[3])  # Extraemos el número de habitación de los argumentos
    quantity = int(command[4])  # Extraemos la cantidad de habitaciones de los argumentos
    price = float(command[5])  # Extraemos el precio de habitación de los argumentos
    if isRoomInFile(roomNum):
        print("ERROR: Ya existe una habitación con el número indicado.")
    else:
        f = open(roomFilePath, "a")  # Abrimos el archivo en modo de adición
        f.write(f"{roomNum},{quantity},{price},DISPONIBLE\n")  # Escribimos la información de la habitación en el archivo
        f.close()  # No olvides cerrar el archivo después de escribir en él
        print("Habitacio registrada")  # Mostramos un mensaje indicando que la habitación ha sido registrada

def addBookingToFile(command):
    roomNum = int(command[3])
    nom = command[4]
    cognom = command[5]
    dni = command[6]
    telefon = command[7]
    if isbookingInFile(roomNum):
        print("ERROR: Ya existe una reserva para esta habitación")
    else:
        if i.verificacioNif(dni):   
            if i.verTelefon(telefon):
                f = open(bookingFilePath, "a")
                f.write(f"{roomNum},{nom},{cognom},{dni},{telefon}\n")
                f.close()
                print("Reserva registrada")