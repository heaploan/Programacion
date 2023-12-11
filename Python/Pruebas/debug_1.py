def funcio_suma( argument_entrada_1, argument_entrada_2):
    argument_sortida =  argument_entrada_1 + argument_entrada_2
    if argument_sortida == None:
        print("No he fet cap suma" )
    else:
        print("He fet una suma")
    return argument_sortida

def funcio_divisio( argument_entrada_1, argument_entrada_2):
    if argument_entrada_1.isnumeric() and argument_entrada_2.isnumeric():
        argument_sortida = argument_entrada_1 / argument_entrada_2
    else:
        argument_sortida = "Necessito números per dividir."
    return argument_sortida

print("Aquest programa demana 2 números i mostra la suma i la divisió.")
print("Pero ho fa emprant funcions.")
numero_1 = input("Introdueix el primer número : ")
numero_2 = input("Introdueix el segon número  : ")
resultat_suma = funcio_suma(numero_1, numero_2)
print(resultat_suma)
resultat_divisio = funcio_divisio(numero_1, numero_2)
print(resultat_divisio)
