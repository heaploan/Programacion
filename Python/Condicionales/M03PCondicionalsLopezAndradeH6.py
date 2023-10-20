#he puesto int input ya que estamos colocando numeros enteros
horas=int(input("pon las horas de la Uf: "))
faltasJustificadas=int(input("pon las faltas justificadas: "))
noJustificadas=int(input("pon las faltas no justificadas: "))
#hemos llamado la variable horas para que se multiplicara por el porcentaje de las faltas
#no justificadas que sería un 10%, por eso el horas*0.1
if noJustificadas>=horas*0.1:
    print("No tienes derecho a evalucacion")
#aquí hemos sumado las faltas justificadas + las no justificadas para luego sacar el 20%
elif faltasJustificadas+noJustificadas>=horas*0.2:
    print("No tienes derecho a evaluacion")
else:
    print("Si tienes derecho a evaluacion")
