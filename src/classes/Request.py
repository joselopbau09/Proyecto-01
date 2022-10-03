
import requests, json
import time
from classes.LecturaCoordenadas import LecturaCoordenadas

class Request:
    """Clase para realizar la llamada a la API.
    
    Attributes:
        coordenadas (obj): Inicializa el objeto que maneja la \"Base de datos\".
        climaCiudad (dic): Almacena los datos que se consultan de la API.
    """
    
    def __init__(self):
        """ Constructor que inicializa los parametros.
                
        """
        self.coordenadas = LecturaCoordenadas()
        self.climaCiudad = {}

    def getClimaCiudad(self): 
        """Se obtiene el diccionario con la información de la ciudad.
        
        Returns:
            dict: Almacena la información consultada en el API.
            
        """
        return self.climaCiudad    

    def conectarApi(self, claveCiudad):
        """Realiza la llamada a la API y genera el json. Lee un archivo txt con la llave.

        Args:
            claveCiudad (str): identificador único para obtener las coordenadas del aeropuerto.

        """
        archivoKey = open('assets/key.txt')
        apiKey = archivoKey.read()
        archivoKey.close()
        url = "http://api.openweathermap.org/data/2.5/weather?"
        latitudLongitud = self.coordenadas.getCoordenadas(claveCiudad)
        
        urlCompleta = f'{url}lat={latitudLongitud[0]}&lon={latitudLongitud[1]}&units=metric&lang=sp&appid={apiKey}'
        respuesta = requests.get(urlCompleta)
        self.climaCiudad = json.loads(respuesta.text)
    
    def generaDatos(self):
        """Guarda los datos del clima en una lista.

        Return:
            list: lista que contiene los datos del clima y la hora en que se realizó la llamada.
            
        """
        datos = []
        detallesClima = self.climaCiudad['weather']
        datos.append(detallesClima[-1]["description"])
        datos.append(str(self.climaCiudad["main"]["temp"]) + " °C")
        datos.append(str(self.climaCiudad["main"]["temp_min"]) + " °C")
        datos.append(str(self.climaCiudad["main"]["temp_max"]) + " °C")
        datos.append(str(self.climaCiudad["wind"]["speed"]) + " m/s")
        datos.append(str(self.climaCiudad["clouds"]["all"]) + "%")
        hora = time.time()
        datos.append(hora)
        return datos
