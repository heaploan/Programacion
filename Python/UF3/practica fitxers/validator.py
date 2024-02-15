import persistance as p
import hotel as h

# Este modulo está creado para validar el comando que se escribe.

# Función que se encarga de verificar que la longitud de argumentos sea correcta
# recibe argumentos y un número
def commandVal(args, n):
    if len(args) == n:
        return True
    else:
        print('ERROR: número de argumentos incorrecto')

# Función que se encarga de verificar si el DNI es válido
# Recibe el DNI
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


# Recibe la capacidad y comprueba que sea mayor a 0, en caso contrario muestra error.
def checkcapacity(cap):
    if cap > 0:
        return True
    else:
        print("ERROR: Capacidad incorrecta, debe ser mayor a 0")

# Recibe precio y comprueba que sea mayor a 0, en caso contrario muestra error.
def checkPrice(price):
    if price > 0:
        return True
    else:
        print("ERROR: Precio incorrecto, debe ser mayor 0")

# recibe teléfono y comprueba que sean 9 dígitos, en caso contrario devuelve False
def verTelefon(telefon):
    if len(telefon) == 9 and telefon.isdigit():
            return True
    else:
        return False

# recibe número, cumprueba que sea digito y lo devuelve como int, en caso contrario devuelve False
def numVal(num):
    if num.isdigit():
        return int(num)
    else:
        return False

# Recibe número, lo separa por '.', si su longitud es mayor a 1, comprueba que ambos lados del '.' sean digitos.
# En caso de ser asi devuelve num en int
# Si no hay punto, simplemente devuelve num como float pero tambien comprueba que sea digito.
# si no es ninguno de los dos casos, devuelve False.
def floatVal(num):
    fl = num.split('.')
    if len(fl) > 1:
        if fl[0].isdigit() and fl[1].isdigit():
            return float(num)
    else:
        if num.isdigit():
            return float(num)
    return False

# Función que se encarga de convertir los datos de habitación y dividirla por valores.
# También pasa los valores a las otras funciones como addRoom y addRoomToFile
def convertRoomData(command):
        roomNum = numVal(command[3])
        cap = numVal(command[4])
        price = floatVal(command[5])
        h.addRoom(roomNum, cap, price)

# Función que se encarga de convertir los datos de reservas y dividirla por valores
# también pasa los valores a las otras funciones como addBooking y addBookingToFile
def convertBookingData(command):
    roomNum = numVal(command[3])
    name = command[4]
    last = command[5]
    dni = command[6]
    phone = command[7]
    h.addBooking(roomNum, name, last, dni, phone)

# Función que se encarga de convertir los datos de finalizar
# También pasa los datos a la función endBooking
def convEndData(command):
    roomNum = numVal(command[2])
    day = command[3]
    h.endBooking(roomNum, day)

# Función para convertir el dato y pasarlo a la funcion cleaner
def convClean(command):
    roomNum = numVal(command[2])
    h.cleaner(roomNum)

# Función que obtiene el dni, utiliza la función de verificar dni
# y lo pasa a la función infoDni
def getDni(command):
    dni = command[2]
    if verificacioNif(dni):
        h.infoDni(dni)
    else:
        print('ERROR: DNI inválido')