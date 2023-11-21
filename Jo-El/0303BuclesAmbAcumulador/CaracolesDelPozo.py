entry = int(input())
for i in range(entry):
    data = input().split()
    profundidad = int(data[0])
    subida = int(data[1])
    bajada = int(data[2])
    metrosSubidos = 0
    dias = 0
    if profundidad > 0:
        if subida <= bajada:
            print("NO")
        else: 
            while metrosSubidos < profundidad:
                dias += 1
                metrosSubidos += subida
                if metrosSubidos < profundidad:
                    metrosSubidos -= bajada
            if metrosSubidos < 0:
                print("NO")
            else:
                print(dias)