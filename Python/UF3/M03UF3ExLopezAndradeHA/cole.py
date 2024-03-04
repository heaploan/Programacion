import validator as v
import persistance as p
import datetime as dt


def addAlta(dni, grau, nota, data):
    dicc = p.loadData()
    d = dni.upper()
    if dni in dicc:
        print("ERROR: Ya hay una inscripcion con el DNI indicado.")
    else:
        if dni not in dicc:
            if v.verificacioNif(d):
                n = v.floatVal(nota)
                if v.notaVal(n):
                    dicc[d] = {'Grau superior': grau, 'Nota': nota, 'Data': data}
                    p.addAltaToFile(d, grau, nota, data)
                    print("Alta realizada con éxito.")
                else:
                    print("ERROR: Nota inválida")

def baixa(dni):
    dicc = p.loadData()
    if dni.upper() in dicc:
        p.updateInscripcionsFile(dni.upper())
        print("Inscripción eliminada exitosamente.")
    else:
        print("No hay alumnos con el DNI indicado")

def llistat():
    dicc = p.loadData()
    if dicc != {}:
        for key, value in dicc.items():
                print(f"Grado:\t{value['data']}\t{key}\t{value['Nota']}{value['Grau superior']}")
        print(f"Nº total d'inscripcions: {len(dicc)}")
    else:
        print('ERROR: No hay grados')