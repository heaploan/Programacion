import persistance as p
import hotel as h

# Este modulo está creado para validar el comando que se escribe.

# Función que se encarga de verificar que la longitud de argumentos sea correcta
def commandVal(args, n):
    if len(args) == n:
        return True
    else:
        print('ERROR: número de argumentos incorrecto')

# Función que se encarga de verificar si el DNI es válido
def verificacioNif(nif):
    if len(nif) != 9:
        return False
    letra = nif[-1].upper()
    if not nif[:-1].isdigit() or not letra.isalpha():
        return False
    letrasValidas = 'TRWAGMYFPDXBNJZSQVHLCKE'
    controlLetra = int(nif[:-1]) % 23
    if letra != letrasValidas[controlLetra]:
        return False
    return True

# Función que se encarga de verificar que la capacidad sea mayor a 0
def checkcapacity(cap):
    if cap > 0:
        return True
    else:
        print("ERROR: Capacidad incorrecta, debe ser mayor a 0")

# Función que se encarga de verificar que el precio sea mayor a 0
def checkPrice(price):
    if price > 0:
        return True
    else:
        print("ERROR: Precio incorrecto, debe ser mayor 0")

# Función que se encarga de verificar los caracteres del telefono y si todos son números
def verTelefon(telefon):
    if len(telefon) == 9 and telefon.isdigit():
            return True
    else:
        return False

# Función que se encarga de convertir los datos de habitación y dividirla por valores.
# También pasa los valores a las otras funciones como addRoom y addRoomToFile
def convertRoomData(command):
    roomNum = command[3]
    cap = int(command[4])
    price = float(command[5])
    h.addRoom(roomNum, cap, price)
    p.addRoomToFile(roomNum, cap, price)

# Función que se encarga de convertir los datos de reservas y dividirla por valores
# también pasa los valores a las otras funciones como addBooking y addBookingToFile
def convertBookingData(command):
    roomNum = (command[3])
    name = command[4]
    last = command[5]
    dni = command[6]
    phone = command[7]
    h.addBooking(roomNum, name, last, dni, phone)
    p.addBookingToFile(roomNum, name, last, dni, phone)

# Función que se encarga de convertir los datos de finalizar
# También pasa los datos a la función endBooking
def convEndData(command):
    roomNum = command[2]
    day = int(command[3])
    h.endBooking(roomNum, day)

# Función para convertir el dato y pasarlo a la funcion cleaner
def convClean(command):
    roomNum = command[2]
    h.cleaner(roomNum)

# Función que obtiene el dni, utiliza la función de verificar dni
# y lo pasa a la función infoDni
def getDni(command):
    dni = command[2]
    if verificacioNif(dni):
        h.infoDni(dni)