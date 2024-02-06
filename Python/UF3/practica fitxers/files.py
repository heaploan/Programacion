import hotel
import os

def RoomsFile():
    folderName = "dades"
    roomsFilePath = "./" + folderName + "/habitacions.txt"
    if os.path.exists(folderName):
    #miramos si existe el fichero de datos.
        if os.path.exists():
            #abrir para leer los datos.
            f = open(roomsFilePath, "r")
            lineas = f.readlines()
            #Se recorre cada lina
            for linea in lineas:
            #Hacemos separación de las líneas con ,
                data = linea.split(",")
            #Quitamos el \n que se encuentra en la segunda posición de linea.
                number = data[1].replace("\n", "")
            #convertimos la nota en int
                num = int(number)
                capacity = int(data[2])
                price = int(data[3])
            #agregamos la habitación = el numero de habitación, la capacidad y el precio (ya convertidos)
                hotel.rooms[num] = {'capacidad': capacity, 
                                    'precio': price}
    else:
        os.mkdir(folderName)

