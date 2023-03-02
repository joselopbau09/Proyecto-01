

# Consultor del clima
Se encarga de consultar el clima haciendo uso del lenguaje Python, apoyándose de la Api [OpenWeatherMap](https://openweathermap.org/api).

## Versión o herramientas:

Paqueterias usadas:
- [Requests](https://pypi.org/project/requests/)
- [time](https://docs.python.org/3/library/time.html)
- [json](https://docs.python.org/3/library/json.html)
- [tkinter](https://docs.python.org/es/3/library/tkinter.html)

## Requerimentos
Para ejecutar el programa se necesita:
- Python 3
- Conexión a internet
- instalar la paquetería requests, se puede hacer con el siguiente comando: 
```
> pip install requests
```
- Recuerda que debes agregagar el archivo siguiente en la carpeta assets `key.txt`, el cual debe de almacenar tu llave(activa) proporcionada por la Api OpenWeatherMap

## Cómo ejecutarlo:
1. Dirigirse en la terminal a la carpeta donde está ubicado el archivo llamado `main.pyw` el cual esta en la carpeta src: 
```
Proyecto-01\src>
```
2. Ejecutar el comando 

```
> main.pyw
```
Otra opción dar doble click sobre el archivo `main.pyw`

-Para ejecutar las pruebas unitarias desde la misma posición en el directorio ejecutar el siguiente comando:

```
> python -m unittest discover
```

## Cómo usarlo
- Sólo es necesario seleccionar la clave de la ciudad de donde se desea conocer el clima
- EL programa está preparado para tratar con errores del usuario.

## Entornos donde fue probado
- Windows 10
