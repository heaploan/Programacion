# Escribir un programa que pida al usuario un número entero
# y muestre por pantalla si es par o impar.
number = int(input("Introduce un numero entero: "))
if number % 2 == 0:
    print(f"El número {number} es par")
else:
    print(f"El número {number} es impar")