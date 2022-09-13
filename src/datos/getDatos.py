from lecturaCiudades import *
import requests, json

class Request:
    
    def __init__(self):
        self.ciudades = LecturaCiudades()
        self.climaCiudad = {}

    def getClimaCiudad(self): 
        return self.climaCiudad

    def coonectarApi(self, claveCiudad):
        archivoKey = open('key.txt')
        apiKey = archivoKey.read()
        url = "http://api.openweathermap.org/data/2.5/weather?"
        latitudLongitud = self.ciudades.getCoordenadas(claveCiudad)
        
        urlCompleta = f'{url}lat={latitudLongitud[0]}&lon={latitudLongitud[1]}&appid={apiKey}'
        respuesta = requests.get(urlCompleta)
        self.climaCiudad = json.loads(respuesta.text)
    
    def imprimeDatos(self):
        detallesClima = self.climaCiudad['weather']
        print("El clima es el siguiente: \n ")
        print("El estado del clima es: " + detallesClima[-1]["main"])
        print("Descricpion del clima: " + detallesClima[-1]["description"])
        print("La temperatura actual es: " + str(self.climaCiudad["main"]["temp"]) + " °K")
        print("La temperatura mínima es: " + str(self.climaCiudad["main"]["temp_min"]) + " °K")
        print("La temperatura máxima es: " + str(self.climaCiudad["main"]["temp_max"]) + " °K")
        print("La velocidad del viento es: " + str(self.climaCiudad["wind"]["speed"]) + " m/s")
        print("La nubosidad es del: " + str(self.climaCiudad["clouds"]["all"]) + "%")
 
""" def main():
    a = Request()
    a.coonectarApi('GDL')
    dic = a.getClimaCiudad()
    print(dic['id'])
    print(type(dic['id']))
    a.imprimeDatos()
main()     """