# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos superiores a 1000€ mensuales
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales por pantalla si el usuario debe tributar o no.
edad = int(input("Introduce tu edad: "))
ingresos = float(input("Introduce tus ingresos mensuales: "))
if edad > 16 and ingresos >= 1000:
    print("Tienes que cotizar")
else:
    print("No tienes que cotizar.")