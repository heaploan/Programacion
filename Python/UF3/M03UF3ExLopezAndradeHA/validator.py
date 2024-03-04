# Modulo creado para la validación de los comandos
# Se encargará de pasar los datos ya validados a los demás módulos.
import datetime as dt
import cole as c

def commandVal(args, n):
    if len(args) == n:
        return True
    else:
        print('ERROR: número de argumentos incorrecto')

def verificacioNif(dni):
    letrasValidas = 'TRWAGMYFPDXBNJZSQVHLCKE'
    if len(dni) != 9 and (not dni[:-1].isdigit() or not letra.isalpha()):
        print("ERROR: DNI incorrecto")
        return False
    controlLetra = int(dni[:-1]) % 23
    letra = dni[-1].upper()
    if letra != letrasValidas[controlLetra]:
        print("ERROR: DNI incorrecto")
        return False
    return True

def convertAlta(command):
    dni = command[2]
    gSup = command[3].upper()
    nota = command[4]
    data = command[5]
    c.addAlta(dni, gSup, nota, data)
    return dni, gSup, nota, data

def floatVal(num):
    fl = str(num).split('.')
    if len(fl) > 1:
        if fl[0].isdigit() and fl[1].isdigit():
            return float(num)
    else:
        if num.isdigit():
            return float(num)
    return False

def notaVal(nota):
    if nota >= 5 and nota <=10:
        return True
    return False

def grauVal(grau):
    if grau == 'AIF' or grau == 'TIL' or grau == 'MIN' or grau == 'DAM' or grau == 'ASIC':
        return True
    return False

def dateFormat(data):
    data = data.split("-")
    d = int(data[0])
    m = int(data[1])
    y = int(data[2])
    fecha = dt.date(y, m, d).strptime("%d-%m-%Y")
    return fecha

def dateVal(fecha):
    if fecha <= dt.date().today:
        return True
    return False

def getDni(command):
    dni = command[2]
    if verificacioNif(dni):
        c.baixa(dni)
    else:
        print('ERROR: DNI inválido')