casos = int(input())
for i in range(casos):
    k = int(input())
    numbers = input().split()
    m = int(input())
    encontrado = False
    for j in range(k):
        talla = int(numbers[j])
        if talla == m or talla == m - 1 or talla == m + 1:
            encontrado = True
        j += 1
    if encontrado:
        print("SI")
    else:
        print("NO")