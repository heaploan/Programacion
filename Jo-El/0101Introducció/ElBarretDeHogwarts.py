# Solicita al usuario que ingrese un nombre
name = input()
# Convierte el nombre a mayúsculas y capitaliza la primera letra
name = name.capitalize()
# Verifica a qué casa de Hogwarts pertenece según el nombre ingresado
if name == "Coratge":
    print("Gryffindor")
elif name == "Coneixement":
    print("Ravenclaw")
elif name == "Ambicio":
    print("Slytherin")
else:
    # Si el nombre no coincide con ninguno de los anteriores, asigna a la casa Hufflepuff
    print("Hufflepuff")