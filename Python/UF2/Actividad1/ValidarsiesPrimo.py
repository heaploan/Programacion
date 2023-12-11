# Recibe un parámetro en forma de número
# Comprueba si es un numero primo o no.
def calculo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True
        
numero = int(input("Introduce un número entero positivo: "))
result = calculo(numero)
if numero == 1:
    print(False)
else:
    print(result)