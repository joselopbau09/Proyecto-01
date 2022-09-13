import unittest
from datos.getDatos import Request

class TestRequest(unittest.TestCase):
    
    def test_getClimaCiudad(self):
        respuesta = Request()
        respuesta.coonectarApi('MEX')
        
        self.assertDictEqual(respuesta.getClimaCiudad()['coord'], {'lon': -99.0721, 'lat': 19.4363})
        self.assertEqual(respuesta.getClimaCiudad()['name'], 'Pantitlán')
        self.assertEqual(respuesta.getClimaCiudad()['id'], 3521944)

if __name__ == '__main__':
    unittest.main()