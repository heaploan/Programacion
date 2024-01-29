import datetime as dt
from datetime import datetime

books = {}
lendings = {}

#Si el código libro no está en el diccionario books:
def booksUpdate(code, title, autor, genre, numPag):
    books[code] = {'titulo': title,
                    'autor': autor,
                    'genero': genre,
                    'paginas': int(numPag),
                    'estado': "disponible"}

def lendingsUpdate(code, alumno, inicioPrestamo, finPrestamo):
    lendings[code] = {'alumno': alumno, 
                'inicio': inicioPrestamo, 
                'fin': finPrestamo,
                'entrega final': '',
                'incidencia': '', 
                'incidencias': 0}

#Verificamos si el codigo está en el diccionario lendings o no
def checkLendings(code):
    if books[code]['estado'] == 'disponible':
        return False
    else:
        return True
    
#Comprobar si el código del libro ya está en el diccionario 'books'
def checkBooks(command):
   if command not in books:
       return True
   else:
       return False