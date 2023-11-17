# Escribir un programa que pregunte el nombre del usuario en la consola
# Despues de que el usuario lo introduzca, muester por pantalla <NOMBRE> tiene <n> letras
# donde <NOMBRE> es el nombre del usuario en mayúsculas y <n> es el numero de letras que tiene el nombre
nombre = input("¿Cómo te llamas? ")
nombre.upper()
print(f"{nombre.upper()} tiene {len(nombre)} letras.")