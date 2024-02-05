import files
import sys

rooms = {}
bookings = {}

def checkParametros(command, n):
    if len(command) == n:
        return True
    else:
        print(f"ERROR: Número de argumentos incorrecto.")

def checkArguments():
    if len(sys.argv) < 2 :
        print("ERROR: Se esperaban al menos 2 argumentos.")
        sys.exit(1)

def checkRoom(command):
    if command[2] in rooms:
        print('ERROR: Ya existe una habitación con el número indicado')
    else:
        return False

def roomsUpdate(command):
    rooms[command[2]] = { 'capacidad': command[3],
                     'precio': command[4]}


def main():
    if checkArguments(2):
        com = sys.argv[1].lower()
        com2 = sys.argv[2:].lower()
    if com == 'afegir':
        subCom = com2[0].lower()
        if subCom == 'habitacio':
            print()
        elif subCom == 'reserva':
            print()
        else:
            print("ERROR comando incorrecto")
