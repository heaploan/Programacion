# Recibe dos parámetros y comprueba si són múltiples entre si o no.
# Devuelve True si lo son y False si no lo son.
def mult(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False
    
print(mult(2, 2))