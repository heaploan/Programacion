# Conversor d'alçada del sistema britànic.
# Solicitar al usuario el número de polzades.
polzades = int(input("Introdueix el nombre de polzades: "))
# Solicitar al usuario el número de peus.
pies = int(input("Introdueix el nombre de peus: "))
# Convertir los peus a polzades y sumarlas a las polzades originales 
polzada = pies * 12 + polzades
# Convertir las polzades a milímetros.
alzadamm = polzada * 25.4
# Convertir milímetros a metros y centímetros.
metres = int(alzadamm // 1000)
centimetres = int(alzadamm % 1000) // 10
# Mostrar el resultado en metros y centímetros.
print(f"{metres}m {centimetres}cm")