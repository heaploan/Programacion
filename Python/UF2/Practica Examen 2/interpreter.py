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
        print('ERROR: ¡Número de argumentos incorrecto')

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
    else: 
        print("ERROR: Número de argumentos incorrecto.")

#TO DO
#tiene que mostrar los libros que están en préstamo
#tiene que indicar los que estén fuera de terminio, es decir, que ya ha pasado la fecha de devolución y aún no se ha regresado.
def listPrestecs(command):
    if len(command) == 1:
        inLendings(command)
    else:
        print('ERROR: Número de argumentos incorrecto')

#Tiene que mostrar los datos del género indicado
def listGenere(command):
    if len(command) == 2:
        checkGenere(command)
    else: 
        print('ERROR: Número de argumentos incorrecto.')
              
#Tiene que mostrar los datos del libro que tien más páginas de la biblioteca
def maxLlibre(command):
    if len(command) == 1:
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
    else:
        print("ERROR: Número de argumentos incorrecto.")

def stats(command):
        #tiene que mostrar el número de libros registrados, número de incidencias registradas y media de páginas por libro de la biblioteca
    if len(command) == 1:
        media = getMedia()
        incidences = getTotalIncidences()
        prestamos = getPrestamos()
        print(f"Media de páginas por libro: {media}")
        print(f"Total de incidencias: {incidences}")
        print(f"Prestamos: {prestamos}")
    else:
        print('ERROR: número de argumentos incorrecto.')

#Tiene que mostrar los libros que tiene en préstamo (si los tiene) y las incidencias que ha tenido (si las ha tenido)
def info(command):
    if len(command) == 2:
        infoStudent(command[1])
        studentIncidence(command[1])
    else:
        print("ERROR: número de argumentos incorrecto.")
    

