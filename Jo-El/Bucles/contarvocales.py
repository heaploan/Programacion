casos = int(input())
for i in range(casos):
    frase = input()
    frase = frase.lower()
    conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letra in frase:
        if letra in 'aeiou':
            conteo_vocales[letra] += 1
    resultado = f'A: {conteo_vocales["a"]} E: {conteo_vocales["e"]} I: {conteo_vocales["i"]} O: {conteo_vocales["o"]} U: {conteo_vocales["u"]}'
    print(resultado)