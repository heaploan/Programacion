import datetime

libros = {}
prestecs = {}

def addLlibre():
    codi = input('Introduce el código: ')
    if codi in libros:
        print('ERROR: El código ya existe')
    else:
        libros['codi'] = codi
    titol = input('Introduce el título: ')
    libros['títol'] = titol
    autor = input('Introduce el autor: ')
    libros['autor'] = autor
    genere = input('Introduce el género: ')
    libros['genere'] = genere
    numDePaginas = int(input('Introduce el número de páginas: '))
    if numDePaginas <= 0:
        libros['páginas'] = numDePaginas
    else:
        print('ERROR: La cantidad de páginas no puede ser menor a 1')
        return
    
def startPrestec():
    codiDelLlibre = input('Introduce el código del libro: ')
    if codiDelLlibre in libros['codi']:
        prestecs['codiLlibre'] = codiDelLlibre
    else:
        print('ERROR: El código no existe.')
    nomAlumne = input('Introduce el nombre del alumno: ')
    if ' ' in nomAlumne:
        print('ERROR: Solo hay que introducir un nombre')
    else:    
        prestecs['Alumne'] = nomAlumne