import unittest
from Request import Request

class TestRequest(unittest.TestCase):
    """ Clase que se encarga de realizar la pruebas unitarias de la clase Request.

    """
    
    def test_getClimaCiudad(self):
        """ Prueba si la conexión con el API y la obtención de los datos se realizo correctamente.
        
        """
        respuesta = Request()
        respuesta.coonectarApi('MEX')
        
        self.assertDictEqual(respuesta.getClimaCiudad()['coord'], {'lon': -99.0721, 'lat': 19.4363})
        self.assertEqual(respuesta.getClimaCiudad()['name'], 'Pantitlán')
        self.assertEqual(respuesta.getClimaCiudad()['id'], 3521944)

if __name__ == '__main__':
    unittest.main()