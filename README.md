# Consultor del clima
Se encarga de consultar el clima haciendo uso del lenguaje Python, apoyándose de la Api OpenWeatherMap.

## Versión o herramientas:

Paqueterias usadas:
- Requests
- time
- json

## Requerimentos
Para ejecutar el programa se necesita:
- Python 3
- Conexión a internet
- instalar la paquetería requests, se puede hacer con el siguiente comando: 
```
$ python -m pip install requests
```

## Cómo ejecutarlo:
1. Dirigirse en la terminal a la carpeta donde está ubicado el archivo llamado main.py el cual esta en la carpeta test: 
```
Proyecto-01/src/test$
```
2. Ejecutar el comando 

```
$ python3 main.py
```
-Para ejecutar las pruebas unitarias desde la misma posición en el directorio ejecutas el siguinete comando:

```
python -m unittest discover
```

## Cómo usarlo
- Sólo es necesario ingresar el indice de la ciudad de donde se desea conocer el clima.
- EL programa está preparado para tratar con errores del usuario.
- Para terminar la ejecución se debe ingresar el digito `0` en la terminal.

## Entornos donde fue probado
- Debian 11
- Ubuntu 20.4
