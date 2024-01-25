import datetime as dt  # primer capa de datetime para hacer timedelta.
from datetime import datetime # para no tener que poner datetime.datetime

books = {}
lendings = {}
students = {}

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

def lendingsUpdate(code, alumne, iniciPrestec, fiPrestec):
    lendings[code[1]] = {'Alumne': alumne[2], 
                        'Inici': iniciPrestec, 
                        'Fi': fiPrestec}
    students[alumne] = {'incidences': 0
                        }
#TO DO 
#Checkar si la fiecha de inicio de prestamo es anterior a la actual o posterior a la fecha de fin de prestamo
def checkDate(code, iniciPrestec, fiPrestec):