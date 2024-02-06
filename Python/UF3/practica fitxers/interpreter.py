def checkParametros(command, n):
    if len(command) == n:
        return True
    else:
        print(f"ERROR: Número de argumentos incorrecto.")

def checkArguments(args, min):
    if len(args) < min:
        print("ERROR: Número de argumentos incorrecto.")
        return False
    return True