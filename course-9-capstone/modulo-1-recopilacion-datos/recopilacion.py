# Modulo 1: Recopilacion de datos — API y web scraping

import requests
import pandas as pd
from bs4 import BeautifulSoup

# ===================== API REST =====================

url_api = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.json"

print("Descargando dataset de la survey...")
respuesta = requests.get(url_api)

if respuesta.status_code == 200:
    datos = respuesta.json()
    df = pd.DataFrame(datos)
    print(f"Dataset cargado: {df.shape[0]} filas, {df.shape[1]} columnas")
    print("\nPrimeras columnas:")
    print(df.columns[:10].tolist())
    print("\nPrimeras filas:")
    print(df.head(3))
    df.to_csv("survey_data.csv", index=False)
    print("\nDataset guardado como survey_data.csv")
else:
    print(f"Error al cargar el dataset: {respuesta.status_code}")

# ===================== WEB SCRAPING =====================

url_web = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"

print("\nExtrayendo datos de lenguajes de programacion...")
respuesta_web = requests.get(url_web)
soup = BeautifulSoup(respuesta_web.text, "html.parser")

tabla = soup.find("table")
if tabla:
    df_lenguajes = pd.read_html(str(tabla))[0]
    print(f"Tabla extraida: {df_lenguajes.shape}")
    print(df_lenguajes.head(10))
    df_lenguajes.to_csv("lenguajes_popularidad.csv", index=False)
    print("Guardado como lenguajes_popularidad.csv")
else:
    print("No se encontro tabla en la pagina")
