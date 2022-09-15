import csv
""" Módulo LecturaCiudades """

class LecturaCiudades:
    """ Se encarga de hacer la lectura del archivo de los  datos de las ciudades, archivo de tipo csv.

    Attributes:
        archivoCiudades (str): Localización del archivo a leer.
        ciudades (dic[str]): Almacena como llave la clave única de la ciudad junto con su latitud y longitud.

    """

    def __init__(self):
        """ Constructor que inicializa  los atributos de la clase.

        """
        self.archivoCiudades = 'dataset1.csv'
        self.ciudades = {}
        self.lectura()

    def getCiudades(self):
        """ Método que se encarga de obtener el diccionario de la ciudades.
        
        Returns:
            dic: Clave de la ciudades de la base de datos.
        """
        return self.ciudades

    def getCoordenadas(self, claveCiudad):
        """ Método que se encarga de obtener la longitud y latitud del diccionario de las ciudades.

        Args:
            claveCiudad (str): Clave única de la ciudad a que se consulta en el diccionario.
        
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
        """ Realiza la lectura del archivo de las ciudades.

        """
        with open(self.archivoCiudades, mode = 'r') as file:
            reader = csv.reader(file)  
            self.ciudades = {rows[1]:f'{rows[4]},{rows[5]}' for rows in reader}