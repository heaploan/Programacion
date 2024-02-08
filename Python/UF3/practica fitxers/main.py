import sys
from hotel import *
from interpreter import *
# ejemplo: py ./main.py afegir habitacio 100 1 45.90

if len(sys.argv) > 1:
    arg1 = sys.argv[1].lower()
    if arg1 == 'afegir':
        arg2 = sys.argv[2].lower()
        if commandVal(sys.argv, 6) == 6 and arg2 == 'habitacio':
            print('habitacio')
        elif len(sys.argv) == 8 and arg2 == 'reserva':
            print('reserva')
        else:
            print('ERROR: numero de argumentos incorrecto')
    elif arg1 == 'finalitzar':
        if len(sys.argv) == 3:
            print('flinalitzar')
    elif arg1 == 'netejar':
        if len(sys.argv) == 3:
            print('netejar')
    elif arg1 == 'list':
        if len(sys.argv) == 2:
            print('list')
    elif arg1 == 'info':
        if len(sys.argv) == 3:
            print('info')
    
    else:
        print("ERROR: Comando incorrecto")
else:
    print("ERROR: no se han introducido argumentos")

