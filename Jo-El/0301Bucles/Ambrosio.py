# Solicita al usuario un valor de entrada que determinará cuántas veces se repetirá el bucle for.
entry = int(input())
# Comienza un bucle for que se ejecutará 'entry' veces.
for i in range(entry):
    # Solicita al usuario un número 'num' en cada iteración del bucle.
    num=int(input())
    # Inicializa una variable 'n2' en 0 para acumular la suma de los cuadrados.
    n2=0
    # Inicia un segundo bucle for que va desde 1 hasta 'num' (inclusive).
    for z in range(1, num + 1):
        # Calcula el cuadrado de 'z' y lo suma a 'n2'.
        n2+=z**2
    # Imprime el valor acumulado de 'n2' después de calcular la suma de cuadrados.
    print(n2)