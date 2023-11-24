# Crear un diccionario vacío
dic = {}
# Solicitar al usuario el número de casos
casos = int(input())
# Iterar a través de la cantidad de casos ingresados
for i in range(casos):
    # Solicitar al usuario el nombre y la fecha de nacimiento y almacenar en el diccionario
    nombre = input()
    fechaNacimiento = input()
    dic[nombre] = fechaNacimiento
# Inicializar una cadena con el primer carácter '{'
resultado = '{'
# Inicializar una variable booleana para controlar si es el primer elemento
primerElemento = True
# Iterar sobre los elementos del diccionario
for nombre, fechaNacimiento in dic.items():
    # Verificar si es el primer elemento
    if primerElemento:
        primerElemento = False  # Cambiar el indicador de primer elemento a False después del primer elemento
    else:
        resultado += ', '  # Agregar una coma antes de cada elemento excepto el primero
    # Agregar el par clave=valor a la cadena resultado
    resultado += f'{nombre}={fechaNacimiento}'
# Agregar el último carácter '}'
resultado += '}'
# Imprimir el resultado
print(resultado)
# Solicitar al usuario un nombre para buscar en el diccionario
nombre1 = input()
# Verificar si el nombre ingresado está en el diccionario y, si es así, imprimir el valor correspondiente
if nombre1 in dic:
    print(dic[nombre1])