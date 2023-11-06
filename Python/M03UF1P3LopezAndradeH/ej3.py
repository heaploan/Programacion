import random

lista = []

for i in range(30):
    lista.append(random.randint(0,29))
print(lista)

repeticiones = 0
for repetido in range(30):
    if repetido == lista[repetido]:
        repeticiones += 1
        print(f"El numero {repetido} esta en la lista en la posiscion {lista[repetido]}")

if repeticiones == 0:
    print("Cap numero ha coincidit amb la seva posicio.")