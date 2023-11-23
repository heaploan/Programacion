casos = int(input())
for i in range(casos):
    n = input().split(":")
    horas = int(n[0])
    minutos = int(n[1])
    totalMinutos = horas * 60 + minutos
    inicioRaid = 22 * 60 + 30
    finalDia = 24 * 60
    finalRaid = 0 * 60 + 30
    if (inicioRaid <= totalMinutos <= finalDia) or (0 <= totalMinutos <= finalRaid):
        print("RAID")
    else:
        if totalMinutos < inicioRaid:
            minutosRaid = inicioRaid - totalMinutos
        else:
            minutosRaid = finalDia - totalMinutos + inicioRaid
        print(minutosRaid)