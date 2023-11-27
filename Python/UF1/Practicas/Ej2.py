# Solicitar al usuario el número de asistentes a la fiesta
asistentes = int(input("Introduce el número de asistentes: "))
# Verificar que el número de asistentes esté en el rango permitido
if 0 <= asistentes <= 999:
    # Coca Cola
    latasPorPack = 6
    packs = 1
    # Calcular la cantidad de packs de Coca Cola necesarios
    cantidadPacksCocaCola = (asistentes + latasPorPack - 1) // latasPorPack
    # Pa de motllo
    rodajasPack = 20
    rodajasEntrepan = 2
    # Calcular el número de sandwiches consumidos y rodajas de pan consumidas
    sandwichesConsumidos = asistentes * 2
    rodajasConsumidas = sandwichesConsumidos * rodajasEntrepan
    # Calcular la cantidad de paquetes de pan (paBimbo) necesarios
    paBimbo = (rodajasConsumidas + rodajasPack - 1) // rodajasPack
    # Nutella
    entrepansPot = 15
    # Calcular la cantidad de pots de Nutella necesarios
    cantidadPotsNutella = (asistentes * rodajasEntrepan + entrepansPot - 1) // entrepansPot
    # Calcular los items restantes
    latasSobrantes = cantidadPacksCocaCola * latasPorPack - asistentes
    rodajasSobrantes = (paBimbo * rodajasPack) - rodajasConsumidas
    # Imprimir la lista de compras
    print(f"Lista de la compra:\n{cantidadPacksCocaCola} packs de coca cola\n{paBimbo} paquets de pa de motllo\n{cantidadPotsNutella} pots de nutella.")
    # Imprimir los items restantes
    print(f"\nSobren:\n{latasSobrantes} llaunes de coca cola\n{rodajasSobrantes} llesques de pa")
else:
    # Imprimir un mensaje de error si el número de asistentes no está en el rango permitido
    print("El nombre d'assistents ha de ser un nombre enter entre 0 i 999.")
