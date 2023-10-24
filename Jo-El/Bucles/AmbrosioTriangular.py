# Leemos el número de casos de prueba (entrada)
entry=int(input())
# Iteramos a través de cada caso de prueba
for i in range(entry):
    # Leemos el número de pisos para este caso
    floor=int(input())   
    # Inicializamos la variable "quantity" para llevar un seguimiento del número total de Ferrero Rocher
    quantity=0
    # Iteramos a través de cada nivel de la pirámide, desde el nivel 1 hasta el nivel "floor"
    for level in range(1, floor + 1):
        # Calculamos la cantidad de Ferrero Rocher en el nivel actual utilizando la fórmula del triángulo numérico
        ferreros=level*(level+1)//2
        # Agregamos la cantidad de Ferrero en el nivel actual al total
        quantity+=ferreros
    # Imprimimos la cantidad total de Ferrero Rocher necesarios para construir la pirámide
    print(quantity)