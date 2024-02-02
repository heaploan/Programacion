import datetime as dt

misiones = {}

def checkMission(command):
    if command not in misiones:
        return True
    else:
        return False

def checkMissios(command):
    if checkMission(command[1]):
        addMission()

def addMission(command):
    if len(command) == 4:
        misiones[]