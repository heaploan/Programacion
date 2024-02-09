import persistance as p
import hotel as h

# Este modulo está creado para validar el comando que se escribe.

def commandVal(args, n):
    if len(args) == n:
        return True
    else:
        print('ERROR: número de argumentos incorrecto')

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

def checkcapacity(cap):
    if cap > 0:
        return True
    else:
        print("ERROR: Capacidad incorrecta, debe ser mayor a 0")

def checkPrice(price):
    if price > 0:
        return True
    else:
        print("ERROR: Precio incorrecto, debe ser mayor 0")

def verTelefon(telefon):
    if len(telefon) == 9 and telefon.isdigit():
            return True
    else:
        return False
    
def convertRoomData(command):
    roomNum = command[3]
    cap = int(command[4])
    price = float(command[5])
    h.addRoom(roomNum, cap, price)
    p.addRoomToFile(roomNum, cap, price)
    
def convertBookingData(command):
    roomNum = (command[3])
    name = command[4]
    last = command[5]
    dni = command[6]
    phone = command[7]
    h.addBooking(roomNum, name, last, dni, phone)
    p.addBookingToFile(roomNum, name, last, dni, phone)

