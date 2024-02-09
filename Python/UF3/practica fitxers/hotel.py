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
                print(f"Precio total: {total}. La habitación queda en espera del servicio de limpieza.")
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


