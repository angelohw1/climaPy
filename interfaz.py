import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default = "browser"

EXCEL_FILE = "clima.xlsx"
SHEET_NAME = "clima"


def cargar_datos():
    df = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME)

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

    df["Temperature"] = pd.to_numeric(df["Temperature"], errors="coerce")
    df["Windspeed"] = pd.to_numeric(df["Windspeed"], errors="coerce")
    df["Elevation"] = pd.to_numeric(df["Elevation"], errors="coerce")

    return df


def mostrar_pie_chart():
    df = cargar_datos()

    if df.empty:
        print("No hay datos disponibles.")
        return

    conteo = df["Weather State"].value_counts().reset_index()
    conteo.columns = ["Estado", "Cantidad"]

    fig = px.pie(
        conteo,
        names="Estado",
        values="Cantidad",
        title="Distribución del Estado del Clima"
    )

    fig.show()



def mostrar_overview(tipo):
    df = cargar_datos()

    if df.empty:
        print("No hay datos disponibles.")
        return

    if tipo == "altitud":
        df_sorted = df.sort_values(by="Elevation")
        y = df_sorted["Elevation"]
        titulo = "Altitud (menor a mayor)"
    elif tipo == "max_temp":
        df_sorted = df.sort_values(by="Temperature")
        y = df_sorted["Temperature"]
        titulo = "Temperatura (menor a mayor)"
    elif tipo == "min_temp":
        df_sorted = df.sort_values(by="Temperature")
        y = df_sorted["Temperature"]
        titulo = "Temperatura (menor a mayor)"
    elif tipo == "viento":
        df_sorted = df.sort_values(by="Windspeed")
        y = df_sorted["Windspeed"]
        titulo = "Velocidad del Viento (menor a mayor)"
    else:
        return

    x = df_sorted["City"]

    fig = go.Figure(
        data=[
            go.Bar(x=x, y=y)
        ]
    )

    fig.update_layout(
        title=titulo,
        xaxis_title="Ciudad",
        yaxis_title="Valor",
    )

    fig.show()

def mostrar_tabla_completa_grafica():
    df = cargar_datos()

    if df.empty:
        print("No hay datos disponibles.")
        return

    df["Lugar"] = df["City"] + " - " + df["Country"]

    fig = go.Figure()

    # 1. Temperatura
    fig.add_trace(go.Bar(
        x=df["Lugar"],
        y=df["Temperature"],
        name="Temperatura Cª"
    ))


    fig.add_trace(go.Bar(
        x=df["Lugar"],
        y=df["Windspeed"],
        name="Velocidad del viento",
        offsetgroup=2  # Grupo 2
    ))

    fig.add_trace(go.Bar(
        x=df["Lugar"],
        y=df["Elevation"],
        name="Altitud",
        yaxis="y2",
        offsetgroup=3
    ))

    fig.update_layout(
        title="Clima General por Ciudad y País",
        xaxis_title="Ciudad - País",
        yaxis=dict(title="Temperatura / Viento"),
        yaxis2=dict(
            title="Altitud",
            overlaying="y",
            side="right"
        ),

        barmode="group",
        legend_title="Series de Datos"
    )

    fig.show()

