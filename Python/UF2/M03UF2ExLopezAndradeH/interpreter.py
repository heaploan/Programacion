from library import *

def registrar(command):    
    if len(command) == 4:
        checkDate(command)
    else:
        print('ERROR: Número de argumentos incorrecto.')

def esborrar(command):
    if len(command) == 2:
        missionDelete(command[1]) 
    else:
        print('ERROR: Número de argumentos incorrecto.')

def list(command):
    if len(command) == 2:
        checkYear(command)

#TO DO
#def setmana(command)
    #if len(command) == 1:


#TO DO
#def primera(command):
    #if len(command) == 1:

