clase = {}
cantidadAlumnos = int(input("Introduce la cantidad de alumnos que registraras: "))
for i in range(cantidadAlumnos):
    alumno = input("Introduce el nombre de un alumno: ")
    while alumno in clase: 
        print(f"El nombre {alumno} ya ha sido registrado. Introduce otro nombre.")
        alumno = input("Introduce el nombre de un alumno: ")    
    notas = []
    nota = float(input("Introduce las notas: "))
    while nota >= 0:
        if nota <=10:
            notas.append(nota)
        else:
            print("Error: pon notas del 0 al 10")
        clase[alumno] = notas
        nota = float(input("Introduce las notas: "))
for alumno in clase:
    notas = clase[alumno]
    if notas:
        media = sum(notas) / len(notas)
        print(f"{alumno} {media:.2f}")
