# Solicita al usuario un número y lo almacena en la variable 'x'
x = int(input())
# Inicia un bucle 'while' que se ejecutará mientras 'x' sea mayor que 0
while x > 0:
    # Solicita al usuario otro número y lo almacena en la variable 'n'
    n = int(input())
    # Inicializa una variable 'factorial' en 1. Esta variable se usará para calcular el factorial de 'n'.
    factorial = 1
    # Comprueba si 'n' es diferente de 0, ya que el factorial de 0 es 1, y no es necesario realizar el bucle si 'n' es 0.
    if n != 0:
        # Inicia un bucle 'for' que se ejecutará desde 1 hasta 'n' (inclusive)
        for i in range(1, n+1):
            # Calcula el factorial multiplicando 'factorial' por 'i' en cada iteración
            factorial *= i
    # Imprime el valor de 'factorial', que es el factorial de 'n'
    print(factorial)
    #Sale del bucle con esta x.
    x -= 1
