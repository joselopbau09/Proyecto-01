
import time

class Cache:

    """Clase para definir el comportamiento del cache.

    """

    def agregaDatos(cache, listaDeDatos, identificador):
        """Método para agregar datos al cache.

        Args:
            cache (dict): diccionario que representa el cache.
            listaDeDatos (list): lista que contiene la información del clima.
            identificador (str): key para el diccionario.
        """

        cache[identificador] = listaDeDatos

    def infoActualizada(cache, identificador):
        """Método para verificar si la información del caché está actualizada, es decir, si tiene menos de 
            10 minutos desde que se guardó la información.

        Args:
            cache (dict): diccionario de donde se verifica la información.
            identificador (str): key del diccionario.

        Return:
            boolean: True si la información está actualizada, False en otro caso.
        """

        horaActual = time.time()
        if(cache.get(identificador) == None):
            return False
        elif(horaActual - cache[identificador][6] > 600000):
            return False
        elif(horaActual - cache[identificador][6] < 600000):
            return True

    def muestraDatos(cache, identificador):
        """Se encarga de crear una cadena.
        
        Args:
            cache (dict): diccionario de donde se extraen los datos.
            identificador (str): key para obtener datos del diccionario.

        Return:
            str: Cadena con la información del aeropuerto proporcionada por la Api.
        """

        informacionClima = f'\
        El clima en {identificador} es: {cache[identificador][0]}\n\
            La temperatura actual es: {cache[identificador][1]}\n\
            La temperatura mínima es: {cache[identificador][2]}\n\
            La temperatura máxima es: {cache[identificador][3]}\n\
            La velocidad del viento es: {cache[identificador][4]}\n\
            La nubosidad es del: {cache[identificador][5]}\n\
            ' 
        return informacionClima    