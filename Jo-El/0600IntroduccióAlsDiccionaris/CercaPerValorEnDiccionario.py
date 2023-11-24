casos = int(input())
for i in range(casos):
    numeroLineas = int(input())
    diccionario= {}
    for i in range(numeroLineas - 1):
        entrada = input().split("-")
        pais = entrada[0]
        capital = entrada[1]
        diccionario[pais] = capital 
    capital_buscada = input()
    # Imprimir el diccionario en formato estándar
    print("{", end="")
    for key, value in diccionario.items():
        print(f"{key}={value}", end=", ")
    print("\b\b}")
    for key, value in diccionario.items():
        if value == capital_buscada:
            print(key)