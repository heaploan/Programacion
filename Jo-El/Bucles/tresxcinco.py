# Leemos una entrada que contiene dos números separados por un espacio
entrada = input()
# Dividimos la entrada en una lista de elementos utilizando el espacio como separador
datos = entrada.split(" ")
# Convertimos los dos elementos de la lista en números enteros
n1 = int(datos[0])
n2 = int(datos[1])
# Iteramos n2 veces (repeticiones)
for i in range(n2):
    # Imprimimos el valor de n1 sin un salto de línea (end="")
    print(n1, end="")
# Imprimimos una línea en blanco para separar la salida
print()
