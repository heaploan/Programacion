# Recibe un parámetro en forma de string
# Verifica si es un correo electrónico con un split separado por '@'
# Si en la parte izquierda hay contenido y en la derecha hay al menos un punto, es un correo, si no, no lo es.
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