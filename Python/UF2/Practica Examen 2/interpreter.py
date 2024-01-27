from library import *

#Comprobar si el código del libro ya está en el diccionario 'books'
def checkBooks(command):
   if command not in books:
       return True
   else:
       return False

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
        today = dt.date.today()
        selectedDate = dt.date(y, m, d)
        if selectedDate >= today:
            iniciPrestec = selectedDate
            fiPrestec = iniciPrestec + dt.timedelta(days=15)
            lendingsUpdate(command[1], command[2], command[3], fiPrestec)
            books[command[1]]['estado'] = "en prestamo"
            print("Préstamo registrado, el libro se ha de regresar:", fiPrestec)
        else:
            print("ERROR: La fecha no puede ser anterior al día de hoy")
    else:
        print('ERROR: Fecha incorrecta.')

#Verificamos si el codigo está en el diccionario lendings o no
def checkLendings(code):
    if code in lendings:
        return False
    else:
        return True

#Se confirma que la longitud de command sea 4, en caso contrario muestra error
#Si el diccionario books está vacío, mostrará error.
#En caso de que un libro esté en préstamo, se mostrará error.
def startPrestec(command):
    if len(command) == 4:
        if not checkBooks(command[1]):
            if checkLendings(command[1]):
                calcDate(command)
            else:
                print("ERROR: No se puede prestar un libro que ya está en préstamo")
        else:
            print("ERROR: No hay libros registrados")
    else:
        print("ERROR: Número de argumentos incorrecto.")

#TO DO
#def endPrestec(command):
    #if len(command) == 3:
        #El libro tiene que existir y tiene que estar en préstamo para poderse regresar
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
             
#TO DO
#def listGenere:
    #tiene que mostrar los datos del género indicado

#TO DO
    #def maxLlibre(command):
        #tiene que mostrar los datos del libro que tien más páginas de la biblioteca

#TO DO
    #def stats(command):
        #tiene que mostrar el número de libros registrados, número de incidencias registradas y media de páginas por libro de la biblioteca

#TO DO
    #def info(command):
        #tiene que mostrar los libros que tiene en préstamo el alumno (si los tiene) y las incidencias que ha tenido.
