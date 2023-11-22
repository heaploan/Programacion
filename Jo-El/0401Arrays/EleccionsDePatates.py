casos = int(input())
for i in range(casos):
    nums = input().split()
    opcions = int(nums[0])
    opcionGanadora = 0
    indiceMax = 0
    for j in range(1, opcions + 1 ):
        actual = int(nums[j])
        if actual > indiceMax:
            opcionGanadora = j
            indiceMax = actual
    print(opcionGanadora)
    