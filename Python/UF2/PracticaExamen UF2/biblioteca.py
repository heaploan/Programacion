import datetime as dt  # primer capa de datetime para hacer timedelta.
from datetime import datetime # para no tener que poner datetime.datetime

books = {}
lendings = {}

def checkBooks(code):
   if code in books:
       return False
   else:
       return True 

def booksUpdate(code, title, author, genre, numPag):
    books[code[1]] = {'titol': title[2], 'autor': author[3], 'genere': genre[4], 'pags': int(numPag[5])}
    
def lendingsUpdate(code, alumne, iniciPrestec, fiPrestec):
    lendings[code[1]] = {'Alumne': alumne[2], 'Inici': iniciPrestec, 'Fi': fiPrestec}