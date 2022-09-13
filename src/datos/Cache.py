import time

class Cache:
    
    def agregaDatos(cache, listaDeDatos, identificador):
        actual = time.time()
        if(cache == {}):
            cache[identificador] = listaDeDatos
        elif(actual- listaDeDatos[7] > 600):
            cache[identificador] = listaDeDatos
        elif():
            pass

    def muestraDatos(cache, identificador):
        print("El clima actual es: \n")
        print("El clima es: " + cache[identificador][0])
        print("Descripción: " + cache[identificador][1])
        print("La temperatura actual es: " + cache[identificador][2])
        print("La temperatura mínima es: " + cache[identificador][3])
        print("La ttemperatura máxima es: " +  cache[identificador][4])
        print("La velocidad del viento es: " + cache[identificador][5])
        print("La nubosidad es del: " + cache[identificador][6])

    


 