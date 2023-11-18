# Leemos el número de casos de prueba (entrada), que representa cuántos casos de prueba vamos a evaluar
k=int(input())
# Iteramos a través de cada caso de prueba
for z in range(k):
    # Leemos el valor "n" para este caso, que representa un número natural
    n=int(input())
    # Comprobamos si "n" es menor o igual a 0 (números naturales comienzan en 1)
    if n<=0:
        print("ELS NOMBRES NATURALS COMENCEN EN 1")
    else:
        # Inicializamos las variables "suma" y "producto" para calcular la suma y el producto de los números naturales
        suma=0
        producto=1
        # Iteramos a través de los números naturales desde 1 hasta "n"
        for i in range(1, n + 1):
            # Calculamos la suma acumulativa de los números naturales
            suma+=i  
            # Calculamos el producto acumulativo de los números naturales
            producto*=i  
        # Imprimimos la suma y el producto calculados
        print(f"SUMA: {suma} PRODUCTE: {producto}")
