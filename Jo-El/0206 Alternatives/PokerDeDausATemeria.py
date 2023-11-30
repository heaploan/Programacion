num = input().split()
maximo = 0  
for i in num:
    cont = 0
    for n in num:
        if i == n:
            cont += 1
    if cont > maximo:
        maximo = cont

if maximo == 1:
    print("RES")
elif maximo == 2:
    print("PARELLA")
elif maximo == 3:
    print("TRIO")
elif maximo == 4:
    print("POKER")