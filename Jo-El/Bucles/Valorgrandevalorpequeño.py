# Leemos el primer número "num" (entrada)
num=int(input())
# Inicializamos las variables "numMin" y "numMax" con el primer número leído
numMin=num
numMax=num
# Iniciamos un bucle while que se ejecutará mientras "num" sea diferente de 0
while num!=0:
    # Leemos un nuevo número "num"
    num=int(input()) 
    # Comprobamos si el nuevo número es diferente de 0
    if num!=0:
        # Comprobamos si el nuevo número es menor que el valor actual de "numMin"
        if num < numMin:
            numMin=num  # Si es menor, actualizamos "numMin" con el nuevo valor
        # Comprobamos si el nuevo número es mayor que el valor actual de "numMax"
        if num>numMax:
            numMax=num  # Si es mayor, actualizamos "numMax" con el nuevo valor      
        # Imprimimos los valores actuales de "numMax" y "numMin" en cada iteración
        print(numMax, numMin)
# El bucle while termina cuando se ingresa un número igual a 0
# En ese punto, el programa muestra el resultado final (el valor máximo y mínimo)
