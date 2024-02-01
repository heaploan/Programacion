from interpreter import *
check = True
while check:
    command = input('>').split('-')
    com = command[0].lower()
    if com == "addllibre":
        addLlibre(command)        
    elif com == "startprestec":
        startPrestec(command)
    elif com == "endprestec":
        endPrestec(command)
    elif com == "listllibres":
        listLlibres(command)
    elif com == "listprestecs":
        listPrestecs(command)
    elif com == "listgenere":
        listGenere(command)
    elif com == "maxllibre":
        maxLlibre(command)
    elif com == "stats":
        stats(command)
    elif com == "info":
        info(command)
    elif com == "quit":
        if len(command) == 1:
            check = False
    else:
        print("ERROR: comando incorrecto")