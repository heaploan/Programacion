#Verifica la longitud del comando.
dictionary = {}

def checkParametros(command, n):
    if len(command) == n:
        return True
    else:
        print(f"ERROR: Número de argumentos incorrecto.")
        return False

#Verifica si el diccionario está vacío o no.
def checkContent():
    if dictionary == {}:
        return True
    else:
        return False
    
#Cuenta el largo del contenido del diccionario y lo devuelve.
def getPrestamos():
    if dictionary:
        return len(dictionary)
    else:
        return 0
    
