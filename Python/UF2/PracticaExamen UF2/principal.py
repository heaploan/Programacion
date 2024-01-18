from interpret import *
check = True

while check:
    command = input('>').split
    if command[0] == "addllibre":
        addLlibre(command)
    elif command[0] == "startprestec":
        startPrestec(command)
