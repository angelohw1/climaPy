import requests
from translate import Translator

traductor = Translator(to_lang="en")

def get_weather(lat, lon):

    if lat is None or lon is None:
        print("Coordenadas inválidas")
        return None

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Error API:", response.status_code)
        return None

    try:
        data = response.json()
    except:
        print("Error al convertir JSON")
        return None

    if "current_weather" not in data:
        print("No hay datos de clima")
        return None

    return data["current_weather"]

def get_weatherDetail(lat,lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data


def get_ciudad(ciudad):

    ciudadCorrecta = False
    url = "https://geocoding-api.open-meteo.com/v1/search?name="

    response = requests.get(url + ciudad)

    data = response.json()

    if "results" not in data:
        return None

        # Buscar coincidencia exacta
    for resultado in data["results"]:
        if resultado["name"].lower() == ciudad.lower():
            ciudadCorrecta =  True

    print(ciudad)
    return ciudadCorrecta


def get_pais(pais):

    paisCorrecto = False
    url = "https://geocoding-api.open-meteo.com/v1/search?name="

    response = requests.get(url + pais)

    data = response.json()

    if "results" not in data:
        return None

        # Buscar coincidencia exacta
    for resultado in data["results"]:
        if resultado["name"].lower() == pais.lower():
            paisCorrecto =  True

    print(pais)

    return paisCorrecto

def get_coordenadas(ciudad, pais):

    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": ciudad,
        "count": 10
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Error en geocoding:", response.status_code)
        return None, None

    try:
        data = response.json()
    except:
        print("Error al decodificar JSON")
        return None, None

    if "results" not in data:
        return None, None

    for resultado in data["results"]:
        if resultado["name"].lower() == ciudad.lower():

            return resultado["latitude"], resultado["longitude"]

    return None, None
