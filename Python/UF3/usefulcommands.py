import sys
import os
#Verifica la longitud del comando.
dictionary = {}

def commandVal(args, n):
    if len(args) == n:
        return True
    else:
        print('ERROR: número de argumentos incorrecto')

def checkArguments():
    if len(sys.argv) < 3:
        print("ERROR: se esperaban al menos 2 argumentos.")

#Verifica si el diccionario está vacío o no.
def checkContent():
    if dictionary == {}:
        return True
    else:
        return False
    
#Cuenta el largo del contenido del diccionario y lo devuelve.
def getLen():
    if dictionary:
        return len(dictionary)
    else:
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
    else:
        return False

# Función que se encarga de verificar si el DNI es válido
def verificacioNif(nif):
    if len(nif) != 9:
        print("ERROR: DNI incorrecto")
        return False
    letra = nif[-1].upper()
    if not nif[:-1].isdigit() or not letra.isalpha():
        print("ERROR: DNI incorrecto")
        return False
    letrasValidas = 'TRWAGMYFPDXBNJZSQVHLCKE'
    controlLetra = int(nif[:-1]) % 23
    if letra != letrasValidas[controlLetra]:
        print("ERROR: DNI incorrecto")
        return False
    return True

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
                    dict[roomNum] = {'name': data[1], 'last': data[2], 'dni': data[3], 'phone': data[4]}   
    return dict