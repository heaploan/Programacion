# para abrir un diccionario se usan llaves
pokemon = {}
# para introducir un valor al diccionario.
pokemon ["Pikachu"] = 345
pokemon ["Charmander"] = 66
pokemon ["Boby"] = 266
print(pokemon)
nombre = input("De quien quieres saber que come? ")
# para buscar lo que se pide en el diccionario.
if nombre in pokemon:
    print(pokemon[nombre])
else:
    print("No tengo mascota con ese nombre.")

# Para recorrer un diccionario:
for poke in pokemon:
    # Solo muestra las claves
    print(poke)
    # Si queremos que se muestre el valor es esto
    print(poke, pokemon[poke])

#Este for es solo para mostrar solo los valores
for valor in pokemon.values():
    print(valor)
# Creamos diccionarios.
mascotas = {}
# Agregamos el nombre y creamos otro diccionario dentro del diccionario de mascotas.
mascotas["Boby"] = {"come": 266, "bebe": "agua", "duerme": 18}
mascotas["Pipo"] = {"come": 25, "bebe": "zumos", "duerme": 18}
mascotas["Lola"] = {"come": 123,"bebe": "agua", "duerme": 12}
print(mascotas)
# Necesitamos ponerlo entre corchetes para mostrar un dato en especifico.
print(mascotas["Pipo"]["duerme"])

