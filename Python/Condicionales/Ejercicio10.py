dinero=float(input("Indica el dinero que tienes: "))
precio=float(input("Indica el precio de la prenda: "))
precioTotal=precio-precio*0.25
print(f"El precio con el descuento aplicado es de: {precioTotal}")
print(f"El dinero restante sería: ",dinero-precioTotal)