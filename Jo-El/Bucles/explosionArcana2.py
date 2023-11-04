ini =int(input())
hp = int(input())
veces = 0
while hp > 0: 
    hp -= ini 
    ini += ini
    veces += 1
print(veces)
