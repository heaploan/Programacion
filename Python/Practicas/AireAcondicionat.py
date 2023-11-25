# Solicitar al usuario el número de casos de prueba
casos = int(input("Introduce el número de casos de prueba: "))
# Iterar a través de cada caso de prueba
for i in range(casos):
    # Obtener el número de grados de las varillas del aire condicionado
    numeroGrados = int(input())
    # Verificar si el aire está apagado (varillas a 0º o 180º)
    if numeroGrados % 360 == 0 or numeroGrados % 360 == 180:
        # Si está apagado, imprimir "OK"
        print("OK")
    else:
        # Si está encendido, imprimir "BRONCA"
        print("BRONCA")
