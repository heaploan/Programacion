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
    lendings = {'code': code,
                'alumne': alumne, 
                        'inici': iniciPrestec, 
                        'fi': fiPrestec,
                        'incidences': 0}
    
#TO DO 
#Checkar si la fiecha de inicio de prestamo es anterior a la actual o posterior a la fecha de fin de prestamo
def checkDate(code, fiPrestec):
    if code in lendings:
        fiPrestec_date = datetime.strptime(fiPrestec, "%Y/%m/%d").date()
        if fiPrestec_date == lendings[code]['fi']:
            books[code]['estado']
            print('El llibre ha quedat disponible.')
        elif fiPrestec_date > lendings[code]['fi']:
            student = lendings[code]['alumne']
            incidences[student]['incidences'] += 1
            print("El llibre s'ha retornat amb retard. Incidencia registrada")
            lendings.pop(code)
            print('El llibre ha quedat disponible.')
        else:
            print("ERROR: la data de fiPrestec no pot ser menor al iniciPrestec")
    else:
        print("ERROR: El llibre no está en préstec")