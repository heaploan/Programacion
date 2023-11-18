# Se solicita al usuario ingresar el número de casos a evaluar
casos = int(input())

# Se utiliza un bucle for para iterar a través de cada caso
for i in range(casos):
    # Se solicita al usuario ingresar los datos para cada caso y se almacenan en una lista llamada 'datos'
    datos = input().split()
    # Se extraen los valores de pozo, subida y bajada de la lista 'datos' y se convierten a enteros
    pozo = int(datos[0])
    subida = int(datos[1])
    bajada = int(datos[2])
    # Inicializamos las variables 'metrosSubidos' y 'dias' en 0 para el caso actual
    metrosSubidos = 0
    dias = 0
    # Se utiliza un bucle while para simular el ascenso y descenso del pozo
    while metrosSubidos < pozo:
        # Se incrementa la cantidad de metros subidos según la tasa de subida
        metrosSubidos += subida 
        # Se incrementa el número de días transcurridos
        dias += 1
        
        # Si la altura alcanzada es igual o mayor al pozo, se realiza el descenso
        if metrosSubidos >= pozo:
            metrosSubidos -= bajada
    # Se verifica si se ha salido del bucle porque se superó la altura del pozo
    if metrosSubidos >= pozo:
        # Se imprime el número de días transcurridos
        print(dias)
    else:
        # Si no se supera la altura del pozo, se imprime "NO"
        print("NO")