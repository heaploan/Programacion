# DEF

# Método es un procedimiento o función que está dentro de una clase.
# Procedimineto
# Función
# Método

# Reecibe un nombre y lo devuelve.
def hello(name="Default", age=51):
    # Solo dentro del tab existe
    print("Hello World!", name)
    if age > 50:
        print("You are young and funny!")
    else:
        print("You're a baby")
# Puede recibir varios parámetros, en este caso recibe 2.
# Recibe dos enteros y devuelve el resultado en numero entero. 
def suma(num1, num2):
    resultado = num1 + num2
    return resultado

# Recibe dos parámetros en enteros y divide estos entre si
# Confirma que el dividendo no sea menor a 0
def division(num1, num2):
    if num2 > 0:
        resultado = num1 / num2
        return resultado
    else:
        print("ERROR: el dividendo no puede ser menor a 0 o 0")
        
hello()
x = suma(8, 2)
print (x)
y = division