import sys
from hotel import *
from interpreter import *
# ejemplo: py ./main.py afegir habitacio 100 1 45.90

if len(sys.argv) < 3:
    print("ERROR: Número de argumentos incorrecto.")
    sys.exit(1)
if sys.argv[1].lower() == 'afegir' and sys.argv[2].lower() == 'habitacio':
        addRoom(sys.argv)  # Pasamos sys.argv como argumento a addRoomToFile
else:
    print("ERROR: Comando incorrecto")
