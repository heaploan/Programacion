ini =int(input())
hp = int(input())
veces = 0
total = 0
while hp > 0: 
    total += ini
    veces += 1
    hp -= total
print(veces)
