import requests
import json
import matplotlib.pyplot as plt

api_url1 = "https://archive-api.open-meteo.com/v1/archive?latitude=41.306&longitude=2.001&start_date=2010-01-01&end_date=2010-12-31&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Europe%2FBerlin"

response1 = requests.get(api_url1)

dades1 = json.loads(response1.text)

tempMax1 = dades1["daily"]["temperature_2m_max"]
tempMin1 = dades1["daily"]["temperature_2m_min"]
pluja1 = dades1["daily"]["precipitation_sum"]

api_url2 = "https://archive-api.open-meteo.com/v1/archive?latitude=41.306&longitude=2.001&start_date=2020-01-01&end_date=2020-12-31&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Europe%2FBerlin"

response2 = requests.get(api_url2)

dades2 = json.loads(response2.text)

tempMax2 = dades2["daily"]["temperature_2m_max"]
tempMin2 = dades2["daily"]["temperature_2m_min"]


mounths = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']

fig, ax = plt.subplots()

ax.plot(tempMax1, label='Temp. Máxima 2010', color='red')
ax.plot(tempMax2, label='Temp. Máxima 2020', color='orange')

ax.plot(tempMin1, label='Temp. Mínima 2010', color='green')
ax.plot(tempMin2, label='Temp. Mínima 2020', color='purple')

ax.set_xticks([0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334])
ax.set_xticklabels(mounths)
plt.xlabel('Fecha')
plt.ylabel('Valor')
plt.title('Datos meteorológicos de diciembre de 2022')
plt.legend()

plt.xticks(rotation=45, ha='right')

plt.show()
