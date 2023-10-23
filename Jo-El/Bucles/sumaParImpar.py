casos=int(input())
pares=0
impares=0
for i in range(casos):
    num=int(input())
    if num%2==0:
        pares+=num
    else:
        impares+=num
    print(f"PARELLS: {pares} SENARS: {impares}")