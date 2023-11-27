def validar(string):
    partes = string.split("@")
    if len(partes) == 2:
        izquierda, derecha = partes
        if izquierda and derecha and "." in derecha:
            return True
confirmacion = validar("apoloandrade1@hotmail.com")
if confirmacion:
    print("Es un correo electrónico")
else:
    print("No es un correo electrónico")