import validator as v
import persistance as p
# Este modulo se ha creado para gestionar la información de los diccionarios.
dict = {}

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
                p.updateRoomStatus(roomNum)
                print("Reserva registrada")
            else:
                print("ERROR: numero incorrecto")