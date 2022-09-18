import unittest
from classes.Request import Request
from classes.Cache import Cache

def almacenaCache(indentificacion, cache):
    """ Se encarga de hacer la llamada a la Api y de almacenar la infroemación en el cache.

    Args:
        indetificacion (str): Clave de la ciudad.
        cache (dic): Donde se alamcena la información.
    
    """
    
    respuesta = Request()
    respuesta.conectarApi(indentificacion)
    datos = respuesta.generaDatos()
    Cache.agregaDatos(cache, datos, indentificacion)

class TestLectura(unittest.TestCase):
    """ Clase que se encarga de realizar las pruebas unitarias de la clase Cache.

    """
<<<<<<< HEAD
    
    resultadoDic = {'destination': 'destination_latitude,destination_longitude', 'MTY': '25.7785,-100.107', 'TLC': '19.3371,-99.566', 'MEX': '19.4363,-99.0721', 'TAM': '22.2964,-97.8659', 'GDL': '20.5218,-103.311', 'CJS': '31.6361,-106.429', 'CUN': '21.0365,-86.8771', 'TIJ': '32.5411,-116.97', 'HMO': '29.0959,-111.048', 'CME': '18.6537,-91.799', 'MID': '20.937,-89.6577', 'CTM': '18.5047,-88.3268', 'VER': '19.1459,-96.1873', 'OAX': '16.9999,-96.7266', 'HUX': '15.7753,-96.2626', 'ZIH': '17.6016,-101.461', 'PVR': '20.6801,-105.254', 'LIM': '-12.0219,-77.1143', 'HAV': '22.9892,-82.4091', 'BOG': '4.70159,-74.1469', 'MIA': '25.7932,-80.2906', 'LAX': '33.9425,-118.408', 'JFK': '40.6398,-73.7789', 'TRC': '25.5683,-103.411', 'PXM': '15.8769,-97.0891', 'ACA': '16.7571,-99.754', 'MZT': '23.1614,-106.266', 'GUA': '14.5833,-90.5275', 'VSA': '17.997,-92.8174', 'BZE': '17.5391,-88.3082', 'DFW': '32.8968,-97.038', 'ORD': '41.9786,-87.9048', 'PHX': '33.4343,-112.012', 'PHL': '39.8719,-75.2411', 'CLT': '35.214,-80.9431', 'YYZ': '43.6772,-79.6306', 'IAH': '29.9844,-95.3414', 'YVR': '49.1939,-123.184', 'CDG': '49.0128,2.55', 'ZCL': '22.8971,-102.687', 'AMS': '52.3086,4.76389', 'ATL': '33.6367,-84.4281', 'CEN': '27.3926,-109.833', 'MAD': '40.4719,-3.56264', 'SCL': '-33.393,-70.7858'}
    
    def test_getCoordenadas(self):
        """ Prueba si la lectura del archivo se realizo correctamente.
        
        """
        lc = LecturaCiudades()
        self.assertListEqual(lc.getCoordenadas('TAM'), ['22.2964','-97.8659'])
        self.assertListEqual(lc.getCoordenadas('SCL'), ['-33.393','-70.7858'])
        self.assertListEqual(lc.getCoordenadas('GDL'), ['20.5218','-103.311'])

        self.assertDictEqual(lc.getCiudades(), self.resultadoDic)
=======

    def test_infoActualizada(self):
        """ Prueba si la información que se almacena en el cache se hace de forma correcta.
        
        """
        
        respuesta = Request()
        cache = {}
        self.assertFalse(Cache.infoActualizada(cache, 'MEX'))
        self.assertFalse(Cache.infoActualizada(cache, 'LAX'))
        self.assertFalse(Cache.infoActualizada(cache, 'BZE'))
        
        almacenaCache('MEX', cache)
        almacenaCache('LAX', cache)
        almacenaCache('BZE', cache)

        self.assertTrue(Cache.infoActualizada(cache, 'MEX'))
        self.assertTrue(Cache.infoActualizada(cache, 'LAX'))
        self.assertTrue(Cache.infoActualizada(cache, 'BZE'))
   
>>>>>>> 9a0c9e14a14d3458693db302a31f5d11f2ed7a35
if __name__ == '__main__':
    unittest.main()