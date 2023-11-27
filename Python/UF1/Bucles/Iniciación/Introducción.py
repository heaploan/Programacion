# 1. Pide dos números al usuario. Guarda los números en variables."
# llama las variables a y b. Muestra los números por pantalla. 
# Calcula la suma, resta, multiplicación y divisón de los dos números anteriores.
# Muestra los resultados por pantalla.
a = int(input("Introduce un número: "))
b = int(input("Introduce otro número: "))
print("El número guardado en la variable a es: ", a)
print("El número guardado en la variable b es: ", b)
suma = a + b
print("El resultado de la suma: ", suma)
resta = a - b
print("El resultado de la resta: ", resta)
multiplicacion = a * b
print("El resultado de la multiplicación: ", multiplicacion)
division = a / b
print("El resultado de la división: ", division)
# 2. Escribe el codigo que intercambie dos variables anteriores utilizando una tercera variable 'c'
# Muestra el valor de cada variable antes y después del cambio.
print(f'Valor de a: {a}')
print(f'Valor de b: {b}')
# En python se puede hacer a, b = b, a pero en otros lenguajes se tiene que usar otra variable 'c'
c = a
a = b
b = c
print("¡Intercambio hecho!")
print(f'Valor de a: {a}')
print(f'Valor de b: {b}')
# 3. Escribe el código que resuelva el siguiente cálculo con las variables del ejercicio 2.
# ha de ir mostrando los cálculos paso a paso mostrando los resultados parciales y finalmente el resultado de la operación.
# El resultado final del paso a paso y de la operación entera ha de coincidir.
print('a + b / 2 * (a + b)')
print(f'{a} + {b} / 2 * ({a} + {b})')
print(f'{a} + ',b / 2, '*' ,(a + b))
print(f'{a} + ',b / 2 * (a + b))
print(a + b / 2 * (a + b))

# 4. Pide un número al usuario. Muestra su numero anterior y posterior por pantalla.
numero = int(input("Ingresa un número: "))
print(f"El número anterior a {numero} es {numero - 1} y el posterior es {numero + 1}")

# 5. Pide cuatro notas al usuario entre 0 y 10. Calcula y muestra su media.
notas = []
for i in range(4):
    nota = (float(input("Ingresa 4 notas: ")))
    if 0 <= nota <= 10:
        notas.append(nota)
media = sum(notas) / len(notas)
print("La media es: ", media)