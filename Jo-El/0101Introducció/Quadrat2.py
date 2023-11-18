casos = int(input())
for i in range(casos):
    dimensions = input().split()
    files = int(dimensions[0])
    columnes = int(dimensions[1])
    if files < columnes:
        dimMin = files
    else:
        dimMin = columnes
    quadrats = 0
    for j in range(1, dimMin + 1):
        quadrats += (files - j + 1) * (columnes - j + 1)
    print(quadrats)
