import validator as v
import persistance as p

# Este modulo se ha creado para gestionar la información de los diccionarios.

def addRoom(roomNum, cap, price):
    dict = p.loadData("habitacio")
    if roomNum in dict:
        print("ERROR: Ya existe una habitación con el número indicado")
    else:
        if v.checkcapacity(cap) and v.checkPrice(price):
            dict[roomNum] = {'cap': cap, 'price': price, 'disp': 'DISPONIBLE'}
            p.addRoomToFile(roomNum, cap, price)
            print("Habitacion registrada")

def addBooking(roomNum, name, lastName, dni, phone):
    dict = p.loadData("reserva")
    if p.verAvailability(roomNum):
        if v.verificacioNif(dni):
            if v.verTelefon(phone):
                dict[roomNum] = {'name': name, 'last': lastName, 'dni': dni, 'phone': phone}
                p.addBookingToFile(roomNum, name, lastName, dni, phone)
                p.updateRoomStatus(roomNum,'OCUPADA')
                print("Reserva registrada")
            else:
                print("ERROR: numero incorrecto")

def endBooking(roomNum, day):
    dict = p.loadData('habitacio')
    d = int(day)
    if roomNum in dict:
        if dict[roomNum]['disp'] == 'OCUPADA':
            if d > 0:
                price = dict[roomNum]['price']
                pr = float(price)
                total = d * pr
                p.updateRoomStatus(roomNum,'BRUTA')
                p.updateBookingsFile(roomNum)
                print(f"Precio total: {total:.2f}. La habitación queda en espera del servicio de limpieza.")
            elif day == 0:
                if dict[roomNum]['disp'] == 'OCUPADA':
                    p.updateRoomStatus(roomNum,'DISPONIBLE')
                    p.updateBookingsFile(roomNum)
            else:
                print('ERROR: El número de días no puede ser negativo. Si quieres anular la reserva, indica numero de dias 0.')
        else:
            print("ERROR: esta habitación no está reservada")
    else: 
        print('No existe una habitación con el número indicado')

def cleaner(roomNum):
    dict = p.loadData('habitacio')
    if roomNum in dict:
        if dict[roomNum]['disp'] == 'BRUTA':
            p.updateRoomStatus(roomNum,'DISPONIBLE')
            print('Habitación limpia. Queda disponible')
        else:
            print('La habitación no está "BRUTA"')
    else:
        print("No existe una habitación con el número indicado")

def roomList():
    dry = p.loadData('habitacio')
    dry2 = p.loadData('reserva')
    if dry:
        print("========\tINFO HOTEL\t========")
        print("Hab\tCap\tEstat\t")
        disp = 0
        ocu = 0
        brut = 0
        for key, value in dry.items():
            print(f"{key}\t{value['cap']}\t{value['disp']}", end=" ")
            if key in dry2:
                print(f"\t==> Client: {dry2[key]['name']} {dry2[key]['last']}")
            else:
                print()
            if value['disp'] == 'DISPONIBLE':
                disp += 1
            elif value['disp'] == 'OCUPADA':
                ocu += 1
            elif value['disp'] == 'BRUTA':
                brut += 1
        print('=========================================')
        print(f'Total habitacions: {len(dry)}')
        print(f'Disponibles: {disp}  Ocupades: {ocu}  Brutes: {brut}')
    else: 
        print("ERROR: No hay habitaciones registradas")

def reserves():
    dry = p.loadData('reserva')
    if dry:
        print('========\tRESERVES\t========')
        for key, value in dry.items():
            print(f"{key}: {value['dni']} - {value['name']} {value['last']} - {value['phone']}")
    else:
        print('ERROR: No hay reservas registradas')

def infoDni(dni):
    dry = p.loadData('reserva')
    if dry:
        cliente = False
        for key, value in dry.items():
            if value['dni'] == dni:
                if not cliente:
                    print(f"Dades del client:\t{value['last']} , {value['name']} - tfn: {value['phone']}")
                    cliente = True
                print(f"habitacio: {key}")
        if not cliente:
            print('ERROR: No se encontraron reservas asociadas a ese DNI')
    
                