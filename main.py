import openpyxl as ox
from openpyxl import load_workbook

from analisis import *
from api_client import get_weather, get_ciudad, get_pais, get_coordenadas, get_weatherDetail
from translate import Translator
from interfaz import mostrar_pie_chart, mostrar_overview

traductorIngles = Translator(to_lang="en")
traductorEspañol = Translator(to_lang="es")


def dia_o_noche(parametro):
    return "Día" if parametro == 1 else "Noche"


def direccion_viento(grados):
    if (grados >= 337.5 or grados < 22.5):
        return "Norte"
    elif grados < 67.5:
        return "Noreste"
    elif grados < 112.5:
        return "Este"
    elif grados < 157.5:
        return "Sureste"
    elif grados < 202.5:
        return "Sur"
    elif grados < 247.5:
        return "Suroeste"
    elif grados < 292.5:
        return "Oeste"
    else:
        return "Noroeste"


def estadoTiempo(parametro):
    estados = {
        0: "Despejado",
        1: "Parcialmente nublado",
        2: "Nublado",
        3: "Muy nublado"
    }
    return estados.get(parametro, "Desconocido")

def add_rows(filas):
    workbook = ox.load_workbook("clima.xlsx")
    clima_sheet = workbook["clima"]
    numFila = clima_sheet.max_row + 1
    letrasColumna = ["A", "B", "C", "D", "E", "F", "G", "H"]

    for i in range(len(letrasColumna)):
        clima_sheet[f"{letrasColumna[i]}{numFila}"] = filas[i]

    workbook.save("clima.xlsx")
    workbook.close()


def eliminarTiempoClimático():
    paisEliminado = input("Introduzca el país registrado: ").strip().lower()
    ciudadEliminada = input("Introduzca la ciudad eliminada: ").strip().lower()

    archivo = "clima.xlsx"
    workbook = load_workbook(archivo)
    clima_sheet = workbook["clima"]

    eliminacionPosible = False

    for i in range(clima_sheet.max_row, 1, -1):
        pais = clima_sheet[f"A{i}"].value
        ciudad = clima_sheet[f"B{i}"].value

        if str(pais).strip().lower() == paisEliminado and \
           str(ciudad).strip().lower() == ciudadEliminada:
            clima_sheet.delete_rows(i)
            eliminacionPosible = True

    if eliminacionPosible:
        workbook.save(archivo)
        print("REGISTRO ELIMINADO CORRECTAMENTE ✅")
    else:
        print("No se encontró el registro")

    workbook.close()

def añadirTiempoClimatico():

    filaDatos = []

    pais = input("Introduce un país: ")
    pais = traductorIngles.translate(pais).strip().lower()

    while not get_pais(pais):
        print("El país no existe.")
        pais = traductorIngles.translate(
            input("Introduzca un país correcto: ")
        ).strip().lower()

    filaDatos.append(traductorEspañol.translate(pais.capitalize()))

    ciudad = input("Introduce una ciudad: ").strip().lower()

    while not get_ciudad(ciudad):
        print("La ciudad no existe.")
        ciudad = input("Introduzca una ciudad correcta: ").strip().lower()

    filaDatos.append(ciudad.capitalize())

    latitud, longitud = get_coordenadas(ciudad, pais)

    weather = get_weather(latitud, longitud)
    weather_detail = get_weatherDetail(latitud, longitud)

    filaDatos.append(weather["temperature"])
    filaDatos.append(weather_detail["elevation"])
    filaDatos.append(weather["windspeed"])
    filaDatos.append(dia_o_noche(weather["is_day"]))
    filaDatos.append(direccion_viento(weather["winddirection"]))
    filaDatos.append(estadoTiempo(weather["weathercode"]))

    add_rows(filaDatos)
    print("TIEMPO CLIMÁTICO REGISTRADO CORRECTAMENTE ✅")

def mostrarMenu():
    print("\n-------- MENÚ --------")
    print("1-- Mostrar tabla completa (modo texto)")
    print("2-- Añadir tiempo climático")
    print("3-- Eliminar tiempo climático")
    print("4-- Mostrar altitud")
    print("5-- Filtrar por ciudad")
    print("6-- Filtrar por país")
    print("7-- Mostrar temperaturas")
    print("8-- Mostrar velocidad del viento")
    print("9-- Mostrar distribución estado clima")
    print("10- Salir")



salir = False

while not salir:

    mostrarMenu()

    try:
        opcionMenu = int(input("Seleccione una opción (1-10): "))
    except ValueError:
        print("Debe introducir un número válido.")
        continue

    if opcionMenu == 1:
        mostrar_toda_tabla()

    elif opcionMenu == 2:
        añadirTiempoClimatico()

    elif opcionMenu == 3:
        eliminarTiempoClimático()

    elif opcionMenu == 4:
        mostrar_overview("altitud")

    elif opcionMenu == 5:
        filtrar_por_ciudad()

    elif opcionMenu == 6:
        filtrar_por_pais()

    elif opcionMenu == 7:
        mostrar_overview("max_temp")

    elif opcionMenu == 8:
        mostrar_overview("viento")

    elif opcionMenu == 9:
        mostrar_pie_chart()

    elif opcionMenu == 10:
        print("Fin del programa")
        salir = True

    else:
        print("Opción incorrecta.")