# CONTROL DE FLUJO

# Nos ayuda a tomar decisiones

#if 2 < 5: 
#    print('2 es menor que 5')
# a == b igual a 'b'
# a <  b menor a 'b'
# a > b mayor a 'b'
# a != b diferente a 'b'
# a <= b menor o igual a 'b'
# a >= b mayor o igual a 'b'
    
#if 2 == 2:
    #print('2 es igual a 2')

#if 2 == 3:
 #   print('2 es igual a 3')

#if 2 > 5:
 #   print('2 es mayor a 5')

#if 5 > 2:
 #   print('5 es mayor a 2')

#if 2 != 2:
 #   print('2 es distinto a 2')

#if 3 != 2:
 #   print('3 es distinto a 2')

#if 3 >= 2:
 #   print('3 es mayor o igual a 2')

#if 3 <= 3:
 #   print('3 es menor o igual a 3')

# IF, ELIF, ELSE.

#if 2 > 5:
#    print('2 es menor a 5 en if')
#elif 2 > 5:
 #   print('2 es menor a 5 en elif')
#elif 2 < 5:
  #  print('2 es menor a 5 en segundo elif')    
#else:
 #   print('Yo me imprimo solo si todo lo anterior evaula en falso')

'''Si en if la opción es falsa, pasa al elif, si también es falsa, pasa al segundo elif
y si todo lo anterior es falso, pasa al else, si alguna de las opciones es verdadero, se queda en esa
en este caso el segundo elif es correcto, por tanto imprime lo del segundo elif.'''

if 2 < 5: print('if de una línea')

print('cuando devuelve true') if 5 > 2 else print('cuando devuelve false') # también conocido como operador ternario

if 2 < 5 and 3 > 2:
    print('ambas devuelven true')

if 2 < 5 and 3 < 2:
    print('hay una falsa, esto no se mostrará')

'''si la evaluación de la izquierda se devuelve True, en ese caso todo se evalua en True y por ende 
vamos a poder ejecutar la instrucción dentro del if, igual caso si la evaluación de la derecha es true,
sucede lo mismo'''

if 1 < 0 or 1 > 0: # Si una condición evalua en true se ejecuta la instrucción
    print('una de las dos condiciones devolvió true')

if 1 < 0 or 1 < 0: # si ambas condiciones son falsas, entonces no se ejecuta
    print('si ambas condicoines evaluan en false no se ejecuta esto.')