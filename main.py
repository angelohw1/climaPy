from api_client import get_weather

lat = 40.4168
lon = -3.7038

weather = get_weather(lat, lon)

print("Temperatura:", weather["temperature"])
print("Viento:", weather["windspeed"])
