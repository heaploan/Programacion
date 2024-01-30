import datetime as dt
from datetime import datetime

books = {}
lendings = {}
incidences = {}

#Si el código libro no está en el diccionario books:
def booksUpdate(code, title, autor, genre, numPag):
    books[code] = {'titulo': title,
                    'autor': autor,
                    'genero': genre,
                    'paginas': int(numPag),
                    'estado': "disponible"}

#Actualiza el diccionario lendings
def lendingsUpdate(code, alumno, inicioPrestamo, finPrestamo):
    lendings[code] = {'alumno': alumno, 
                'inicio': inicioPrestamo, 
                'fin': finPrestamo}

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

#La fecha del regreso no puede ser anterior a la fecha del inicio del préstamo
#Si la fecha del regreso es posterior a la registrada, se deberá de registrar la incidencia
#La incidencia quedará registrada con el nombre del alumno, codigo del libro y los tres datos del préstamo.
#Fecha en la que se ha prestado el libro, fecha en la que se tenia que regresar y fecha en la que se ha regresado finalmente.
def checkDate(code, finPrestamo):
    if books[code]['estado'] == 'en prestamo':
        finPrestamoDate = datetime.strptime(finPrestamo, "%d/%m/%Y").date()
        if finPrestamoDate <= lendings[code]['fin']:
            books[code]['estado'] = 'disponible'
            lendings.pop(code)
            print('El libro ahora esta disponible.')
        elif finPrestamoDate > lendings[code]['fin']:
            incidences[lendings[code]['alumno']] = []
            incidences[lendings[code]['alumno']].append([lendings[code], lendings[code]['inicio'], lendings[code]['fin'], finPrestamoDate])
            print("El libro ha sido entregado con retraso, incidencia registrada.")
            books[code]['estado'] = 'disponible'
            lendings.pop(code)
            print('El libro ahora está disponible')
        else:
            print("ERROR: La fecha de fin de préstamo no puede ser menor a la de inicio")
    else:
        print("ERROR: El libro no está en préstamo")

#dividimos la fecha ingresada en command con '/' en tres partes, dia, mes y año
#comprobamos que sean números y si los rangos no son los indicados, mostrará error.
#cambiamos el formato de la fecha ingreada a año, mes  y día.
#sumamos con timedelta 15 días al inicio del prestamo para obtener la fecha del fin del prestamo.
#actualizamos el diccionario lendings y el estado del libro en el diccionario books.
#Además de que también comprobamos de que el prestamo no puede registrarse dias anteriores al dia actual. 
def calcDate(command):
    d_m_y = command[3].split('/')
    d = int(d_m_y[0])
    m = int(d_m_y[1])
    y = int(d_m_y[2])
    selectedDate = dt.date(y, m, d)
    finPrestamo = selectedDate + dt.timedelta(days=15)
    lendingsUpdate(command[1], command[2], selectedDate, finPrestamo)
    books[command[1]]['estado'] = "en prestamo"
    print("Préstamo registrado, el libro se ha de regresar:", finPrestamo)

#Verifica que el género exista en el diccionario books, si no existe mostrará el error.
def checkGenere(command):
    genero = command[1]
    encontrado = False
    for code, info in books.items():
        if info['genero'].lower() == genero.lower():
            encontrado = True
            print(f"{code}: {info['titulo']} , {info['autor']} - ESTADO: {info['estado']}")                
        if not encontrado:
            print(f"No hay libros del género '{genero}' registrados.")