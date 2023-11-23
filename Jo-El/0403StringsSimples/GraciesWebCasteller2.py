# Se lee la cantidad de casos que se evaluarán
casos = int(input())
# Bucle principal para cada caso
for i in range(casos):
    # Se leen las listas de palabras para cada caso
    palabras1, palabras2 = input().split(), input().split()
    # Se obtiene la longitud de ambas listas de palabras
    lenPalabras1, lenPalabras2 = len(palabras1), len(palabras2)
    # Se verifica si las listas de palabras tienen la misma longitud
    if lenPalabras1 != lenPalabras2:
        print("WEBCASTELLER ESTA TRAVIESO HOY")
    else:
        # Inicialización de contador para coincidencias totales
        total = 0  
        # Bucle para comparar palabras en las listas
        for j in range(lenPalabras1):
            # Inicialización de variables para la comparación de palabras
            coincidencias = 0
            # Determina la longitud de la palabra más larga
            if len(palabras1[j]) > len(palabras2[j]):
                maxPalabra = len(palabras1[j])
            else:
                maxPalabra = len(palabras2[j])        
            # Bucle para comparar letras en las palabras
            for k in range(maxPalabra):
                # Se verifica que el índice k esté dentro de los límites de las palabras
                if k < len(palabras1[j]) and k < len(palabras2[j]):
                    # Se compara cada letra en las palabras
                    if palabras1[j][k] == palabras2[j][k]:
                        coincidencias += 1         
            # Se verifica si más del 50% de las letras coinciden
            if maxPalabra / 2 <= coincidencias:
                total += 1     
        # Se verifica si todas las palabras tienen suficientes coincidencias
        if total == lenPalabras1: 
            print("GRACIES WEBCASTELLER")
        else:  
            print("WEBCASTELLER ESTA TRAVIESO HOY")