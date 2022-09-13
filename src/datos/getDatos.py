from lecturaCiudades import *
from Cache import *
import requests, json
import time

class Request:
    
    def __init__(self):
        self.ciudades = LecturaCiudades()
        self.climaCiudad = {}

    def coonectarApi(self, claveCiudad):
        archivoKey = open('key.txt')
        apiKey = archivoKey.read()
        url = "http://api.openweathermap.org/data/2.5/weather?"
        latitudLongitud = self.ciudades.getCoordenadas(claveCiudad)
        
        urlCompleta = f'{url}lat={latitudLongitud[0]}&lon={latitudLongitud[1]}&appid={apiKey}'
        respuesta = requests.get(urlCompleta)
        self.climaCiudad = json.loads(respuesta.text)
    
    def generaDatos(self):
        datos = []
        detallesClima = self.climaCiudad['weather']
        datos.append(detallesClima[-1]["main"])
        datos.append(detallesClima[-1]["description"])
        datos.append(str(self.climaCiudad["main"]["temp"]) + " °K")
        datos.append(str(self.climaCiudad["main"]["temp_min"]) + " °K")
        datos.append(str(self.climaCiudad["main"]["temp_max"]) + " °K")
        datos.append(str(self.climaCiudad["wind"]["speed"]) + " m/s")
        datos.append(str(self.climaCiudad["clouds"]["all"]) + "%")
        hora = time.time()
        datos.append(hora)
        return datos


def main():
    a = Request()
    cache = {}
    a.coonectarApi('MEX')
    datos = a.generaDatos()
    Cache.agregaDatos(cache, datos, 'MEX')
    Cache.muestraDatos(cache, 'MEX')
main()   

