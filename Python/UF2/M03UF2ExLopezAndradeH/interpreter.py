from library import *

def registrar(command):    
        checkDate(command)

def esborrar(command):
        missionDelete(command[1]) 

def list(command):
        checkYear(command)

def setmana(command):
    checkWeek(command)

#TO DO
#def primera(command):
    #if len(command) == 1:

