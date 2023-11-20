# Solicita al usuario que ingrese las horas, minutos y segundos
h = int(input())
m = int(input())
s = int(input())
# Incrementa los segundos en 1
s += 1
# Verifica si los segundos alcanzaron 60, en cuyo caso se reinician y se incrementan los minutos
if s == 60:
    s = 0
    m += 1
    # Verifica si los minutos alcanzaron 60, en cuyo caso se reinician y se incrementan las horas
    if m == 60:
        m = 0
        h += 1
        # Verifica si las horas alcanzaron 24, en cuyo caso se reinician
        if h == 24:
            h = 0
# Imprime la nueva hora en el formato "hora minutos segundos"
print(f"{h} {m} {s}")
  
