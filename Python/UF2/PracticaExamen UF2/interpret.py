from biblioteca import *

def addLlibre(command):
    if len(command) == 6:
        if checkBooks(command[1]):
            if command[5].isdigit() and int(command[5]) > 0:
                booksUpdate(command[1], command[2], command[3], command[4], command[5])
                print('Llibre registrat')
            else:
                print('ERROR: num de pagines incorrecte!')
        else:
            print('ERROR: Ja eisteix un llibre amb aquest codi')
    else:
        print("ERROR: nº d'arguments incorrecte")
                
def startPrestec(command):
    if len(command) == 4:
        if not checkBooks(command[1]):
            d, m, y = command[3].split('/')
            if d.isdigit() and m.isdigit() and y.isdigit() and 0 < int(d) < 32 and 0 < int(m) < 13 and int(y) > 0:
                return
            else:
                print('ERROR: Data incorrecte')
        else:
            print('ERROR: No hi ha cap llibre registrat')
    else:
        print("ERROR: nº d'arguments incorrecte")