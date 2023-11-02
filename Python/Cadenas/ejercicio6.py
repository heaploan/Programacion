#creamos la variable password pidiendo una contraseña
password=input("Introduce una contraseña: ")
#creamos la variable oculto para cambiar los todos valores de password
oculto="*" * len(password)
#imprimimos oculto y muestra ya los cambios a password.
print(oculto)