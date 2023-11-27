# Creamos un dicionario vacio
data = {}

# Pedimos al usuario que introduzca los datos.
nom = input("Introduce tu nombre: ")
edat = int(input("Introduce tu edad: "))
adreça = input("Introduce tu direccion: ")
telefon = int(input("Introduce tu numero de telefono: "))

# Guardamos los datos en el diccionario
data[nom] = nom
data[edat] = edat
data[adreça] = adreça
data[telefon] = telefon

# Mostramos los datos por pantalla
print(f"{nom} te {edat}, viu a {adreça} i el seu numero de telefon es {telefon}")