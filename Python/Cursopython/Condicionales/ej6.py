# Los alumnos de un curso se han dividido en dos groupos A y B de acuerdo al sexo y el nombre.
# El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N
name = input("¿Cuál es tu nombre? ")
gender = input("Cual es tu sexo (M o H)? ")
if (gender == "M" and name.lower() < "m") or (gender  == "H" and name.lower() > "n"):
    group = "A"
else:
    group = "B"
print(f"Tu groupo es {group}")