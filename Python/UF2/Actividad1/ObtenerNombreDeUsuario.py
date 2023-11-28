# Obtiene los parámetros que se le pide al usuario en forma de string.
# Construye el nombre de usuario eliminando los espacios del nombre
# Agrega la longitud del apellido
# Agrega las tres primeras cifras del DNI
# Finalmente muestra la información introducida por el usuario.
# Así como el nombre de usuario creado con esta fórmula. 
def obtenirNomUsuari(nom, cognoms, dni):
    cifras = dni[:3]
    return nom.replace(" ", "") + str(len(cognoms)) + cifras

nom = input("Introdueix el teu nom: ")
cognoms = input("Introdueix el teu cognom: ")
dni = input("Introdueix el teu DNI sense lletra: ")

nomUsuari = obtenirNomUsuari(nom, cognoms, dni)
print(f"Nom: {nom}\nCognoms: {cognoms}\nDNI: {dni}\nUsuari: {nomUsuari}")
