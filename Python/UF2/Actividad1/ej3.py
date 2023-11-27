# Recibe un parámetro y calcula el factorial de este.
# Si es diferente a 0 y mayor a 1 calcula el factorial
# Si es 1 devuelve 1
def CalcularFactorial(num1):
    factorial = 1
    if num1 != 0:
        for i in range(1, num1 + 1):
            factorial *= i
        return factorial
    else:
        return 1

resultado = CalcularFactorial(7)
print(resultado)