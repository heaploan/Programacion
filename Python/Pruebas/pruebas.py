# En caso de ser complejo, no hace nada a la variable, no la modifica
# A esto se le llama paso por valor
"""def cambiarnum(a):
    a = a + 1
a = 2
cambiarnum(a)
print(a)"""

# Al ser simple si cambia la variable, en este caso si agrega el 8
# A esto se le llama paso por referencia
"""def cambiar(nums):
    nums.append(8)
lista = [1,2,3]
cambiar(lista)
print(lista)"""

