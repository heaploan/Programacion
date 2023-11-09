# Solicita al usuario el número de casos a considerar.
casos = int(input("Introdueix el nombre de casos a considerar: ")) 
# Inicia un bucle que se repetirá 'casos' veces.
for i in range(casos):  
    # Solicita al usuario una línea de números y la divide en una lista de cadenas utilizando espacios como separador.
    numeros = input().split(" ")  
    # Inicializa la variable 'posicion' que se utilizará para rastrear si es el primer número.
    posicion = 0  
    # Inicializa la variable 'suma' para calcular la suma de los números.
    suma = 0  
    # Itera a través de los números en la lista 'numeros'.
    for i in numeros:  
        # Comprueba si no es el primer número.
        if posicion != 0:  
            # Convierte el número a entero y lo suma al acumulador 'suma'.
            suma += int(i)  
        else:
            # Si es el primer número, aumenta 'posicion' en 1 para indicar que ya hemos pasado el primer número.
            posicion += 1  
        # Imprime el valor acumulado de 'suma' en cada iteración.
        print(suma)  
