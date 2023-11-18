casos = int(input())
for i in range(casos): 
    datos = input().split()
    pozo = int(datos[0])
    subida = int(datos[1])
    bajada = int(datos[2])
    metrosSubidos = 0
    dias = 0
    while metrosSubidos < pozo:
        metrosSubidos += subida
        dias += 1
        if metrosSubidos >= pozo:
            metrosSubidos -= bajada
    if metrosSubidos >= pozo:
        print(dias)
    else:
        print("NO")

