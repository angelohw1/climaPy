import requests
from translate import Translator

traductor = Translator(to_lang="en")

def get_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }

    response = requests.get(url, params=params)
    data = response.json()

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

def get_coordenadas(ciudad,pais):

    lat = None
    lon = None
    url = "https://geocoding-api.open-meteo.com/v1/search?name="

    response = requests.get(url + ciudad)

    data = response.json()

    if "results" not in data:
        return None

        # Buscar coincidencia exacta
    for resultado in data["results"]:
        if  resultado["name"].lower()== ciudad.lower() and resultado["country"].lower()==(pais.lower()):

           lat = resultado["latitude"]
           lon = resultado["longitude"]

    print(pais)
    return lat, lon

