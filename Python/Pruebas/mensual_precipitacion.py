import requests
import json
import matplotlib.pyplot as plt

mounths = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']

def es_bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
    else:
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]

year1 = 2000
m_days1 = es_bisiesto(year1)
api_url1 = f"https://archive-api.open-meteo.com/v1/archive?latitude=41.306&longitude=2.001&start_date={year1}-01-01&end_date={year1}-12-31&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Europe%2FBerlin"
response1 = requests.get(api_url1)
dades1 = json.loads(response1.text)
day = 0
preclist = []
for i in range(12):
    precsum1 = dades1["daily"]["precipitation_sum"][day]
    for j in range(m_days1[i]):
        precsum1 += dades1["daily"]["precipitation_sum"][day]
        day += 1
    preclist.append(precsum1)

        

year2 = 2020
m_days2 = es_bisiesto(year2)
api_url2 = f"https://archive-api.open-meteo.com/v1/archive?latitude=41.306&longitude=2.001&start_date={year2}-01-01&end_date={year2}-12-31&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Europe%2FBerlin"
response2 = requests.get(api_url2)
dades2 = json.loads(response2.text)
day = 0
preclist2 = []
for i in range(12):
    precsum2 = dades2["daily"]["precipitation_sum"][day]
    for j in range(m_days2[i]):
        precsum2 += dades2["daily"]["precipitation_sum"][day]
        day += 1
    preclist2.append(precsum2)

fig, ax = plt.subplots()
ax.bar(range(12), preclist, label=f'Precipitación {year1}', color='blue', width=0.45)
bar_positions = []
for i in range(12):
    position = i + 0.45
    bar_positions.append(position)
ax.bar(bar_positions, preclist2, label=f'Precipitación {year2}', color='green', width=0.45)

label_positions = []
for i in range(12):
    position = i + 0.45 / 2
    label_positions.append(position)
ax.set_xticks(label_positions)
ax.set_xticklabels(mounths)
plt.xlabel('Meses')
plt.ylabel('Precipitación')
plt.title(f'Comparacion de precipitacion mensual de {year1} y {year2}')
plt.legend()
plt.xticks(rotation=45, ha='right')
plt.show()