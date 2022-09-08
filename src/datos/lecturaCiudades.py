from ast import If
import csv

class LecturaCiudades:

    def __init__(self, archivoCiudades):
        self.archivoCiudades = archivoCiudades
        self.ciudades = {}

    def getCiudades(self):
        return self.ciudades

    def getCoordenadas(self, claveCiudad):
        coordenadas = []
        latitud = ''
        longitud = ''
        coordenadaLatLon = self.ciudades.get(claveCiudad)
        i = 0
        while (i < len(coordenadaLatLon)):
            if (coordenadaLatLon[i] == ','):
                coordenadaLatLon[i] = ''                
                longitud = coordenadaLatLon
                break
            latitud += coordenadaLatLon[i]
            coordenadaLatLon[i] = ''
            i += 1
        coordenadas.append(latitud)            
        coordenadas.append(longitud)          

        return coordenadas  

    def lectura(self):
        with open(self.archivoCiudades, mode = 'r') as file:
            reader = csv.reader(file)  
            self.ciudades = {rows[1]:f'{rows[4]},{rows[5]}' for rows in reader}

    def imprime(self):
        print(self.ciudades)

def main():
    a = LecturaCiudades('dataset1.csv')
    a.lectura()
    a.imprime()

main()   

