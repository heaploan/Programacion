from hotel import *

def main():
    if checkArguments(6):
        com = sys.argv[1].lower()
        com2 = sys.argv[2].lower()
        if com == 'afegir' and com2 == 'habitacio':
            numero = sys.argv[3]
            capacidad = sys.argv[4]
            precio = sys.argv[5]
            roomsUpdate(numero, capacidad, precio)
    #elif com == 'finalitzar':