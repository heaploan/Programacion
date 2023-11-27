#la f la he colocado para poder llamar las variables denro de las comillas y colocandolas dentro de llaves
a = int(input('Introdueix un número: '))
b = int(input('Introdueix un altre número: '))
print(f'El número guardat a la variable a és: {a}')
print(f'El número guardat a la variable b és: {b} ')
print('El resultat de la suma: ',a+b)
print('El resultat de la resta: ',a-b)
print('El resultat de la multiplicació: ',a*b)
print('El resultat de la divisió: ',a/b)
print(f'Valor de a: {a}')
print(f'Valor de b: {b}')
#Pero en python se puede hacer a,b = b,a, solo que con la variable c se puede aprender para otros lenguajes
c=a
a=b
b=c
print('Intercambi fet!')
print(f'Valor de a: {a}')
print(f'Valor de b: {b}')
print('a+b/2*(a+b)')
print(f'{a}+{b}/2*({a}+{b})')
print(f'{a}+',b/2,'*',(a+b))
print(f'{a}+',b/2*(a+b))
print(a+b/2*(a+b))
