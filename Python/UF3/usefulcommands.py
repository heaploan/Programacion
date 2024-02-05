import sys
import os
#Verifica la longitud del comando.
dictionary = {}

def checkParametros(command, n):
    if len(command) == n:
        return True
    else:
        print(f"ERROR: Número de argumentos incorrecto.")

def checkArguments():
    if len(sys.argv) < 3:
        print("ERROR: se esperaban al menos 2 argumentos.")

#Verifica si el diccionario está vacío o no.
def checkContent():
    if dictionary == {}:
        return True
    else:
        return False
    
#Cuenta el largo del contenido del diccionario y lo devuelve.
def getLen():
    if dictionary:
        return len(dictionary)
    else:
        return 0

#detectar fin de fichero
def fileEnd():
    EOF = False
    while not EOF:
        #character = file.read(1) 
        #if character == "": #Si el elemento está vacío
            EOF = True