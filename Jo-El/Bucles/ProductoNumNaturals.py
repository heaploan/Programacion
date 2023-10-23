k = int(input())
for z in range(k):
    n = int(input())
    if n <= 0:
        print("ELS NOMBRES NATURALS COMENCEN EN 1")
    else:
        suma = 0
        producto = 1
        for i in range(1, n + 1):
            suma += i
            producto *= i
        print(f"SUMA: {suma} PRODUCTE: {producto}")