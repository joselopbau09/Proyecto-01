import requests, json

# Key
api_key = "ingresa la key"
 
# Url
url = "http://api.openweathermap.org/data/2.5/weather?"
 
# lat lon
lat = input("Enter latitude: ")

lon = input("Enter longitude: ")
 
# concatenación de la url
complete_url = f'{url}lat={lat}&lon={lon}&appid={api_key}'
 

respuesta = requests.get(complete_url)
 
x = json.loads(respuesta.text)

#Imprime el diccionario completo
#print(x)
#print("\n")

#Imprime las llaves del diccionario formado por otros diccionarios
#print(x.keys())
#print("\n")

#Imprime las llaves de algun diccionario dentro del diccionario principal, en este caso de "sys"
#print(x["sys"].keys())
#print("\n")

#Lista en el diccionario que contiene las características del clima
clima = x["weather"]

#Imprime los elementos específicos del clima
print("El clima es el siguiente: \n ")
print("El estado del clima es: " + clima[-1]["main"])
print("Descricpion del clima: " + clima[-1]["description"])
print("La temperatura actual es: " + str(x["main"]["temp"]) + " °K")
print("La temperatura mínima es: " + str(x["main"]["temp_min"]) + " °K")
print("La temperatura máxima es: " + str(x["main"]["temp_max"]) + " °K")
print("La velocidad del viento es: " + str(x["wind"]["speed"]) + " m/s")
print("La nubosidad es del: " + str(x["clouds"]["all"]) + "%")




