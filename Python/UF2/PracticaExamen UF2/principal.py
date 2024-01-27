from interpret import *
check = True
while check:
    command = input('>').split('-')
    if command[0] == "addLlibre":
        addLlibre(command)
    elif command[0] == "startPrestec":
        startPrestec(command)
    #TO DO
    elif command[0] == "endPrestec":
        endPrestec(command)
    #TO DO
    #elif command[0] == "listLlibres":
        #listLlibres(command)
    #TO DO
    #elif command[0] == "listPrestecs":
        #listPrestecs(command)
    #TO DO
    #elif command[0] == "listGenere":
        #listGenere(command)
    #TO DO 
    #elif command[0] == "maxLlibre":
        #maxLlibre(command)
    #TO DO 
    #elif command[0] == "stats":
        #stats(command)
    #TO DO 
    #elif command[0] == "info":
        #info(command)
    elif command[0] == "quit":
        check = False
    #else:
        #print("ERROR: comando incorrecto")
    