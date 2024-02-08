def checkParametros(command, n):
    if len(command) == n:
        return True
    else:
        print(f"ERROR: Número de argumentos incorrecto.")

def verificacioNif(nif):
    if len(nif) != 9:
        print("ERROR: DNI incorrecto")
        return False
    letra = nif[-1].upper()
    if not nif[:-1].isdigit() or not letra.isalpha():
        print("ERROR: DNI incorrecto")
        return False
    letrasValidas = 'TRWAGMYFPDXBNJZSQVHLCKE'
    controlLetra = int(nif[:-1]) % 23
    if letra != letrasValidas[controlLetra]:
        print("ERROR: DNI incorrecto")
        return False
    return True

def verTelefon(telefon):
    if telefon.isdigit() and len(telefon) == 9:
        return True
    else:
        return False
    
