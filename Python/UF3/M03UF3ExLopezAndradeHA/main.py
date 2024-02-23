import sys
import validator as v
from cole import *

if len(sys.argv) > 1:
    arg1 = sys.argv[1].lower()
    if arg1 == 'alta':
        if v.commandVal(sys.argv, 6): 
            v.convertAlta(sys.argv)
    elif arg1 == 'baixa':
        if v.commandVal(sys.argv, 3):
            v.getDni(sys.argv)
    elif arg1 == 'llistat':
        arg2 = sys.argv[2]
        if v.commandVal(sys.argv, 3):
            if arg2 == '*':
                llistat()
    elif arg1 == 'mitjana':
        if v.commandVal(sys.argv, 2):
            print('mitjana')
    elif arg1 == 'stats':
        if v.commandVal(sys.argv, 3):
            print('stats')
    else:
        print("ERROR: Comando incorrecto")
else:
    print("ERROR: no se han introducido argumentos")