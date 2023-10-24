casos=int(input())
for i in range(casos):
    pares=0
    impares=0
    num=int(input())
    for z in range(num+1):
        if z%2==0:
            pares+=z
        else:
            impares+=z
    print(f"PARELLS: {pares} SENARS: {impares}")