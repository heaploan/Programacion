numeros=[6, 1, 2, 3, 8, 1, 0, 3, 0, 0, 4, 5, 7]
#a
print(f"La llista numeros: {numeros}")
#b
print(f"La llista te: {len(numeros)} elements.")
#c
print(f"A la posicio 4 de la llista hi ha: {numeros[4]}")
#d
numeros.append(9)
#e
numeros.insert(1,4)
#f
print(f"La llista numeros: {numeros}")
#g
numeros.remove(6)
#h
print(f"La llista numeros: {numeros}")
#i
print(f"El darrer element de la llista es: {numeros[-1]}")
#j
suma=0
for i in numeros:
    suma+=i
print(f"La suma de los elementos de la lista es: {suma}")
#k
num=int(input("Introdueix un numero: "))
if num in numeros:
    print(f"El numero {num} esta a la llista.")
else:
    print(f"El numero {num} no esta a la llista")
#l
numeros.append(6)
#m
print(f"La llista numeros: {numeros}")
#o
num2=int(input("Introdueix un numero: "))
z=0
for i in range(len(numeros)):
    if num2==numeros[i] and z==1:
        z+=1
        print(f"La posicio de {num2} es: {i}")
#p
numeros.sort(reverse=True)
print(f"La llista numeros: {numeros}")
#q
numeros.sort()
print(f"La llista numeros: {numeros}")
