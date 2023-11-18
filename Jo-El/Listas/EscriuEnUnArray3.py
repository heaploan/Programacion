# Se crea una lista vacía llamada 'lista' para almacenar números ingresados por el usuario
lista = []
# Se inicializa la variable 'numero' en 0 para entrar al bucle
numero = 0
# Se utiliza un bucle while que continuará hasta que el usuario ingrese -1
while numero != -1:
    # Se solicita al usuario ingresar números separados por espacios y se almacenan en 'numeros'
    numeros = input().split()
    # Se utiliza un bucle for para iterar sobre cada número en 'numeros'
    for num in numeros:
        # Se convierte el número de cadena a entero
        numero = int(num)   
        # Si el número ingresado no es -1, se agrega a la lista 'lista'
        if numero != -1:
            lista.append(numero)
# Se imprime la lista completa después de que el usuario ingresa -1
print(lista)
# Se solicita al usuario ingresar un número entero 'n'
n = int(input())
# Se intenta imprimir el elemento en la posición 'n' de la lista 'lista'
print(lista[n])