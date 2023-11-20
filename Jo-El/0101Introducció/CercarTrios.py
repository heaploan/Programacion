# Solicita al usuario que ingrese el primer número
n1 = int(input())
# Solicita al usuario que ingrese el segundo número
n2 = int(input())
# Solicita al usuario que ingrese el tercer número
n3 = int(input())
# Verifica si los tres números son iguales
if n1 == n2 and n1 == n3:
    # Imprime "SI" si los tres números son iguales
    print("SI")
else:
    # Imprime "NO" si al menos uno de los números es diferente
    print("NO")
