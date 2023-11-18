casos = int(input())
for i in range(casos):
    entry = input()
    data = entry.split()
    hp = int(data[0])
    rammusAttack = int(data[1])
    twitchVenom = int(data[2])
    if hp > 0 and rammusAttack > 0 and twitchVenom > 0:
        rondas_rammus = 0
        rondas_twitch = 0
        while hp > 0:
            hp -= rammusAttack
            rondas_rammus += 1
            if hp <= 0:
                print(f"RAMMUS {rondas_rammus}") 
            else:
                hp -= twitchVenom
                rondas_twitch += 1
                if hp <= 0:
                        print(f"TWITCH {rondas_twitch}")