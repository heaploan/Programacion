from library import *

#Aquí comprobamos el tamaño de la string introducida, en caso de no ser correcta, mostrará error.
#Si el numero de páginas sea 0 o menor a 0 dará error de páginas.
#En caso el código del libro ya está registrado, mostrará dicho error.
#Si todo está en orden, mostrará un mensaje de 'libro registrado' y se agregará el libro al diccionario.
def addLlibre(command):
    if len(command) == 6:
        if checkBooks(command[1]):
            if command[5].isdigit() and int(command[5]) > 0:
                booksUpdate(command[1], command[2], command[3], command[4], command[5])
                print('Libro registrado.')
            else:
                print('ERROR: ¡Número de páginas incorrecto!')
        else:
            print('ERROR: ¡Ya existe un libro con este código')
    else:
        print('ERROR: ¡Número de argumentos incorrecto!')

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
    if 0 < d < 32 and 0 < m < 13 and y > 0:
        selectedDate = dt.date(y, m, d)
        finPrestamo = selectedDate + dt.timedelta(days=15)
        lendingsUpdate(command[1], command[2], selectedDate, finPrestamo)
        books[command[1]]['estado'] = "en prestamo"
        print("Préstamo registrado, el libro se ha de regresar:", finPrestamo)
    else:
        print('ERROR: Fecha incorrecta.')

#Se confirma que la longitud de command sea 4, en caso contrario muestra error
#Si el diccionario books está vacío, mostrará error.
#En caso de que un libro esté en préstamo, se mostrará error.
def startPrestec(command):
    if len(command) == 4:
        if not checkBooks(command[1]):
            if not checkLendings(command[1]):
                calcDate(command)
            else:
                print("ERROR: No se puede prestar un libro que ya está en préstamo")
        else:
            print("ERROR: No hay libros registrados")
    else:
        print("ERROR: Número de argumentos incorrecto.")

def checkDate(code, finPrestamo):
    if books[code]['estado'] == 'en prestamo':
        finPrestamoDate = datetime.strptime(finPrestamo, "%d/%m/%Y").date()
        if finPrestamoDate == lendings[code]['fin']:
            books[code]['estado'] = 'disponible'
            print('El llibre ha quedat disponible.')
        elif finPrestamoDate > lendings[code]['fin']:
            lendings[code]['incidencias'] += 1
            lendings[code]['entrega final'] = finPrestamoDate
            lendings[code]['incidencia'] = {'alumno': lendings[code]['alumno'],
                                            'libro': code,
                                            'inicio': lendings[code]['inicio'],
                                            'fin': lendings[code]['fin'],}
            print("El libro ha sido entregado con retraso, incidencia registrada.")
            books[code]['estado'] = 'disponible'
            print('El libro ahora está disponible')
        else:
            print("ERROR: La fecha de fin de préstamo no puede ser menor a la de inicio")
    else:
        print("ERROR: El libro no está en préstamo")


#TO DO
def endPrestec(command):
    if len(command) == 3:
        #El libro tiene que existir y tiene que estar en préstamo para poderse regresar
        if not checkBooks(command[1]):
            checkDate(command[1], command[2])
        else:
            print('ERROR: El codigo del libro no está registrado')
    else:
        print('ERROR: Número de argumentos incorrecto.')
        #La fecha del regreso no puede ser anterior a la fecha del inicio del préstamo
            
        #Si la fecha del regreso es posterior a la registrada, se deberá de registrar la incidencia
        #La incidencia quedará registrada con el nombre del alumno, codigo del libro y los tres datos del préstamo.
        #Fecha en la que se ha prestado el libro, fecha en la que se tenia que regresar y fecha en la que se ha regresado finalmente.
            
#Comprobamos que el comando tenga la longitud indicada
#Si el diccionario books está vacío, mostrará error.
#En caso de que haya libros, imprimirá el código y sus valores, titulo, autor y estado.
def listLlibres(command):
    if len(command) == 1:
        if books == {}:
            print('No hay libros registrados.')
        else:
            for code, info in books.items():
                print(f"{code}: {info['titulo']} , {info['autor']} - ESTADO: {info['estado']}")

#TO DO
#def listPrestecs(command):
    #tiene que mostrar los libros que están en préstamo
    #tiene que indicar los que estén fuera de terminio, es decir, que ya ha pasado la fecha de devolución y aún no se ha regresado.
             
#Tiene que mostrar los datos del género indicado
def listGenere(command):
    if len(command) == 2:
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
              
#Tiene que mostrar los datos del libro que tien más páginas de la biblioteca
def maxLlibre(command):
    if len(command) == 1:
        if not checkBooks:
            print('ERROR: No hay libros registrados.')
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
#TO DO
    #def stats(command):
        #tiene que mostrar el número de libros registrados, número de incidencias registradas y media de páginas por libro de la biblioteca

#TO DO 
#Tiene que mostrar los libros que tiene en préstamo (si los tiene) y las incidencias que ha tenido (si las ha tenido)
def info(command):
    foundLoans = False
    if len(command) == 2:
        if command[1]:
            for code, info in lendings.items():
                if info['alumno'] == command[1]:
                    if not foundLoans:
                        print(f"Libros en préstamo:")
                        foundLoans = True
                    bookTitle = books[code]['titulo']
                    if books[code]['estado'] == "disponible":
                        print(f"El alumno indicado no tiene libros en préstamo.")
                    else:
                        print(f"Llibre: {code} - {bookTitle} Inici: {info['inicio']} Data fi: {info['fin']}")
                        if info['incidencias'] > 0:
                            print("Incidencias:")
                            print(f"libro: {code} inicio: {info['inicio']} fin: {info['fin']} Entrega Final: {info['entrega final']}")
                        # Eliminamos la parte del 'elif' que imprime "El alumno indicado no tiene incidencias registradas"
