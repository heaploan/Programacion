import files
import sys

rooms = {}
bookings = {}

def checkParametros(command, n):
    if len(command) == n:
        return True
    else:
        print(f"ERROR: Número de argumentos incorrecto.")

def checkArguments(minimos):
    if len(sys.argv) < minimos :
        print("ERROR: Se esperaban al menos 2 argumentos.")
        sys.exit(1)

def checkRoom(command):
    if command[2] in rooms:
        print('ERROR: Ya existe una habitación con el número indicado')
    else:
        return False

def roomsUpdate(numero, capacidad, precio):
    rooms[numero] = { 'capacidad': capacidad,
                     'precio': precio}

print(rooms)
