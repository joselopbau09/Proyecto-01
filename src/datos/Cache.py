import time

class Cache:
    
    def agregaDatos(cache, listaDeDatos, identificador):
        horaActual = time.time()
        if(cache.get(identificador) == None):
            cache[identificador] = listaDeDatos
        elif(horaActual - listaDeDatos[6] > 600000):
            cache[identificador] = listaDeDatos
        elif():
            pass

    def muestraDatos(cache, identificador):
        print("El clima es: " + cache[identificador][0])
        print("La temperatura actual es: " + cache[identificador][1])
        print("La temperatura mínima es: " + cache[identificador][2])
        print("La temperatura máxima es: " +  cache[identificador][3])
        print("La velocidad del viento es: " + cache[identificador][4])
        print("La nubosidad es del: " + cache[identificador][5])

    


 