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
    if numDePaginas > 0:
        libros['páginas'] = numDePaginas
    else:
        print('ERROR: La cantidad de páginas no puede ser menor a 1')
    return libros
    
addLlibre()
print(libros)

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
    fechaPrestec = input('Introduce la fecha del préstamo en formato dd/mm/aaaa: ')
    fechaPrestec = fechaPrestec.replace('/', '-')
    partesFecha = fechaPrestec.split('-')
    dia = int(partesFecha[0])
    mes = int(partesFecha[1])
    año = int(partesFecha[2])
    diaRetorno = dia + 15
    mesRetorno = mes
    añoRetorno = año
    if diaRetorno > 31:
        diaRetorno -= 31
        mesRetorno +=1
    if mesRetorno > 12:
        mesRetorno -= 12
        añoRetorno += 1
    fechaFormateadaPrestamo = f"{año:04d}-{mes:02d}-{dia:02d}"
    fechaFormateadaRetorno = f"{añoRetorno:04d}-{mesRetorno:02d}-{diaRetorno:02d}"
    prestecs['Prestecs'] = {'fechaPrestamo': fechaFormateadaPrestamo, 'fechaRetorno': fechaFormateadaRetorno}

startPrestec()
print(prestecs) 