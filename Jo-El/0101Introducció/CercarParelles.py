# Solicita al usuario que ingrese el primer número
n1 = int(input())
# Solicita al usuario que ingrese el segundo número
n2 = int(input())
# Solicita al usuario que ingrese el tercer número
n3 = int(input())
# Verifica si al menos dos de los números son iguales
if n1 == n2 or n2 == n3 or n1 == n3:
    # Imprime "SI" si al menos dos números son iguales
    print("SI")
else:
    # Imprime "NO" si los tres números son distintos
    print("NO")