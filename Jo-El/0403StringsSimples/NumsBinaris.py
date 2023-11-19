# Obtener el número de casos de prueba
casos = int(input())
# Iterar sobre cada caso de prueba
for i in range(casos):
    # Leer la línea de entrada y dividirla en partes
    entry = input().split()
    num1 = int(entry[0])
    operacion = entry[1]
    num2 = int(entry[2])
    # Realizar la operación correspondiente
    if operacion == "+":
        resultado = num1 + num2
    elif operacion == "-":
        resultado = num1 - num2
    # Inicializar variables para la conversión a binario
    resultadoBinario = 0
    potencia = 1
    # Verificar si el resultado es cero
    if resultado == 0:
        resultadoBinario = 0
    else: 
        # Convertir el resultado a binario manualmente
        while resultado > 0:
            # Obtener el bit actual del resultado
            bit = resultado % 2
            # Actualizar el resultadoBinario con el bit en la posición correcta
            resultadoBinario += bit * potencia
            # Dividir el resultado por 2 para avanzar al siguiente bit
            resultado //= 2
            # Multiplicar potencia por 10 para avanzar a la siguiente posición
            potencia *= 10
    # Imprimir el resultado en formato binario
    print(resultadoBinario)
