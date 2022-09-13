from lecturaCiudades import LecturaCiudades
from Cache import *
from Request import *

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
        val = input()
        if val.isnumeric():
            if (int(val) < min or max < int(val)):
                print(error)
            else:
                return int(val)
        else:
            print(error)

def getMenu(ciudades):
    """ Crea un menú con las claves única de las ciudades.

        Args:
            ciudad (list[str]): Contiene las claves de las ciudades. 

         Returns:
            str: El menú formado con las claves.   

    """
    i = 1
    menu = ''
    while( i < len(ciudades) ):
        menu += f'{i}: {ciudades[i]}\t\t\t\t\t'
        if i%2 == 0:
            menu += '\n'
        i += 1
    return menu     

def main():

    while(True):
        lc = LecturaCiudades()
        dicCiudades = lc.getCiudades()
        menu = getMenu(list(dicCiudades.keys()))
        opcion = getInt(menu, 'Ingrese una opción valida', 1, 45)
        identificador = list(dicCiudades.keys())[opcion]
        print("El clima en " + identificador + " es: \n")
        a = Request()
        cache = {}
        a.coonectarApi(identificador)
        datos = a.generaDatos()
        Cache.agregaDatos(cache, datos, identificador)
        Cache.muestraDatos(cache, identificador)

main()