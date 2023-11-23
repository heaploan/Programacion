# Solicita al usuario ingresar la cantidad de casos a evaluar
casos = int(input())
# Inicia un bucle que se ejecutará la cantidad de veces especificada por el usuario
for i in range(casos):
    # Solicita al usuario ingresar la hora de introducción del video en formato de 12 horas (ej. 10:30 AM)
    horaIntroduccion = input()
    # Solicita al usuario ingresar la hora en que se produce el golpe en formato de 12 horas (ej. 12:45 PM)
    horaGolpe = input()
    # Solicita al usuario ingresar la duración de la mayonesa en formato de horas y minutos (ej. 0:45)
    tiempoMayonesa = input()
    # Condicional para convertir la hora de introducción a formato de 24 horas
    if horaIntroduccion[-2:] == "PM" and horaIntroduccion[:2] != "12":
        horaIntroduccion24H = int(horaIntroduccion[:2]) + 12
    else:
        horaIntroduccion24H = int(horaIntroduccion[:2])
    # Condicional para convertir la hora del golpe a formato de 24 horas
    if horaGolpe[-2:] == "PM" and horaGolpe[:2] != "12":
        horaGolpe24H = int(horaGolpe[:2]) + 12
    else:
        horaGolpe24H = int(horaGolpe[:2])
    # Obtención de los minutos de la hora de introducción
    if ':' in horaIntroduccion:
        minutos_introduccion = int(horaIntroduccion[3:5])
    else:
        minutos_introduccion = 0
    # Obtención de los minutos de la hora del golpe
    if ':' in horaGolpe:
        minutosGolpe = int(horaGolpe[3:5])
    else:
        minutosGolpe = 0
    # Cálculo del tiempo total en minutos desde la introducción hasta el golpe
    tiempoTotal = (horaGolpe24H - horaIntroduccion24H) * 60 + (minutosGolpe - minutos_introduccion)
    # Obtención de las horas y minutos de la duración de la mayonesa
    tiempoMayonesaHoras, tiempoMayonesaMinutos = int(tiempoMayonesa.split(':')[0]), int(tiempoMayonesa.split(':')[1])
    # Compara si el tiempo total es mayor o igual al tiempo de duración de la mayonesa
    if tiempoTotal >= tiempoMayonesaHoras * 60 + tiempoMayonesaMinutos:
        print("SI")
    else:
        print("NO")
