# Importamos las bibliotecas necesarias
import requests  # para realizar solicitudes HTTP
import json      # para manejar datos en formato JSON
import sys # Para poder correrlo desde terminal
# Pedimos al usuario que ingrese la fecha en formato año-mes
ym = sys.argv[1]
# Definimos la URL de la API con la latitud, longitud y la fecha proporcionada
api_url = f"https://archive-api.open-meteo.com/v1/archive?latitude=41.306&longitude=2.001&start_date={ym}-01&end_date={ym}-31&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Europe%2FBerlin"
# Realizamos una solicitud GET a la API y almacenamos la respuesta en formato JSON
response = requests.get(api_url)
dades = json.loads(response.text)
# Extraemos la temperatura máxima del primer día del mes
Tmax = dades["daily"]["temperature_2m_max"][0]
# Obtenemos la longitud de la lista de temperaturas máximas
ltmax = len(dades["daily"]["temperature_2m_max"])
# Bucle para encontrar la temperatura máxima del mes
for i in range(ltmax):
    if Tmax < dades["daily"]["temperature_2m_max"][i]:
        Tmax = dades["daily"]["temperature_2m_max"][i]
# Extraemos la temperatura mínima del primer día del mes
Tmin = dades["daily"]["temperature_2m_min"][0]
# Obtenemos la longitud de la lista de temperaturas mínimas
ltmin = len(dades["daily"]["temperature_2m_min"])
# Bucle para encontrar la temperatura mínima del mes
for i in range(ltmin):
    if Tmin > dades["daily"]["temperature_2m_min"][i]:
        Tmin = dades["daily"]["temperature_2m_min"][i]
# Inicializamos la variable dpluja para contar los días de lluvia
dpluja = 0
# Obtenemos la longitud de la lista de precipitaciones
lprec = len(dades["daily"]["precipitation_sum"])
# Bucle para contar los días en los que ha llovido (precipitación > 0)
for i in range(lprec):
    if dades["daily"]["precipitation_sum"][i] > 0:
        dpluja = dpluja + 1
# Imprimimos los resultados: temperatura máxima, temperatura mínima y días de lluvia
print("Tmax=", Tmax, "ºC", "Tmin=", Tmin, "ºC", "Días de lluvia:", dpluja)
