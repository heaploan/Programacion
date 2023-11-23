# Lee el número de casos de prueba
casos = int(input())
# Itera sobre cada caso de prueba
for i in range(casos):
    # Lee la palabra para el caso actual
    string = input()
    # Inicializa la variable que indica si hay letras seguidas
    seguidas = False
    # Itera sobre la palabra para verificar si hay letras consecutivas iguales
    for j in range(len(string) - 1):
        # Compara si la letra actual es igual a la siguiente
        if string[j] == string[j + 1]:
            seguidas = True
    # Imprime "SI" si se encontraron letras seguidas, "NO" en caso contrario
    if seguidas:
        print("SI")
    else:
        print("NO")