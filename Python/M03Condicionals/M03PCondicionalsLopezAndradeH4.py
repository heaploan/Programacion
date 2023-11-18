#he colocado las variables de los instrumentos para que luego muestre la informacion al ser llamadas.
guitarra=696
piano=718
bateria=256
saxo=310
#solo he puesto input ya que lo unico que pedimos que sea introducido es texto.
instrumentoDeseado=input("Introduce el instrumento del que necesites las partituras (guitarra, piano, bateria y saxo): ")
#hemos llamado la variable del contenido que hemos pedido para que si es igual a alguno de los instrumentos
#ponga las partituras que hay de dicho instrumento.
if instrumentoDeseado=="guitarra":
    print(f"La guitarra tiene {guitarra} partituras")
#elif siempre va ligado al if y es para indicar otro contenido referente a lo mismo.
elif instrumentoDeseado=="piano":
    print(f"El piano tiene {piano} partituras")
elif instrumentoDeseado=="bateria":
    print(f"La bateria tiene {bateria} partituras")
elif instrumentoDeseado=="saxo":
    print(f"La bateria tiene {saxo} partituras")
#he colocado este else es para indicar el error al introducir el instrumento indicado.
else:
    print("Error. No es ninguno de los instrumentos disponibles")