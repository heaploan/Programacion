#creamos la variable meses con lista e introducimos todos los meses del año en texto.
meses=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
#introducimos los dias que tiene cada mes, simplificando que febrero tiene 28 días.
dias_mes=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#creamos la variable num_mes para pedir el numero del mes.
num_mes=int(input("Introduce el numero de mes del 1 al 12: "))
#si num mes es  igual o mayor o menor o igual a 12...
if 1 <= num_mes <= 12:
        #creamos esta variable introduciendo la lista de meses -1 para ajustarnos a la lista.
        nombre_mes = meses[num_mes - 1]  
        #creamos variable dias y le asignamos la lista num_mes -1 para ajustarnos a esta.
        dias = dias_mes[num_mes - 1]
        #imprimimos el nombre del mes y los días que tiene.
        print(f"{nombre_mes} tiene {dias} días.")
else:
    print("Numero de mes no valido, debe estar entre 1 y 12.")