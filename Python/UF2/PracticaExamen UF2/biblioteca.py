import datetime as dt  # primer capa de datetime para hacer timedelta.
from datetime import datetime # para no tener que poner datetime.datetime

books = {}
lendings = {}
incidences = {}

def checkBooks(code):
   if code in books:
       return False
   else:
       return True 

def booksUpdate(code, title, author, genre, numPag):
    books[code] = {'titol': title,
                      'autor': author,
                      'genere': genre,
                      'pags': int(numPag),
                      #TO DO
                      'ESTAT': "disponible"
                    }
    
def checkLendings(code):
    if code in lendings:
        books[code]['ESTAT'] = "en préstec"
        return False
    else:
        books[code]['ESTAT'] = "disponible"
        return True

#Actualiza el diccionario lendings y incidences con sus incidencias
def lendingsUpdate(code, alumne, iniciPrestec, fiPrestec):
    lendings[code] = {'alumne': alumne, 
                        'inici': iniciPrestec, 
                        'fi': fiPrestec}
    incidences[alumne] = {'incidences': 0
                        }
    
#TO DO 
#Checkar si la fiecha de inicio de prestamo es anterior a la actual o posterior a la fecha de fin de prestamo
def checkDate(code, fiPrestec):
    print(fiPrestec)
    if code in lendings:
        if  fiPrestec > lendings[code]['fi']:
            student = lendings[code[1]]['alumne']
            incidences[student]['incidences'] += 1
            print("El llibre s'ha retornat amb retard. Incidencia registrada")
            lendings[code]['fi'] = fiPrestec
            print('El llibre ha quedat disponible.')
        elif fiPrestec <= lendings[code]['inici']:
            print("ERROR: la data de fiPrestec no pot ser menor al iniciPrestec")
        else:
            print('El llibre ha quedat disponible.')
    else:
        print("ERROR: El llibre no está en préstec")

    
