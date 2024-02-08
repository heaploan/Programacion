import sys as s
# Este modulo está creado para validar el comando que se escribe.


def commandVal(args, n):
    if len(args) == n:
        return True
    else:
        print('ERROR: número de argumentos incorrecto')
