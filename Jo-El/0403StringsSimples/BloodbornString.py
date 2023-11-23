casos = int(input())
for i in range(casos):
    string = input()
    seguidas = False
    for j in range(len(string) - 1):
        if string[j] == string[j + 1]:
            seguidas = True
    if seguidas:
        print("SI")
    else:
        print("NO")