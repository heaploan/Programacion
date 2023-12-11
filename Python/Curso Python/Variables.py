# VARIABLES

# Una variable es como una cajita que contiene un tipo de dato. 
# Declaramos una variable:
x = 5
y = "chanchito feliz"
# Print permite que se le puedan pasar multiples argumentos para imprimirlos en consola.
# llamamos las dos variables.
# print(x, y)
# A las variables se le pueden asignar distintos nombres más expresivos para saber de qué se trata
email = "chanchito@feliz.com"
# print(email)
# El nombre que se le da a las variables puede ser completamente arbitrario.
# Habrá que poner nombres que sean representativas de lo que uno está haciendo. 
# Se utilizamos camelcase para separar una palabra de la otra
miVar = "chanchito"
# se pueden asignar variables en mayusculas por lo general para asignar constantes o variables que no pueden cambiar su valor.
# no se pueden asignar variables que empiecen con números, siempre después de una letra. 
# Python también puede definir multiples variables en una sola línea.
a, b, c = 'lala', 'lele', 'lili'
# print(a, b, c)
valor1 = valor2 = valor3 = 'chanchito feliz'
# print(valor1, valor2, valor3)
# Python también nos deja hacer concatenación de strings (palabras)
inicio = 'Hola '
final = 'mundo'
# Para utilizar la concatenación se usa la variable y el símbolo de suma.
# De esta manera concatenamos las dos variables. 
# print(inicio + final)
# Si no se pusiera espacio, las dos palabras estarían completamente juntas.
# los strings se pueden crear con comillas simples o comillas dobles.
palabra = 'hola mundo' #string
oracion = "hola mundo comilla doble" #string
# en termino de programación un numero entero es sin decimales. 
entero = 20 # iteger (int)
conDecimales = 20.2 # float
complejo = 1j # numero complejo se define agregando una j 
# print(palabra, oracion, entero, conDecimales, complejo)

# LISTAS

# Una lista en python es una colección de datos o varios datos agrupados dentro de una lista. 
lista = ['Hola', 'Mundo', 'Chanchito feliz'] # Para definir una lista vacía se utilizan los paréntesis de corchetes.
lista2 = lista.copy() # este método copia la lista en lista2
lista.append('Chanchito triste') # Para agregar más elemenots a la lista, llamamos al método .append a la lista.
# el método de append cambia la lista sin necesidad de crear una nueva lista.  

# lista.clear() el método clear elimina todos los elementos dentro de la lista.
# print(lista, lista2)
# lista2 al ser una copia a una etapa anterior a lista solo contiene 1, 2, 3
# esto sucede por hacer el copy antes de agregar el valor 4 a la lista. 
# Podemos contar elementos y ver cuantas veces este se repite dentro de una lista
# Esto se puede hacer utilizando el método de count.
# print(lista, lista2.count(3))
# print(len(lista), len(lista2)) # la funcion len() cuenta la cantidad de elementos que se encuentran dentro de una lista.
largoLista = len(lista)
largoLista2 = len(lista2)
# print(largoLista, largoLista2) también se pueden crear variables y le asignamos el valor e imprimimos las variables.
# Podemos acceder a los elementos que tienen un arreglo
# print(lista[0]) # el primer elemento de una lista siempre es el 0
# print(lista[1])
# print(lista[2])
# Para eliminar elementos de una lista

# Metodo pop()

# lista.pop() # en este caso eliminamos el último elemento de la lista.

# Metodo remove()

# Para remover un elemento en concreto se utiliza el elemento remove.
# lista.remove('Hola') # este elimina un elemento por su valor.

# Metodo reverse()

# lista.reverse() # para ordenar al reves los elementos de la lista. 

# Metodo sort()

# lista.sort # no podemos utilizar el metodo sort si la lista tiene tanto string como integers. 
# para poder utilizar el metodo de sort, las listas siempre tienen que tener el mismo tipo de dato. 

# TUPLAS

# Las tuplas a diferencia de las listas, no se pueden modificar, para cambiarlas se tiene que hacer una copia de estas.
tupla = ('hola', 'mundo', 'somos', 'tupla')
# print(tupla.index('mundo')) # nos devuelve la posición del elemento especificado en la tupla
# print(tupla[0]) # accedemos a la posición de un elemento
# Para modificar una tupla tenemos que transformar la tupla en lista.
listaDeTupla = list(tupla)
listaDeTupla.append('chanchito') # no modificamos la tupla en si, si no que creamos una lista para poder modificar los elementos contenidos.
# print(listaDeTupla)
rango = range(6)
# print(rango)

# DICCIONARIOS

# Para crear un diccionario siempre utilizamos las llaves.
diccionario = {
    "nombre": "Chanchito feliz",
    "raza": "Persa",
    "edad": 5
} 
# print(diccionario)
# Para acceder a un valor del diccionario utilizamos []
# print(diccionario['nombre']) # tenemos que pasar como string el valor de la propiedad del diccionario, en este caso al nombre.
# print(diccionario['raza'])
# Tambien se puede utilizar el metodo get.
# print(diccionario.get('nombre')) 
# diccionario['nombre'] = "Fluffy" # en este caso modificamos el nombre y elimina el ya asignado antes.
# print(len(diccionario))
diccionario['ronronea'] = 'Si' # para agregar una propiedad nueva. 
# print(diccionario)
#copiaGatito = diccionario.copy()
# Otra forma de copiarlo sería: 
copiaGatito = dict(diccionario)
# En el caso de querer eliminar una propiedad o valor de un diccionario se llama el método de pop
# diccionario.pop('ronronea') # especificamos la propiedad
# Otra forma de eliminar el ultimo valor: 
# diccionario.popitem()
# Otra forma de eliminar un valor en concreto sería llamando la funcion del
# del diccionario['ronronea']
# Para eliminar todos los valores que contiene el diccionario llamamos el metodo clear
# diccionario.clear()
print(diccionario, copiaGatito)

