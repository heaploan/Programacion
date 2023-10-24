#se pone el numero de casos a calcular
casos=int(input())
#se crea el rango con la variable casos dentro de este.
for i in range(casos):
    #creamos las variables pares e impares=0 para que se les asigne mas tarde un valor.
    pares=0
    impares=0
    #variable num para crear el rango de los numeros a calcular
    num=int(input())
    #metemos el num dentro del rango para hacer las operaciones 
    for z in range(num+1):
        #usamos la variable z que creamos en for ya que toma el valor de num
        if z%2==0:
            pares+=z
        else:
            impares+=z
    #el print lo ponemos a la altura de for para que muestre solo el resultado de las operaciones.        
    print(f"PARELLS: {pares} SENARS: {impares}")