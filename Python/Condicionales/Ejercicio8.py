hora=int(input("Introduce una hora (entre 0-23): "))
minuto=int(input("Introduce un minuto (entre 0-59): "))
segundo=int(input("Introduce un segundo (entre 0-59): "))
segundosTotales=hora*60*60+minuto*60+segundo
print(f"La hora introducida es {hora}:{minuto}:{segundo} que corresponde a {segundosTotales} segundos")
