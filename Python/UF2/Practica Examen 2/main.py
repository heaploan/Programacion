from interpreter import *
check = True
while check:
    command = input('>').split('-')
    if command[0].lower() == "addllibre":
        addLlibre(command)
    elif command[0].lower() == "startprestec":
        startPrestec(command)
    #TO DO
    elif command[0].lower() == "endprestec":
        endPrestec(command)
    elif command[0].lower() == "listllibres":
        listLlibres(command)
    #TO DO
    #elif command[0].lower() == "listprestecs":
        #listPrestecs(command)
    #TO DO
    elif command[0].lower() == "listgenere":
        listGenere(command)
    elif command[0].lower() == "maxllibre":
        maxLlibre(command)
    #TO DO 
    #elif command[0].lower() == "stats":
        #stats(command)
    #TO DO
    #elif command[0].lower() == "info":
        #info(command)
    elif command[0].lower() == "quit":
        check = False
    else:
        print("ERROR: comando incorrecto")
    