from interpreter import *

check = True

while check:
    command = input('').split(',')
    com = command[0].lower()
    if com == 'registrar':
        checkDate(command)
    elif com == 'esborrar':
        missionDelete(command)
    elif com == 'list':
        list(command)
    #elif com == 'setmana':

    #elif com == 'primera':

    elif com == 'exit':
        if len(command) == 1:
            check = False
    else:
        print('ERROR: comando incorrecto.')