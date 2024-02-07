def checkParametros(command, n):
    if len(command) == n:
        return True
    else:
        print(f"ERROR: Número de argumentos incorrecto.")

def verificacioNif(nif):
    if len(nif) != 9:
        return False
    letra = nif[-1].upper()
    if not nif[:-1].isdigit() or not letra.isalpha():
        return False
    letrasValidas = 'TRWAGMYFPDXBNJZSQVHLCKE'
    controlLetra = int(nif[:-1]) % 23
    if letra != letrasValidas[controlLetra]:
        return False
    return True