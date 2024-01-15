# dato = input('Ingrese dato: ')

# lista = ['hola', 'mundo', 'chanchito', 'feliz', 'dragones']

# if lista.count(dato) > 0:
#     print('El dato existe:', dato)
# else:
#     print('El dato no existe: ', dato)

# Solicitar al usuario que ingrese el primer número
primero = input('Ingrese primer número: ')

# Intentar convertir el primer número a entero con manejo de excepciones
try:
    primero = int(primero)
except:
    # Si la conversión falla, asignar 'chanchito feliz' a primero
    primero = 'chanchito feliz'

# Verificar si el primer número no es un entero e imprimir un mensaje de error
if primero == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()

# Solicitar al usuario que ingrese el segundo número
segundo = input('Ingrese segundo número: ')

# Intentar convertir el segundo número a entero con manejo de excepciones
try:
    segundo = int(segundo)
except:
    # Si la conversión falla, asignar 'chanchito feliz' a segundo
    segundo = 'chanchito feliz'

# Verificar si el segundo número no es un entero e imprimir un mensaje de error
if segundo == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()

# Solicitar al usuario que ingrese la operación a realizar
simbolo = input('Ingrese operación: ')

# Realizar la operación según el símbolo ingresado
if simbolo == '+':
    print('Suma: ', primero + segundo)
elif simbolo == '-':
    print('Resta: ', primero - segundo)
elif simbolo == '*':
    print('Multiplicación: ', primero * segundo)
elif simbolo == '/':
    print('División: ', primero / segundo)
else:
    print('El símbolo ingresado no es válido')