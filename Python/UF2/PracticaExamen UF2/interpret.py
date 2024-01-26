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
            if checkLendings(command[1]):
                d_m_y = command[3].split('/')
                d = d_m_y[0]
                m = d_m_y[1]
                y = d_m_y[2]
                if d.isdigit() and m.isdigit() and y.isdigit() and 0 < int(d) < 32 and 0 < int(m) < 13 and int(y) > 0:
                    d = int(d)
                    m = int(m)
                    y = int(y)
                    if d >= datetime.today().day and m >= datetime.today().month and y >= datetime.today().year:
                        iniciPrestec = dt.date(y,m,d)
                        fiPrestec = iniciPrestec + dt.timedelta(days=15)
                        lendingsUpdate(command[1],command[2],command[3], fiPrestec)
                        print("Prestec registrat. El llibre s'ha de retornar:",fiPrestec)
                    else:
                        print("ERROR: La fecha no puede ser anterior al día de hoy")
                else:
                    print('ERROR: Data incorrecte')
            else:
                print("ERROR: No es pot registrar el préstec d'un llibre que ja està en préstec.")  
        else:
            print('ERROR: No hi ha cap llibre registrat')
    else:
        print("ERROR: nº d'arguments incorrecte")
    #Si la fecha de regreso es posterior a la registrada, se tendrá que registrar una incidencia

#TO DO 
def endPrestec(command):
    if len(command) == 3:
    #El libro tiene que existir y estar en prestamo para poderse regresar
    #La fecha de regreso no puede ser antarior a la fecha del inicio del prestamo.
            checkDate(command[1], command[2])
    else:
        print('ERROR: el comando no es correcte')

    #Registrar que un libro se regresa a la biblioteca por tanto queda disponible

    #La incidencia quedara registrada con el nombre del alumno, codigo del libro, la fecha del prestamo, del retorno y la que se ha regresado finalmente.

#TO DO 
#def listLlibres(command):
    #Mostrar todos los datos de todos los libros registrados.
    #EJ: >ListLlibre
    #001 : La historia interminable, Michael Ende, - ESTAT: en préstec
    #002 : El principito, Antoine de Saint Exupery - ESTAT: disponible 

#TO DO
#def listPresteces(command):

#TO DO 
#def listGenere(command):

#TO DO
#def maxLlibre(command):

#TO DO 
#def stats(command):

#TO DO
#def info(command):
