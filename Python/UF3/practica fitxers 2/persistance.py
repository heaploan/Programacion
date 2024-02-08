import os

# Este modulo está hecho para gestionar los ficheros y su contenido.
folderName = "./dades"
roomsFile = folderName + "/habitacions.txt"
bookingsFile = folderName + "/reserves.txt"

def roomsFolderPath(type):
    dict = {}
    if os.path.exists(folderName):
        if type == 'habitacio':
            if os.path.exists(roomsFile):
                    f = open(roomsFile, "r")
                    lineas = f.readlines()
                    for linea in lineas:
                        data = linea.strip().split(",")
                        roomNum = data[2]
                        cap = data[3]
                        price = data[4]
                        dict[roomNum] = {'cap': cap,
                                        'price': price,
                                        'disp': "DISPONIBLE"}
        elif type == 'reserva':
                if os.path.exists(bookingsFile):
                    f = open(bookingsFile, "r")
                    lines = f.readlines()
                    for line in lines:
                        data = line.strip().split(',')
                        roomNum = data[2]
                        name = data[3]
                        lastName = data[4]
                        dni = data[5]
                        phone = data[6]
                        dict[roomNum] = {'name': name,
                                            'last name': lastName,
                                            'dni': dni,
                                            'phone': phone}
    else:
        os.mkdir(folderName)
        return dict


