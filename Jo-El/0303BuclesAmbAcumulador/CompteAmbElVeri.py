# Se solicita al usuario ingresar el número de casos a evaluar
casos = int(input())
# Se utiliza un bucle for para iterar a través de cada caso
for i in range(casos):
    # Se solicita al usuario ingresar la entrada para cada caso y se almacena en la variable 'entry'
    entry = input()   
    # Se divide la entrada en una lista llamada 'data'
    data = entry.split()  
    # Se extraen los valores de hp, rammusAttack y twitchVenom de la lista 'data' y se convierten a enteros
    hp = int(data[0])
    rammusAttack = int(data[1])
    twitchVenom = int(data[2])  
    # Se verifica que los valores sean mayores a 0 antes de iniciar el juego
    if hp > 0 and rammusAttack > 0 and twitchVenom > 0:
        rondas_rammus = 0
        rondas_twitch = 0       
        # Se utiliza un bucle while para simular el juego hasta que el HP sea menor o igual a 0
        while hp > 0:
            # Se reduce el HP por el ataque de Rammus
            hp -= rammusAttack           
            # Se incrementa el número de rondas de Rammus
            rondas_rammus += 1          
            # Se verifica si el HP es menor o igual a 0 después del ataque de Rammus
            if hp <= 0:
                print(f"RAMMUS {rondas_rammus}") 
            else:
                # Si no, se reduce el HP por el ataque de Twitch
                hp -= twitchVenom               
                # Se incrementa el número de rondas de Twitch
                rondas_twitch += 1  
                # Se verifica si el HP es menor o igual a 0 después del ataque de Twitch
                if hp <= 0:
                    print(f"TWITCH {rondas_twitch}")
