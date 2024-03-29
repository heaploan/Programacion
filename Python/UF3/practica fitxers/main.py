from validator import *
import hotel as h
import sys
from hotel import *

if len(sys.argv) > 1:
    arg1 = sys.argv[1].lower()
    if arg1 == 'afegir':
        arg2 = sys.argv[2].lower()
        if len(sys.argv) == 6 and arg2 == 'habitacio':
            convertRoomData(sys.argv)
        elif len(sys.argv) == 8 and arg2 == 'reserva':
            convertBookingData(sys.argv)
        else:
            print("ERROR: numero de argumentos incorrecto")
    elif arg1 == 'finalitzar':
        if commandVal(sys.argv, 4):
            convEndData(sys.argv)
    elif arg1 == 'netejar':
        if commandVal(sys.argv, 3):
            convClean(sys.argv)
    elif arg1 == 'list':
        if commandVal(sys.argv, 2):
            roomList()
    elif arg1 == 'info':
        if commandVal(sys.argv, 3):
            getDni(sys.argv)
    elif arg1 == 'reserves':
        if commandVal(sys.argv, 2):
            reserves()
    else:
        print("ERROR: Comando incorrecto")
else:
    print("ERROR: no se han introducido argumentos")