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
                'inici': inicioPrestamo, 
                'fi': finPrestamo,
                'incidence': '', 
                'incidences': 0}
