import persistence as p
import sys

rooms = {}

def checkParametros(command, n):
    if len(command) < n:
        print(f"ERROR: Número de argumentos incorrecto.")
        return False
    else:
        return True

def afegirHabitacio(command):
    numero = command[0]
    capacidad = command[1]
    precio = command[2]
    for n in rooms:
        if n in rooms:
            print("ERROR: Ya hay una habitación registrada con ese número.")
        else:
            rooms[numero] = {'capacidad': capacidad,
                             'precio': precio,
                             'estado': 'disponible'}
            rooms = p.roomsFile()

def main():
    command = sys.argv
    if command[0] == 'afegir' and command[1] == 'habitacio':
        if checkParametros(command, 6):
            afegirHabitacio()
    