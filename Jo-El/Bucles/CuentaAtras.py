# Pedimos al usuario que ingrese un número y lo almacenamos en la variable "numero".
numero = int(input())
# Verificamos si el número ingresado es mayor o igual a cero.
if numero >= 0:
    # Si el número es mayor o igual a cero, entramos en este bucle for.
    # El bucle for recorre un rango de números desde "numero" hasta -1 con paso -1.
    # Esto significa que empezará desde el número ingresado por el usuario y se irá
    # decrementando en 1 en cada iteración hasta llegar a -1.
    for i in range(numero, -1, -1):
        # En cada iteración del bucle, imprimimos el valor de "i" sin saltar de línea.
        # La opción "end" se utiliza para especificar el carácter que se imprimirá al
        # final de cada impresión, en este caso, no se imprimirá un salto de línea
        # (end="").
        print(i, end="")