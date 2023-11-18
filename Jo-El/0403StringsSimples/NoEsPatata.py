# Se solicita al usuario ingresar el número de casos a evaluar
casos = int(input())
# Se utiliza un bucle for para iterar a través de cada caso
for i in range(casos):
    # Se solicita al usuario ingresar la entrada para cada caso y se almacena en la variable 'entry'
    entry = input().lower()   
    # Se convierte la entrada a minúsculas para hacer la comparación de manera insensible a mayúsculas/minúsculas   
    # Se verifica si la entrada es igual a "patata"
    if entry == "patata":
        # Si es igual, se imprime "Es Patata"
        print("Es Patata")
    else:
        # Si no es igual, se imprime "No es Patata"
        print("No es Patata") 
