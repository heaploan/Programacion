# Se solicita al usuario ingresar la cantidad de casos que se evaluarán
casos = int(input())
# Se inicia un bucle para cada caso
for i in range(casos):
    # Se solicita al usuario ingresar el valor de k para el caso actual
    k = int(input())  
    # Se solicita al usuario ingresar la lista de números separados por espacios
    numeros = input().split() 
    # Se solicita al usuario ingresar el número p que se contará en la lista
    p = int(input()) 
    # Inicializa el contador de apariciones del número p en la lista
    apariciones = 0
    # Itera a través de cada número en la lista
    for num in numeros:
        # Compara el número actual con el número p
        if int(num) == p:
            # Si son iguales, incrementa el contador de apariciones
            apariciones += 1  
    # Imprime la cantidad de apariciones del número p en la lista actual
    print(apariciones)
