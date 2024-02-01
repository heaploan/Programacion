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
        getBooksList()
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
        getMaxPages()
    else:
        print("ERROR: Número de argumentos incorrecto.")

def stats(command):
        #tiene que mostrar el número de libros registrados, número de incidencias registradas y media de páginas por libro de la biblioteca
    if len(command) == 1:
        printStats()
    else:
        print('ERROR: número de argumentos incorrecto.')

#Tiene que mostrar los libros que tiene en préstamo (si los tiene) y las incidencias que ha tenido (si las ha tenido)
def info(command):
    if len(command) == 2:
        infoStudent(command[1])
        studentIncidence(command[1])
    else:
        print("ERROR: número de argumentos incorrecto.")
    

