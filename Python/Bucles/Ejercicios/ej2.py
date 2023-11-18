#se crea la variable para guardar la información que se le pedirá al usuario con int ya que pide numero entero.
num1=0
while num1 >= 1:
    num1=int(input("Ingrese un número mayor al 0: "))
#se crea la segunda variable para el contenido del for y se pone la primera variable multiplicada por dos
#en el print se llama la segunda variable para tener el resultado del for y se deja tal cual ya que al empezar de 0
#mostrará el numero multiplicado por dos pero menos uno que sería un 2*2=8 pero muestra 7.
    if num1<=0:
        print("Valor invalido, ingrese un numero mayor al 0")
for num2 in range (num1,num1*2):
    print(num2)