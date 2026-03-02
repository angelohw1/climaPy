import openpyxl as ox
from analisis import mostrar_mayor_temperatura, mostrar_menor_temperatura, mostrar_velocidad_viento
from api_client import get_weather, get_ciudad, get_pais, get_coordenadas, get_weatherDetail


from translate import Translator

traductor = Translator(to_lang="en")

def dia_o_noche(parametro):

    if parametro == 1:
        actual = "dia"
    else:
        actual = "noche"
    return actual

def direccion_viento(grados):
    direccion = None
    if (grados >= 337.5 or grados < 22.5):
        direccion = "Norte"
    elif grados < 67.5:
        direccion = "Noreste"
    elif grados < 112.5:
        direccion = "Este"
    elif grados < 157.5:
        direccion = "Sureste"
    elif grados < 202.5:
        direccion = "Sur"
    elif grados < 247.5:
        direccion = "Suroeste"
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

    return estado


def add_rows(filas):
    workbook = ox.load_workbook("clima.xlsx")

    clima_sheet = workbook["clima"]
    numFila = clima_sheet.max_row + 1
    numFila = str(numFila)
    letrasColumna = ["A", "B", "C", "D", "E", "F", "G", "H"]

    for i in range(len(letrasColumna)):
        celdaFinal = str(letrasColumna[i] + numFila)

        clima_sheet[celdaFinal] = filas[i]
    workbook.save("clima.xlsx")
    workbook.close()


def mostrarMenu():
    print("----MENÚ-----")
    print("1-- Mostar tiempos climáticos actuales")
    print("2-- Añadir tiempos climáticos  ")
    print("3-- Eliminar tiempos climáticos ")
    print("4-- Mostrar tiempo Actual")
    print("5-- Filtrar tiempo  climátco por ciudad")
    print("6-- Filtrar tiempo climático por país")
    print("7-- Mostrar mayor temperatura")
    print("8-- Mostrar menor temperatura")
    print("9-- Mostrar Velocidad del viento")
    print("10- Salir")

def mostrarTemperaturaActual():
    ## Pides el pais y  la ciudad

    ##comprobar que el pais y la ciudad existan en la tabla, que sean concididnes una misma fila

    # mostrar el pais con con su ciudad, toda su fila, guardar en variable





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

    latitud, longitud = get_coordenadas(ciudad, pais)
    print(latitud, longitud)

    print(f"***************TIEMPO EN {ciudad.upper()}******************")
    weather = get_weather(latitud, longitud)
    weather_detail = get_weatherDetail(latitud, longitud)

    print("Temperatura :", weather["temperature"], "Cº")

    print("Altitud sobre el nivel del mar: ", weather_detail["elevation"], "metros")

    print("Viento:", weather["windspeed"], "km/h")

    print("Actualmente es de ", dia_o_noche(weather["is_day"]))

    print("Dirección del viento: ", direccion_viento(weather["winddirection"]))

    print("Estado del clima: ", estadoTiempo(weather["weathercode"]))

    print("\nRespuesta generada en: ", weather_detail["generationtime_ms"], "milisegundos ")


def añadirTiempoClimatico():

    filaDatos = []
    pais = input("Introduce un país: ")
    pais = pais.capitalize()

    pais = traductor.translate(pais)
    pais = pais.strip()
    print(pais)

    while not get_pais(pais):
        print("El país introducido  no existe ")
        pais = input("Por favor introduzca un país correcto: ")
        pais = pais.strip()

    filaDatos.append(pais)  # Añadimos el país

    ciudad = input("Introduce una ciudad: ")
    ciudad = ciudad.capitalize()
    ciudad = ciudad.strip()

    while not get_ciudad(ciudad):
        print("La ciudad  introducida no existe ")
        ciudad = input("Por favor introduzca una ciudad correcta: ")
        ciudad = ciudad.strip()

    filaDatos.append(ciudad)  # Añadimos ciudad

    latitud, longitud = get_coordenadas(ciudad, pais)

    weather = get_weather(latitud, longitud)
    weather_detail = get_weatherDetail(latitud, longitud)

    filaDatos.append(weather["temperature"])

    filaDatos.append(weather_detail["elevation"])  # añadimos altiud

    filaDatos.append(weather["windspeed"])  # añadimos velocidad del viento

    filaDatos.append(dia_o_noche(weather["is_day"]))  # añadimos si es de día o no

    filaDatos.append(direccion_viento(weather["winddirection"]))  # añadimos la dirección del viento

    filaDatos.append(estadoTiempo(weather["weathercode"]))  # Añadimos el estado del tiempo

    add_rows(filaDatos)

    print("-------------------TIEMPO CLIMÁTICO REGISTRADO CORRECTAMENTE--------------")


salir = False

while not salir:

   try:
       mostrarMenu()
       opcionMenu = input("Introduzca una opción del menú (1-10): ")

       opcionMenu = int(opcionMenu)

       if opcionMenu == 1:
           pass
       elif opcionMenu == 2:
           añadirTiempoClimatico()
       elif opcionMenu == 3:
           mostrarTemperaturaActual()
       elif opcionMenu == 4:
           pass
       elif opcionMenu == 5:
           pass
       elif opcionMenu == 6:
           pass
       elif opcionMenu == 7:
           mostrar_mayor_temperatura()
       elif opcionMenu == 8:
           mostrar_menor_temperatura()
       elif opcionMenu == 9:
           mostrar_velocidad_viento()
       elif opcionMenu == 10:
           print("Fin del programa")
           salir = True


       else:
           opcionMenu = input("La opción escogida es incorecta\nPor favor escoga una de las opciones del menú(1-10): ")
   except ValueError:
       print("\nLa opción escogida no puede ser numérica")











