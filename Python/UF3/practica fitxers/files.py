from hotel import *
import os


# def roomsFile():
#     rooms = {}
#     folderName = "dades"
#     roomsFilePath = "./" + folderName + "/habitacions.txt"
#     if os.path.exists(folderName):
#     #miramos si existe el fichero de datos.
#         if os.path.exists(roomsFilePath):
#             #abrir para leer los datos.
#             f = open(roomsFilePath, "r")
#             lineas = f.readlines()
#             #Se recorre cada lina
#             for linea in lineas:
#             #Hacemos separación de las líneas con ,
#                 data = linea.strip().split(",")
#             #Quitamos el \n que se encuentra en la segunda posición de linea.
#                 number = int(data[1])
#                 capacity = int(data[2])
#                 price = float(data[3])
#             #agregamos la habitación = el numero de habitación, la capacidad y el precio (ya convertidos)
#                 rooms[number] = {'capacidad': capacity, 
#                                'precio': price}
#     else:
#         os.mkdir(folderName)

# def bookingsFile():
#     folderName = "dades"
#     bookingsFilePath = "./" + folderName + "/reserves.txt"
#     if os.path.exists(folderName):
#     #miramos si existe el fichero de datos.
#         if os.path.exists():
#             #abrir para leer los datos.
#             f = open(bookingsFilePath, "r")
#             lineas = f.readlines()
#             #Se recorre cada lina
#             for linea in lineas:
#             #Hacemos separación de las líneas con ,
#                 data = linea.strip().split(",")
#             #EL nombre está en la posición 0 de linea
#                 habitacio = data[2]
#                 nom = data[3]
#                 cognom = data[4]
#                 dni = data[5]
#                 tlf = data[6]
#                 bookings[habitacio] = {'nombre': nom,
#                                        'apellido': cognom,
#                                        'dni': dni,
#                                        'telefono': tlf}
#     else:
#         os.mkdir(folderName)