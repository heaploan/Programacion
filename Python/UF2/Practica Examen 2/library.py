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
            alumno = lendings[code]['alumno']
            if alumno not in incidences:
                incidences[lendings[code]['alumno']] = []
            incidences[lendings[code]['alumno']].append([code, lendings[code]['inicio'], lendings[code]['fin'], finPrestamoDate])
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

#verifica si hay libros registrados, si no los hay, mostrará mensaje de error
#En caso de haber libros, recorre el diccionario e imprime todos los libros registrados. 
def getBooksList():
    if books == {}:
        print('No hay libros registrados.')
    else:
        for code, info in books.items():
            print(f"{code}: {info['titulo']} , {info['autor']} - ESTADO: {info['estado']}")

#Para obtener el libro con el mayor número de páginas.
def getMaxPages():
    if books == {}:
            print('ERROR: No hay libros registrados')  
    else:
        maxPages = 0
        maxPagesBook = ''
        for code, info in books.items():
            numPages = info['paginas']
            if numPages > maxPages:
                maxPages = numPages
                maxPagesBook = {'code': code, 'title': info['titulo'], 'pages': numPages}
        if maxPagesBook:
            print(f'El libro con más páginas de la biblioteca es: {maxPagesBook["title"]} con {maxPagesBook["pages"]} páginas.')

#Verifica que el género exista en el diccionario books, si no existe mostrará el error.
def checkGenere(command):
        if command[1] == '' or command[1] == ' ':
            print('ERROR: genero no especificado')
        else:
            if not checkBooks:
                print("ERROR: no hay libros registrados.")
            else:
                genero = command[1]
                encontrado = False
                for code, info in books.items():
                    if info['genero'].lower() == genero.lower():
                        encontrado = True
                        print(f"{code}: {info['titulo']} , {info['autor']} - ESTADO: {info['estado']}")                
                if not encontrado:
                    print(f"No hay libros del género '{genero}' registrados.")

#Verifica que haya libros registrados, si hay préstamos registrados y si los hay, entonces imprime los libros y la información del préstamo.
#En caso de que haya algún error, mostrará el mensaje de error correspondiente.
def inLendings(command):
    if books == {}:
        print("No hay libros registrados.")
    else:
        if lendings == {}:
            print('No hay libros en préstamo.')
        else:     
            print('Libros en préstamo:')
            for code, lending in lendings.items():
                today = datetime.today().date()
                if lending['fin'] < today:
                    print(f"Libro: {code} - {books[code]['titulo']} inicio: {lending['inicio']} fin: {lending['fin']} *FUERA DE PLAZO*  ")
                else:
                    print(f"Libro: {code} - {books[code]['titulo']} inicio: {lending['inicio']} fin: {lending['fin']}")

#Verifica que el alumno esté en el diccionario lendings, si está, imprimirá la información del libro.
def infoStudent(command):
    print("Llibres en prestec:")
    check= 0
    for code in lendings:
        if lendings[code]['alumno'] == command:
            check += 1        
    if check > 0:
        for code in lendings:
            if command == lendings[code]['alumno']:
                print(f"Libro: {code} - {books[code]['titulo']} inicio: {lendings[code]['inicio']} fin: {lendings[code]['fin']}")
    else:
        print("El alumno indicado no tiene préstamos registrados")

#Verifica que el alumno esté en el diccionario incidencias
def studentIncidence(command):
    print("Incidències:")
    
    if command in incidences:
        for incidence in incidences[command]:
            print(f"Libro: {incidence[0]}  inicio: {incidence[1]} fin: {incidence[2]} fecha regreso: {incidence[3]}")
    else:
        print("El alumno indicado no tiene incidencias registradas.")    

#Recibe los datos que hay de los libros, si no hay libros, regresa 0 para no dividir entre 0.
#En caso de haber libros, hace una media de las páginas que hay en los libros, dividiendola por la longitud del diccionario books.
def getMedia():
    if not books:
        return 0
    totalPages = 0
    for info in books.values():
        totalPages += info['paginas']
    return totalPages / len(books)

#Cuenta las incidencias que hay registradas en el diccionario incidences mirando el largo del diccionario incidences.
def getTotalIncidences():
    total = 0
    for incidencesList in incidences.values():
        total += len(incidencesList)
        return total

#Calcula el largo del diccionario lendings para contar los prestamos que hay registrados en ese momento.
def getPrestamos():
    if lendings:
        return len(lendings)
    else:
        return 0