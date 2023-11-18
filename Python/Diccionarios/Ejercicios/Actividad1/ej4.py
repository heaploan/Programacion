# Crear un diccionario vacío para almacenar los nombres y las notas de los alumnos.
clase = {}
# Solicitar al usuario la cantidad de alumnos a registrar.
cantidadAlumnos = int(input("Introduce la cantidad de alumnos que registraras: "))
# Iterar sobre el rango de la cantidad de alumnos.
for i in range(cantidadAlumnos):
    # Solicitar al usuario el nombre de un alumno.
    alumno = input("Introduce el nombre de un alumno: ")

    # Verificar si el nombre del alumno ya ha sido registrado.
    while alumno in clase:
        print(f"El nombre {alumno} ya ha sido registrado. Introduce otro nombre.")
        alumno = input("Introduce el nombre de un alumno: ")    
    # Inicializar una lista vacía para almacenar las notas del alumno.
    notas = []
    # Solicitar al usuario ingresar las notas del alumno.
    nota = float(input("Introduce las notas: "))
    
    # Continuar solicitando notas mientras la nota sea mayor o igual a cero.
    while nota >= 0:
        # Verificar que la nota esté en el rango válido (0 a 10) y agregarla a la lista.
        if nota <= 10:
            notas.append(nota)
        else:
            print("Error: pon notas del 0 al 10")
        # Almacenar las notas en el diccionario con el nombre del alumno como clave.
        clase[alumno] = notas
        # Solicitar al usuario ingresar otra nota.
        nota = float(input("Introduce las notas: "))
# Iterar sobre el diccionario para calcular y mostrar el promedio de notas para cada alumno.
for alumno in clase:
    notas = clase[alumno]
    if notas:
        media = sum(notas) / len(notas)
        print(f"{alumno} {media:.2f}")