nombre=input("Ingrese su nombre completo: ")
o=nombre.split(" ")
print(nombre.lower())
print(nombre.upper())
for i in o:
    print(i.capitalize(), end=" ")