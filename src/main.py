from classes.LecturaCoordenadas import LecturaCoordenadas
from classes.Cache import *
from classes.Request import *

def getInt(mensaje, error,min, max):
    """Se encarga de interactuar con el usuario mediante terminal, dependiendo si el valor es aceptado imprime un error o el menú.
    
    Args:
        mensaje (str): Menú que se muestr al usuario.
        error (str): Mensaje de error que se le muestra al usuario, si ingresa un valor incorrecto.
        min (int): Limite inferior de los valores aceptados.
        max (int): Limite superior de los valores aceptados.
    
    Returns:
        int: Regresa el la opción selecionada por el usuario.

    """

    while (True):
        print(mensaje)
        valorIngresado = input()
        if valorIngresado.isnumeric():
            if (int(valorIngresado) < min or max < int(valorIngresado)):
                print(error)
            else:
                return int(valorIngresado)
        else:
            print(error)

def getMenu(aeropuertos):
    """ Crea un menú con las claves única de los aeropuertos.

    Args:
        ciudad (list[str]): Contiene las claves de los aeropuertos. 

    Returns:
        str: El menú formado con las claves.   

    """
    indice = 1
    menu = ''
    while( indice < len(aeropuertos) ):
        menu += f'{indice}: {aeropuertos[indice]}\t\t\t\t\t'
        if indice%2 == 0:
            menu += '\n'
        indice += 1
    return menu     

def main():

    lectura = LecturaCoordenadas()
    dicAeropuertos = lectura.getCiudades()
    menu = getMenu(list(dicAeropuertos.keys()))
    
    while(True):
        print("Elige una ciudad ingresando su índice, si deseas terminar la ejcución ingresa 0: \n")
        opcion = getInt(menu, 'Ingrese una opción valida', 0, 45)
        if( opcion == 0):    
            break
        identificador = list(dicAeropuertos.keys())[opcion]
        print("El clima en " + identificador + " es: \n")
        solicitud = Request()
        cache = {}

        if(cache == {}):
            solicitud.conectarApi(identificador)
            datos = solicitud.generaDatos()
            Cache.agregaDatos(cache,datos,identificador)
            Cache.muestraDatos(cache, identificador)
            print()

        elif(Cache.infoActualizada(cache, identificador) == True):
            Cache.muestraDatos(cache, identificador)
            print()

        elif():
            solicitud.conectarApi(identificador)
            datos = solicitud.generaDatos()
            Cache.agregaDatos(cache,datos,identificador)
            Cache.muestraDatos(cache, identificador)
            print()
main()