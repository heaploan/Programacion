import validator as v
import persistance as p
import datetime as dt


def addAlta(dni, grau, nota, data):
    dicc = p.loadData()
    if dni in dicc:
        print("ERROR: Ya hay una inscripcion con el DNI indicado.")
    else:
        if v.verificacioNif(dni):
            dicc[dni] = {'Grau superior': grau, 'Nota': nota, 'Data': data}
            p.addAltaToFile(dni, grau, nota, data)
            print("Alta realizada con éxito.")

def baixa(dni):
    dicc = p.loadData()
    if dni in dicc:
        p.updateInscripcionsFile(dni)
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