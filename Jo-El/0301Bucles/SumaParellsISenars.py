# Leemos el número de casos de prueba (entrada), que representa cuántos casos vamos a evaluar
casos=int(input())
# Iteramos a través de cada caso de prueba
for i in range(casos):
    pares=0  # Inicializamos la variable "pares" para llevar un seguimiento de la suma de números pares
    impares=0  # Inicializamos la variable "impares" para llevar un seguimiento de la suma de números impares
    # Leemos un número "num" para este caso
    num=int(input())
    # Iteramos a través de los números desde 0 hasta "num" inclusive
    for z in range(num+1):
        # Comprobamos si el número "z" es par o impar
        if z%2==0:
            pares+=z  # Si es par, agregamos "z" a la suma de números pares
        else:
            impares+=z  # Si es impar, agregamos "z" a la suma de números impares
    # Imprimimos las sumas de números pares e impares para este caso
    print(f"PARELLS: {pares} SENARS: {impares}")
