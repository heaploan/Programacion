casos = int(input())
for i in range(casos):
    numeroLineas = int(input())
    diccionario = {}
    for j in range(numeroLineas - 1):
        entrada = input().split("-")
        pais = entrada[0]
        capital = entrada[1]
        diccionario[pais] = capital
    capitalBuscada = input()
    print("{", end="")
    first_item = True
    for key, value in diccionario.items():
        if not first_item:
            print(", ", end="")
        print(f"{key}={value}", end="")
        first_item = False
    print("}")
    for key, value in diccionario.items():
        if value == capitalBuscada:
            print(key)