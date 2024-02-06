import persistence as p
from interpreter import *

rooms = {}
bookings = {}

# Habitación -> nº(id), capacidad, precio por día, estado (DISPONIBLE, BRUTA, OCUPADA)
 
# Reserva -> nom, cognom, dni, telefon

# La aplicación tiene que ser persistente, los datos tienen que quedar guardados en ficheros
# de manera que cuando se cierre, la aplicación no pierda los datos registrados
# y se puedan cargar a la siguiente ejecución. Los datos se tienen que guardar
# en una carpeta llamada dades, dentro tienen que haber dos archivos
# uno con los datos de habitaciones y otro con reservas.
# se tiene que guardar con el mismo formato los dos archivos .txt.

# Para comodidad, no existirá menú y la aplicació funcionará por línea de comandos.
# ejemplo: py ./main.py afegir habitacio 100 1 45.90
# en el archivo de habitacio tendria que quedar: 100, 1, 45.90, DISPONIBLE

def addRoom(command):
    # Verificamos si los parámetros son correctos
    if checkParametros(command, 6):
        # Cargamos las habitaciones desde el archivo
        p.loadRoomsFromFile()
        # Extraemos el número de habitación de los argumentos y lo convertimos a entero, es necesario que lo sea para poder hacer el if siguiente.
        roomNum = int(command[3])
        # Verificamos si la habitación ya está en el diccionario de habitaciones
        if roomNum not in rooms:
            # Si la habitación no está en el diccionario, la añadimos
            rooms[roomNum] = {'capacitat': command[4], 'preu': command[5], 'estat': 'DISPONIBLE'}
        # Llamamos a la función para añadir la habitación al archivo
        p.addRoomToFile(command)


