frase=input("Introduce una frase: ")
con=""
for i in frase:
    if i.lower() not in "aeiou":    
        con+=i
print(con)