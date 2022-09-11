import csv

class LecturaCiudades:

    def __init__(self):
        self.archivoCiudades = 'dataset1.csv'
        self.ciudades = {}
        self.lectura()

    def getCiudades(self):
        return self.ciudades

    def getCoordenadas(self, claveCiudad):
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
        with open(self.archivoCiudades, mode = 'r') as file:
            reader = csv.reader(file)  
            self.ciudades = {rows[1]:f'{rows[4]},{rows[5]}' for rows in reader}

    def imprime(self):
        print(self.ciudades)