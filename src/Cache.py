import time

class Cache:

    """Clase para definir el comportamiento del cache

    """

    def agregaDatos(cache, listaDeDatos, identificador):
        """Método para agregar datos al cache, verifica si ya están y su antigüedad.

        Args:
            cache (dict): diccionario que representa el cache
            listaDeDatos (list): lista que contiene la información del clima 
            identificador (str): key para el diccionario
        """
        horaActual = time.time()
        if(cache.get(identificador) == None):
            cache[identificador] = listaDeDatos
        elif(horaActual - listaDeDatos[6] > 600000):
            cache[identificador] = listaDeDatos
        elif():
            pass

    def muestraDatos(cache, identificador):
        """Imprime los datos en la terminal
        
        Args:
            cache (dict): diccionario de donde se extraen los datos
            identificador (str): key para obtener datos del diccionario

        """
        print("El clima es: " + cache[identificador][0])
        print("La temperatura actual es: " + cache[identificador][1])
        print("La temperatura mínima es: " + cache[identificador][2])
        print("La temperatura máxima es: " +  cache[identificador][3])
        print("La velocidad del viento es: " + cache[identificador][4])
        print("La nubosidad es del: " + cache[identificador][5])

    


 