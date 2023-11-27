def calculo(num):
    for n in range(2, num):
        if num % n == 0:
            return True
        else:
            return False
        
numero = int(input("Introduce un número entero positivo: "))
result = calculo(numero)
if numero == 2 or numero == 1:
    print(False)
else:
    print(result)