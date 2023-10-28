buida=[]
print(buida)
nums=[1,2,8,0,4,3]
print(nums)
lista=["Pedro",5.3,6,True]
print(lista)
pares=[2,4,6]
print(pares)
len(pares)
print(len(pares))
#agrega el valor al final
buida.append(5)
print(buida)
#agrega los valores a la lista
buida.extend([3,4,8])
print(buida)
buida.insert(0,8)
print(buida)
#pone la lista de mayor a menor
buida.sort(reverse=True)
print(buida)
#muestra la ultima, al poner negativos se entiende que se quiere mostrar el ultimo
print(nums[-1])
#imprime desde que empieza hasta que acaba.
print(nums[1:4])
#si el 3 esta en la lista nums, mostrara el mensaje
if 3 in nums:
    print("Esta en la lista")
#si el 5 no esta en la lista nums, mostrara el mensaje.
if 5 not in nums:
    print("No esta en la lista")
nombre=input()
for letra in nombre:
    #pone el nombre y luego repite las letras dos veces
    print(letra*2)
#hace las letras minusculas
nombre.lower()
#hace las letras mayusculas
nombre.upper()