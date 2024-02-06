import os
import sys 

#--------------------------
#open(nombreArchivo,modo)
#--------------------------

#   *r: modo read o modo de lectura.
#       Si abro un archivo en este modo, y este no existe, lanza un error.

#   *w: modo write o modo escritura.
#       - Si el archivo no existe, lo crea.
#       - Si el archivo existe, los datos contenidos en el, son eliminados.

#   *a: modo add o modo añadir.
#       - Si el archivo no existe lo crea
#       - Si el archivo existe, los nuevos datos son guardados al final (los anteriores se mantienen.)

#Retorna un fichero.
#Con los archivos que más se trabajarán:
#       -'.txt'
#       -'.csv'

#file = open('rooms.txt', 'string') #cambiamos string por lo que se quiera hacer, 'r', 'w' o 'a'

#--------------------------
#readline()
#--------------------------

#Retorna la linea en la cual se encuentra el puntero.
#Una vez se aplica el readline, el puntero se mueve a la segunda línea
#Cuando abrimos el archivo por primera vez, el puntero estará en la primera línea.

#linea = file.readline()
#print(linea)

#Esto es un ejemplo (por eso no hay funciones ni modulos)
#Aplicación que registra notas de alumnos mediante linea de comandos.
#uso fitxers.py nombreAlumno nota (para añadir alumno)
#Uso fitxers.py list (para listar datos de los alumnos)

alumnos = {}


nombreCarpeta = "pesaos"
rutaArchivo = "./" + nombreCarpeta + "/notas.txt"
#Si existe la carpeta
if os.path.exists(nombreCarpeta):
    #miramos si existe el fichero de datos.
    if os.path.exists(rutaArchivo):
        #abrir para leer los datos.
        f = open(rutaArchivo, "r")
        lineas = f.readlines()
        #Se recorre cada lina
        for linea in lineas:
            #Hacemos separación de las líneas con -
            linea = linea.split("-")
            #EL nombre está en la posición 0 de linea
            nombre = linea[0]
            #Quitamos el \n que se encuentra en la segunda posición de linea.
            nota = linea[1].replace("\n", "")
            #convertimos la nota en int
            nota = int(nota)
            #el nombre del alumno = nota (ya convertida)
            alumnos[nombre] = nota
else:
    os.mkdir(nombreCarpeta)


command = sys.argv
if len(command) > 1:
    if len(command) == 2:
        if command[1].lower() == "list":
            #listado de alumnos
            if len("alumnos") == 0:
                print("No hay alumnos registrados")
            else:
                for nombre in alumnos:
                    print(nombre, "-", alumnos[nombre])
        else:
            print("Comando incorrecto") 


    elif len(command) == 3:
        nombre = command[1]
        nota = int(command[2])
        if nombre not in alumnos:
            #escribimos en el diccionario
            alumnos[nombre] = nota
            #escribimos en el fichero ("con a para añadir")
            f = open(rutaArchivo, "a")
            f.write(nombre + "-" + str(nota) + "\n")
            f.close()
            print("Alumno registrado")
        else:
            print("Ya existe un alumno con ese nombre")
else:
    print("Uso fitxers.py nombreAlumno nota (para añadir alumno)")
    print("Uso fitxers.py list (para listar datos de los alumnos)")
