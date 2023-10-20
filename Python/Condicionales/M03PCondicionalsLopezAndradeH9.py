a=int(input("Inserta un número de sets ganados entre 0 y 8: "))
b=int(input("Inserta un número de sets ganados entre 0 y 8: "))
#este if pone el rango del 0 a 8 incluyendo ambos números.
if 0<=a<=8 and 0<=b<=8:
    #si a o b son mayores a 7 el resultado es invalido
    if a>7 or b>7:
        print("Resultado invalido")
    #si a es igual a 7 y b es menor a 5, el resultado es invalido
    elif a==7:
        if b<5:
            print("Resultado invalido")
        #en los demas casos gana A
        else:
            print("Gana A")
    #se repite lo mismo que con A
    elif b==7:
        if a<5:
            print("Resultado invalido")
        else:
            print("Gana B")
    #si a es igual a 6 y b=a entonces es empate
    elif a==6 and a==b:
        print("Empate a 6: Gana el primero en anotar.")
    #lo mismo pero con empate a 5
    elif a==5 and a==b:
        print("Empate a 5: Gana primero en llegar a 7.")
    #si a=6 y b es dos menos que a, gana a
    elif a==6 and b<=a-2:
        print("Gana A")
    #si b=6 y a es dos enos que b, gana b
    elif b==6 and a<=b-2:
        print("Gana B")
    #en cualquier otro caso, el partido aun no termina
    else:
        print("Sin terminar")
#En caso de ser un numero fuera del rango especificado, dará error.
else:
    print("Número inválido, repite de nuevo.")
