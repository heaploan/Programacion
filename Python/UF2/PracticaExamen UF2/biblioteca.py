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
                      'pags': int(numPag)}
    
def checkLendings(code):
    if code in lendings:
        return False
    else:
        return True

def lendingsUpdate(code, alumne, iniciPrestec, fiPrestec):
    lendings[code[1]] = {'Alumne': alumne[2], 
                        'Inici': iniciPrestec, 
                        'Fi': fiPrestec}
    students[alumne] = {'incidences': 0
                        }

def esBisiesto(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False