import requests
import json

# Asignamos las url del ejemplo a variables
restUrl="https://www.el-tiempo.net/api/json/v1/provincias/08/municipios/08089/weather"
htmlUrl="https://www.eltiempo.es/gava.html"
# Hacemos petición al servidor en formato html.
respostaHtml=requests.get(htmlUrl)
# Mostramos por pantalla la respuesta recibida
print("------- RESPOSTA HTML ---------")
print(respostaHtml.text)
print()
# Hacemos el mismo proceso con el servicio rest.
respostaREST=requests.get(restUrl)
print("------- RESPOSTA REST ---------")
print(respostaREST.text)
print()

# json 

dades=json.loads(respostaREST.text)
print("------- JSON FORMATEJAT ---------")
print(json.dumps(dades,indent=3))
print()
print("Data d'elaboració de l'informe ",dades["elaborado"])
print("Municipi ",dades["nombre"]," a la província de ",dades["provincia"])
print("Predicció per data ",dades["prediccion"]["dia"][0]["@attributes"]["fecha"])
print("Predicció: temperatura màxima: ",dades["prediccion"]["dia"][0]["temperatura"]["maxima"])
print("Predicció: temperatura mínima: ",dades["prediccion"]["dia"][0]["temperatura"]["minima"])