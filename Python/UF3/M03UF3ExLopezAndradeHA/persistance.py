import os
import validator as v

folderName = "./documentos"
inscripcionsPath = folderName + "/inscripcions.txt"
mediaPath = folderName + "/mitjana.txt"

def loadData():
    if not os.path.exists(folderName):
        os.mkdir(folderName)
    dicc = {}
    if os.path.exists(inscripcionsPath):
        f = open(inscripcionsPath, "r")
        for line in f:
            data = line.strip().split("/")
            if len(data) >= 4:
                dni = data[0]
                dicc[dni] = {'Grau superior': data[1], 'Nota': data[2], 'Data': data[3]}
    return dicc

def isDniInFile(dni):
    if os.path.exists(inscripcionsPath):
        f = open(inscripcionsPath, "r")
        for line in f:
            data = line.strip().split("/")
            if len(data) >= 1 and v.verificacioNif(data[0]) == dni:
                f.close()
                return True
        f.close()
    return False

def addAltaToFile(dni, grau, nota, data):
    if not os.path.exists(folderName):
        os.mkdir(folderName)
    if not os.path.exists(inscripcionsPath):
        f = open(inscripcionsPath, "a")
        f.write(f"{dni}/{grau}/{nota}/{data}\n")
        f.close()
    elif os.path.exists(inscripcionsPath):  # Crea el archivo si no existe
        if not isDniInFile(inscripcionsPath):
            f = open(inscripcionsPath, "a")
            f.write(f"{dni}/{grau}/{nota}/{data}\n")
            f.close()

def updateInscripcionsFile(dni):
    f = open(inscripcionsPath, "r")
    lines = f.readlines()
    f.close()
    f = open(inscripcionsPath, "w")
    for line in lines:
        data = line.strip().split('/')
        if data[0] != dni:
            f.write(line)
    f.close()