num=int(input("Escribe un numero mayor o igual a 10: "))
'''Para poner and se tiene que volver a poner la variable, en este caso, volver a poner num (IMPORTANTE)'''
'''Aunque python permite poner esto 10<num<20'''
if num>10 and num<20:
    print("Lo has hecho correctamente!")
elif num<=10:
    print("Has puesto un número menor")
else: 
    print("Has puesto un número mayor")
'''Si ponemos and, las dos condiciones se cumplen el resultado es TRUE'''
'''El AND solo devuelve si ambas son TRUE y el OR con solo se cumpla una devuelve'''
'''elif es en caso de que se pueda cumplir otra condición y siempre va enganchado al if, nunca después de un else'''
