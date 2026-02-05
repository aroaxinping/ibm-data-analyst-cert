# Modulo 5: APIs and Data Collection — Ejercicios

import requests
import pandas as pd

# ===================== API REST (ejemplo con API publica) =====================

# API de paises — no requiere autenticacion
def obtener_pais(nombre):
    """Obtiene informacion de un pais desde la API REST Countries."""
    url = f"https://restcountries.com/v3.1/name/{nombre}"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()[0]
        return {
            "nombre": datos["name"]["common"],
            "capital": datos.get("capital", ["N/A"])[0],
            "poblacion": datos["population"],
            "region": datos["region"]
        }
    else:
        print(f"Error {respuesta.status_code}")
        return None

# pais = obtener_pais("spain")
# print(pais)

# ===================== PARAMETROS EN URL =====================

def buscar_libros(titulo):
    """Busca libros en la API de Open Library."""
    url = "https://openlibrary.org/search.json"
    params = {"q": titulo, "limit": 5}
    respuesta = requests.get(url, params=params)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        libros = []
        for libro in datos["docs"]:
            libros.append({
                "titulo": libro.get("title", "Sin titulo"),
                "autor": libro.get("author_name", ["Desconocido"])[0],
                "año": libro.get("first_publish_year", "N/A")
            })
        return pd.DataFrame(libros)
    return None

# df_libros = buscar_libros("data science")
# print(df_libros)

# ===================== WEB SCRAPING (esquema) =====================

# from bs4 import BeautifulSoup
#
# url = "https://example.com/tabla"
# respuesta = requests.get(url)
# soup = BeautifulSoup(respuesta.text, "html.parser")
#
# # Extraer tabla
# tabla = soup.find("table")
# filas = []
# for tr in tabla.find_all("tr")[1:]:  # saltar encabezado
#     celdas = [td.text.strip() for td in tr.find_all("td")]
#     filas.append(celdas)
#
# df = pd.DataFrame(filas)
# print(df.head())

print("Modulo 5: ejercicios listos para ejecutar con conexion a internet.")
print("Descomentar las llamadas a funcion para probar.")
