# Recibe un parámetro en forma de texto
# Comprueba si el DNI es válido
# Comprueba si la letra es correcta
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

dni = input("Introduce un DNI: ")
print(verificacioNif(dni))