import pandas as pd

def cargar_datos():
    try:
        df = pd.read_excel("clima.xlsx")

        df.columns = [
            "Country",
            "City",
            "Temperature",
            "Elevation",
            "Windspeed",
            "Day/Night",
            "Wind Direction",
            "Weather State"
        ]
        df["Temperature"] = pd.to_numeric(df["Temperature"])
        df["Windspeed"] = pd.to_numeric(df["Windspeed"])
        df["Elevation"] = pd.to_numeric(df["Elevation"])

        return df

    except FileNotFoundError:
        print("No se encontró el archivo clima.xlsx")
        return None

def mostrar_toda_tabla():
    df = cargar_datos()

    if df is not None and not df.empty:
        print("\nTABLA COMPLETA DE DATOS CLIMÁTICOS:\n")
        print(df.to_string(index=False))
    else:
        print("No hay datos disponibles.")

def mostrar_mayor_temperatura():
    df = cargar_datos()
    if df is not None and not df.empty:

        max_temp = df["Temperature"].max()
        fila = df[df["Temperature"] == max_temp]

        print("\nMayor temperatura registrada:")
        print(fila[["Country", "City", "Temperature"]])

    else:
        print("No hay datos disponibles.")

def mostrar_menor_temperatura():
    df = cargar_datos()
    if df is not None and not df.empty:

        min_temp = df["Temperature"].min()
        fila = df[df["Temperature"] == min_temp]

        print("\nMenor temperatura registrada:")
        print(fila[["Country", "City", "Temperature"]])

    else:
        print("No hay datos disponibles.")

def mostrar_velocidad_viento():
    df = cargar_datos()
    if df is not None and not df.empty:

        max_wind = df["Windspeed"].max()
        fila = df[df["Windspeed"] == max_wind]

        print("\nMayor velocidad del viento registrada:")
        print(fila[["Country", "City", "Windspeed"]])

    else:
        print("No hay datos disponibles.")

def filtrar_por_ciudad():
    df = cargar_datos()

    if df is not None and not df.empty:

        ciudad = input("Introduce la ciudad: ").strip()

        resultado = df[df["City"].str.lower() == ciudad.lower()]

        if not resultado.empty:
            print(f"\nDatos del clima ciudad: {ciudad}\n")
            print(resultado.to_string(index=False))
        else:
            print("No se encontraron datos para esa ciudad.")

    else:
        print("No hay datos disponibles.")

def filtrar_por_pais():
    df = cargar_datos()

    if df is not None and not df.empty:

        pais = input("Introduce el país: ").strip()
        resultado = df[df["Country"].str.lower() == pais.lower()]

        if not resultado.empty:
            print(f"\nDatos del clima pais: {pais}\n")
            print(resultado.to_string(index=False))
        else:
            print("No se encontraron datos para ese país.")

    else:
        print("No hay datos disponibles.")