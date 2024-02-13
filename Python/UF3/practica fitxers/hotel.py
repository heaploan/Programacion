import validator as v
import persistance as p

# Este modulo se ha creado para gestionar la información de los diccionarios.


def addRoom(roomNum, cap, price):
    # Carga los datos de habitaciones desde un archivo
    dict = p.loadData("habitacio")
    # Comprueba si la habitación ya existe en el diccionario
    if roomNum in dict:
        # Imprime un mensaje de error si la habitación ya existe
        print("ERROR: Ya existe una habitación con el número indicado")
    else:
        # Verifica la capacidad y el precio de la habitación
        if roomNum > 0:
            if v.checkcapacity(cap) and v.checkPrice(price):
                # Agrega la habitación al diccionario de habitaciones
                dict[roomNum] = {'cap': cap, 'price': price, 'disp': 'DISPONIBLE'}
                # Agrega la habitación al archivo de datos de habitaciones
                p.addRoomToFile(roomNum, cap, price)
                # Imprime un mensaje de éxito
                print("Habitacion registrada")
        else:
            print('ERROR: El número de la habitación tiene que ser mayor a 0')

def addBooking(roomNum, name, lastName, dni, phone):
    # Carga los datos de reservas desde un archivo
    dict = p.loadData("reserva")
    # Verifica la disponibilidad de la habitación
    if p.verAvailability(roomNum):
        # Verifica el formato del DNI
        if v.verificacioNif(dni):
            # Verifica el formato del número de teléfono
            if v.verTelefon(phone):
                # Agrega la reserva al diccionario de reservas
                dict[roomNum] = {'name': name, 'last': lastName, 'dni': dni, 'phone': phone}
                # Agrega la reserva al archivo de datos de reservas
                p.addBookingToFile(roomNum, name, lastName, dni, phone)
                # Actualiza el estado de la habitación a OCUPADA
                p.updateRoomStatus(roomNum,'OCUPADA')
                # Imprime un mensaje de éxito
                print("Reserva registrada")
            else:
                # Imprime un mensaje de error si el número de teléfono es incorrecto
                print("ERROR: numero incorrecto")
        else: 
            print("ERROR: DNI incorrecto")
    

def endBooking(roomNum, day):
    # Carga los datos de habitaciones desde un archivo
    dict = p.loadData('habitacio')
    if day.isdigit() or (day[0] == "-" and day[1:].isdigit()):
        d = int(day)
        if roomNum in dict:
            if dict[roomNum]['disp'] == 'OCUPADA':
                if d > 0:
                    # Calcula el precio total de la estancia
                    price = dict[roomNum]['price']
                    pr = price
                    total = d * pr
                    # Actualiza el estado de la habitación a BRUTA
                    p.updateRoomStatus(roomNum,'BRUTA')
                    # Actualiza el archivo de reservas
                    p.updateBookingsFile(roomNum)
                    # Imprime el precio total y un mensaje informativo
                    print(f"Precio total: {total:.2f}€. La habitación queda en espera del servicio de limpieza.")
                elif d == 0:
                    if dict[roomNum]['disp'] == 'OCUPADA':
                        # Actualiza el estado de la habitación a DISPONIBLE si se cancela la reserva
                        p.updateRoomStatus(roomNum,'DISPONIBLE')
                        # Actualiza el archivo de reservas
                        p.updateBookingsFile(roomNum)
                        print("Reserva cancelada, la habitación queda disponible")
                else:
                    # Imprime un mensaje de error si el número de días es negativo
                    print('ERROR: El número de días no puede ser negativo. Si quieres anular la reserva, indica numero de dias 0.')
            else:
                # Imprime un mensaje de error si la habitación no está ocupada
                print("ERROR: esta habitación no está reservada")
        else: 
            # Imprime un mensaje de error si la habitación no existe
            print('No existe una habitación con el número indicado')
    else:
        print("ERROR: El día debe ser un número")
        
def cleaner(roomNum):
    # Carga los datos de habitaciones desde un archivo
    dict = p.loadData('habitacio')
    if roomNum in dict:
        if dict[roomNum]['disp'] == 'BRUTA':
            # Actualiza el estado de la habitación a DISPONIBLE si está BRUTA
            p.updateRoomStatus(roomNum,'DISPONIBLE')
            # Imprime un mensaje de éxito
            print('Habitación limpia. Queda disponible')
        else:
            # Imprime un mensaje de error si la habitación no está BRUTA
            print('La habitación no está "BRUTA"')
    else:
        # Imprime un mensaje de error si la habitación no existe
        print("No existe una habitación con el número indicado")

def roomList():
    # Carga los datos de habitaciones y reservas desde archivos en dos variables para usar los datos de ambos de ambos.
    dry = p.loadData('habitacio')
    dry2 = p.loadData('reserva')
    if dry:
        # Imprime información sobre las habitaciones y sus estados
        print("========\tINFO HOTEL\t========")
        print("Hab\tCap\tEstat\t")
        disp = 0
        ocu = 0
        brut = 0
        for key, value in dry.items():
            print(f"{key}\t{value['cap']}\t{value['disp']}", end=" ")
            # Imprime información adicional si la habitación está reservada
            if key in dry2:
                print(f"\t==> Client: {dry2[key]['name']} {dry2[key]['last']}")
            else:
                print()
            # Contabiliza las habitaciones por estado
            if value['disp'] == 'DISPONIBLE':
                disp += 1
            elif value['disp'] == 'OCUPADA':
                ocu += 1
            elif value['disp'] == 'BRUTA':
                brut += 1
        print('=========================================')
        # Imprime el total de habitaciones por estado
        print(f'Total habitacions: {len(dry)}')
        print(f'Disponibles: {disp}  Ocupades: {ocu}  Brutes: {brut}')
    else: 
        # Imprime un mensaje de error si no hay habitaciones registradas
        print("ERROR: No hay habitaciones registradas")

def infoDni(dni):
    # Carga los datos de reservas desde un archivo
    dry = p.loadData('reserva')
    if dry != {}:
        cliente = False
        # Busca reservas asociadas al DNI dado
        for key, value in dry.items():
            if value['dni'] == dni:
                # Imprime información del cliente y sus reservas asociadas
                if not cliente:
                    print(f"Dades del client:\t{value['last']} , {value['name']} - tfn: {value['phone']}")
                    cliente = True
                print(f"habitacio: {key}")
        if not cliente:
            # Imprime un mensaje de error si no se encontraron reservas asociadas al DNI dado
            print('ERROR: No se encontraron reservas asociadas a ese DNI')
    else:
        print('ERROR: No hay reservas')
    
def reserves():
    # Carga los datos de reservas desde un archivo
    dry = p.loadData('reserva')
    if dry:
        # Imprime información sobre las reservas realizadas
        print('========\tRESERVES\t========')
        for key, value in dry.items():
            print(f"{key}: {value['dni']} - {value['name']} {value['last']} - {value['phone']}")
    else:
        # Imprime un mensaje de error si no hay reservas registradas
        print('ERROR: No hay reservas registradas')