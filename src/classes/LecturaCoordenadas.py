import csv

""" Módulo LecturaCoordenadas """

class LecturaCoordenadas:
    """ Se encarga de hacer la lectura del archivo de los datos de las ciudades, archivo de tipo csv.

    Attributes:
        archivoCoordenadas (str): Localización del archivo a leer.
        ciudades (dic[str]): Almacena como llave la clave única de la ciudad junto con su latitud y longitud.

    """

    def __init__(self):
        """ Constructor que inicializa  los atributos de la clase.

        """
        self.archivoCoordenadas = 'assets/dataset1.csv'
        self.ciudades = {}
        self.lectura()

    def getCiudades(self):
        """ Método que se encarga de obtener el diccionario de las ciudades.
        
        Returns:
            dic: Clave del aeropuerto de la base de datos.
        """
        return self.ciudades

    def getCoordenadas(self, claveCiudad):
        """ Método que se encarga de obtener la longitud y latitud del diccionario de las ciudades.

        Args:
            claveCiudad (str): Clave única de la ciudad que se consulta en el diccionario.
        
        Returns:
            list(str): Lista con la latitud y longitud de la ciudad dada.    
        
        """
        coordenadas = []
        latitud = ''
        longitud = ''
        coordenadaLatLon = self.ciudades.get(claveCiudad)
        latitudLongitud = list(coordenadaLatLon)
        i = 0
        while (i < len(coordenadaLatLon)):
            if (latitudLongitud[i] == ','):
                latitudLongitud[i] = ''                
                longitud = "".join(latitudLongitud)
                break
            latitud += latitudLongitud[i]
            latitudLongitud[i] = ''
            i += 1
        coordenadas.append(latitud)            
        coordenadas.append(longitud)          

        return coordenadas  

    def lectura(self):
        """ Realiza la lectura del archivo que contiene las coordenadas

        """
        with open(self.archivoCoordenadas, mode = 'r') as file:
            reader = csv.reader(file)  
            self.ciudades = {rows[1]:f'{rows[4]},{rows[5]}' for rows in reader}
def main():
    lectura = LecturaCoordenadas()
main()                