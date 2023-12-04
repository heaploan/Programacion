# Recibe un parámetro y calcula el factorial de este.
# Si es diferente a 0 y mayor a 1 calcula el factorial
# Si es 1 devuelve 1
def CalcularFactorial(num1):
    if num1 < 0:
        return 1
    else: 
        factorial = 1
        for i in range(1, num1 + 1):
            factorial *= i
        return factorial

resultado = CalcularFactorial(0)
print(resultado)


# Se puede hacer de otra forma y es recursiva, aqui un ejemplo
"""def factorial(n):
    if n == 1:
        return 1
    resultat = n * factorial(n - 1)
    return resultat"""