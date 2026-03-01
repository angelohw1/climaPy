from api_client import get_weather, get_ciudad, get_pais, get_coordenadas, get_weatherDetail

from translate import Translator
traductor = Translator(to_lang="en")


def dia_o_noche(parametro):
    if parametro == 1:
        print("Actualmente es de día")
    else:
        print("Actualmente es de noche")

def direccion_viento(grados):

    direccion = None
    if (grados >= 337.5 or grados < 22.5):
        direccion =  "Norte"
    elif grados < 67.5:
        direccion = "Noreste"
    elif grados < 112.5:
        direccion =  "Este"
    elif grados < 157.5:
        direccion = "Sureste"
    elif grados < 202.5:
        direccion =  "Sur"
    elif grados < 247.5:
        direccion =   "Suroeste"
    elif grados < 292.5:
        direccion = "Oeste"
    else:
        direccion = "Noroeste"

    return direccion

def estadoTiempo(parametro):

    estado = None
    if parametro == 0:
        estado = "Despejado"
    elif parametro == 1:
        estado = "Parcialmente nublado"
    elif parametro == 2:
        estado = "Nublado"
    elif parametro == 3:
        estado = "Muy nublado"

    return  estado


pais = input("Introduce un país: ")
pais = pais.capitalize()

pais = traductor.translate(pais)
pais = pais.strip()
print(pais)


while not get_pais(pais):
    print("El país introducido  no existe ")
    pais = input("Por favor introduzca un país correcto: ")
    pais = pais.strip()

ciudad = input("Introduce una ciudad: ")
ciudad = ciudad.capitalize()
ciudad = ciudad.strip()
print(ciudad)

while not get_ciudad(ciudad):
    print("La ciudad  introducida no existe ")
    ciudad = input("Por favor introduzca una ciudad correcta: ")
    ciudad = ciudad.strip()



latitud,longitud = get_coordenadas(ciudad,pais)
print(latitud,longitud)

print(f"***************TIEMPO EN {ciudad.upper()}******************")
weather = get_weather(latitud, longitud)
weather_detail = get_weatherDetail(latitud,longitud)

print("Temperatura :", weather["temperature"] , "Cº")
print("Viento:", weather["windspeed"], "km/h")
print("Altitud sobre el nivel del mar: ",weather_detail["elevation"], "metros")
dia_o_noche(weather["is_day"])

print("Dirección del viento: ",direccion_viento(weather["winddirection"]))

print("Estado del clima: ", estadoTiempo(weather["weathercode"]))


print("\nRespuesta generada en: ", weather_detail["generationtime_ms"], "milisegundos ")



