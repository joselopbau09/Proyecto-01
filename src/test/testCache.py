import unittest
from classes.Request import Request
from classes.Cache import Cache

def almacenaCache(indentificacion, cache):
    respuesta = Request()
    respuesta.conectarApi(indentificacion)
    datos = respuesta.generaDatos()
    Cache.agregaDatos(cache, datos, indentificacion)

class TestLectura(unittest.TestCase):
    """ Clase que se encarga de realizar las pruebas unitarias de la clase Cache.

    """

    def test_infoActualizada(self):
        """ Prueba si la lectura del archivo se realizo correctamente.
        
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
   
if __name__ == '__main__':
    unittest.main()