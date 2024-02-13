import validator as v
import persistance as p

# Este modulo se ha creado para gestionar la información del hotel.

# En esta funcion, leemos el archivo 'habitacions.txt', agregamos la habitación, comprobando si está en el diccionario y que el numero sea mayor a 0
# Recibimos el número de habitación, la capacidad y el precio.
def addRoom(roomNum, cap, price):
    dict = p.loadData("habitacio")
    if roomNum in dict:
        print("ERROR: Ya existe una habitación con el número indicado")
    else:
        if roomNum > 0:
            if v.checkcapacity(cap) and v.checkPrice(price):
                dict[roomNum] = {'cap': cap, 'price': price, 'disp': 'DISPONIBLE'}
                p.addRoomToFile(roomNum, cap, price)
                print("Habitacion registrada")
        else:
            print('ERROR: El número de la habitación tiene que ser mayor a 0')

# En esta funcion cargamos el archivo 'reserves.txt', verificamos su disponibilidad, el dni y el telefono
# En caso de todo estar en orden, se cambia el status de la habitación a OCUPADA y guardamos los datos en el archivo 'reserves.txt'
# Recibimos numero de habitación, nombre, apellidos, dni y telefono
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
        else: 
            print("ERROR: DNI incorrecto")
    
# En esta funcion terminamos o cancelamos la reserva.
# Si la habitación está ocupada, la cambia a BRUTA en caso de que el dia sea mayor a 0 y calcula el precio
# Si el dia es 0 vuelve a 'DISPONIBLE' sin coste.
# En caso de que alguno de los datos sea incorrecto, mostrará su respectivo error.
# Recibimos numero de habitación y dias
def endBooking(roomNum, day):
    dict = p.loadData('habitacio')
    if day.isdigit() or (day[0] == "-" and day[1:].isdigit()):
        d = int(day)
        if roomNum in dict:
            if dict[roomNum]['disp'] == 'OCUPADA':
                if d > 0:
                    price = dict[roomNum]['price']
                    pr = price
                    total = d * pr
                    p.updateRoomStatus(roomNum,'BRUTA')

                    p.updateBookingsFile(roomNum)
                    print(f"Precio total: {total:.2f}€. La habitación queda en espera del servicio de limpieza.")
                elif d == 0:
                    if dict[roomNum]['disp'] == 'OCUPADA':
                        p.updateRoomStatus(roomNum,'DISPONIBLE')
                        p.updateBookingsFile(roomNum)
                        print("Reserva cancelada. Sin costo. La habitación queda disponible")
                else:
                    print('ERROR: El número de días no puede ser negativo. Si quieres anular la reserva, indica numero de dias 0.')
            else:
                print("ERROR: esta habitación no está reservada")
        else: 
            print('No existe una habitación con el número indicado')
    else:
        print("ERROR: El día debe ser un número")

# En esta función cargamos el archivo 'habitacions.txt', comprobamos el numero de habitación.
# Si está y su estado es 'BRUTA', actualizamos el estado en el archivo '.txt' a DISPONIBLE.
# En caso de que alguno de los datos sea incorrecto, mostrará su respectivo error. 
# Recibimos numero de habitación
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

# En esta función cargamos habitacions.txt y reserva.txt para poder manejar los datos de ambos.
# Confirmamos que la habitación exista y si existe cogemos sus valores y los imprimimos.
# En caso de que alguno de los datos sea incorrecto, mostrará su respectivo error. 
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

# En esta funcion cargamos los datos de 'reserves.txt'
# Verificamos que el dni recibido sea el mismo que está en el diccionario e imprimimos su información y la habitación reservada.
# En caso de no haber clientes con ese DNI imprimirá su error y en caso de no haber reservas, mostrará que no hay reservas. 
# Recibimos el DNI
def infoDni(dni):
    dry = p.loadData('reserva')
    if dry != {}:
        cliente = False
        for key, value in dry.items():
            if value['dni'] == dni:
                if not cliente:
                    print(f"Dades del client:\t{value['last']} , {value['name']} - tfn: {value['phone']}")
                    cliente = True
                print(f"habitacio: {key}")
        if not cliente:
            print('ERROR: No se encontraron reservas asociadas a ese DNI')
    else:
        print('ERROR: No hay reservas')

# En esta funcion cargamos los datos de 'reserva'  
# En caso de no haber datos guardados en el archivo, nos avisará que no hay reservas, en caso contrario, imprimirá la información.
def reserves():
    dry = p.loadData('reserva')
    if dry:
        print('========\tRESERVES\t========')
        for key, value in dry.items():
            print(f"{key}: {value['dni']} - {value['name']} {value['last']} - {value['phone']}")
    else:
        print('ERROR: No hay reservas registradas')