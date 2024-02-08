import validator as v
import sys
from hotel import *
# ejemplo: py ./main.py afegir habitacio 100 1 45.90

if v.commandVal(sys.argv) > 1:
    arg1 = sys.argv[1].lower()
    if arg1 == 'afegir':
        arg2 = sys.argv[2].lower()
        if len(sys.argv) == 6 and arg2 == 'habitacio':
            print('habitacio')
        elif len(sys.argv) == 8 and arg2 == 'reserva':
            print('reserva')
    elif arg1 == 'finalitzar':
        if v.commandVal(sys.argv, 3):
            print('flinalitzar')
    elif arg1 == 'netejar':
        if v.commandVal(sys.argv, 3):
            print('netejar')
    elif arg1 == 'list':
        if v.commandVal(sys.argv, 2):
            print('list')
    elif arg1 == 'info':
        if v.commandVal(sys.argv, 3):
            print('info dni')
    elif arg1 == 'reserves':
        if v.commandVal(sys.argv, 2):
            print('reserves')
    else:
        print("ERROR: Comando incorrecto")
else:
    print("ERROR: no se han introducido argumentos")