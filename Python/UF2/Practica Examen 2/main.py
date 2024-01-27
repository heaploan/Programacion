from interpreter import *
check = True
while check:
    command = input('>').lower().split('-')
    if command[0] == "addllibre":
        addLlibre(command)
    elif command[0] == "startprestec":
        startPrestec(command)
    #TO DO
    #elif command[0] == "endprestec":
        #endPrestec(command)
    elif command[0] == "listllibres":
        listLlibres(command)
    #TO DO
    #elif command[0] == "listprestecs":
        #listPrestecs(command)
    #TO DO
    #elif command[0] == "listgenere":
        #listGenere(command)
    #TO DO 
    #elif command[0] == "maxllibre":
        #maxLlibre(command)
    #TO DO 
    #elif command[0] == "stats":
        #stats(command)
    #TO DO 
    #elif command[0] == "info":
        #info(command)
    elif command[0] == "quit":
        check = False
    else:
        print("ERROR: comando incorrecto")
    