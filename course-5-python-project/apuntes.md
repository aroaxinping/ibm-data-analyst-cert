# Apuntes — Course 5: Python Project for Data Science

**Duracion:** 8 horas
**Modulos:** 1 (proyecto unico)

---

## Que cubre este curso

Proyecto practico aplicado. El objetivo es simular el trabajo de un "Data
Scientist" extrayendo datos financieros reales, limpiandolos y creando
visualizaciones para comparar el precio de las acciones con los beneficios
reportados de dos empresas: Tesla (TSLA) y GameStop (GME).

---

## Herramientas del proyecto

**yfinance:** libreria de Python para descargar datos historicos de acciones
de Yahoo Finance.

```python
pip install yfinance
```

**BeautifulSoup:** para extraer datos de beneficios (revenue) de Macrotrends
cuando no estan disponibles via API.

**pandas + plotly:** para limpiar y visualizar.

---

## El proyecto paso a paso

### 1. Descargar datos de acciones con yfinance

```python
import yfinance as yf

tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)

print(tesla_data.head())
```

El DataFrame tiene columnas: `Date`, `Open`, `High`, `Low`, `Close`, `Volume`.

```python
gamestop = yf.Ticker("GME")
gme_data = gamestop.history(period="max")
gme_data.reset_index(inplace=True)
```

### 2. Extraer datos de revenue con web scraping

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
headers = {"User-Agent": "Mozilla/5.0"}
respuesta = requests.get(url, headers=headers)
soup = BeautifulSoup(respuesta.text, "html.parser")

# Localizar la tabla de revenue anual
tablas = soup.find_all("table")
# Iterar hasta encontrar la correcta por su contenido
for tabla in tablas:
    if "Tesla Annual Revenue" in str(tabla):
        df_revenue = pd.read_html(str(tabla))[0]
        break
```

### 3. Limpiar los datos de revenue

```python
# La columna Revenue suele venir como "$21,461M" — hay que limpiarla
df_revenue.columns = ["Date", "Revenue"]
df_revenue["Revenue"] = (
    df_revenue["Revenue"]
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.replace("M", "", regex=False)
)
df_revenue.dropna(inplace=True)
df_revenue = df_revenue[df_revenue["Revenue"] != ""]
df_revenue["Revenue"] = df_revenue["Revenue"].astype(float)
```

### 4. Crear el dashboard de visualizacion

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def crear_dashboard(datos_acciones, datos_revenue, ticker):
    fig = make_subplots(
        rows=2, cols=1,
        shared_xaxes=True,
        subplot_titles=[f"{ticker} — Precio de cierre", f"{ticker} — Revenue (millones $)"]
    )

    fig.add_trace(
        go.Scatter(x=datos_acciones["Date"], y=datos_acciones["Close"], name="Precio"),
        row=1, col=1
    )

    fig.add_trace(
        go.Bar(x=datos_revenue["Date"], y=datos_revenue["Revenue"], name="Revenue"),
        row=2, col=1
    )

    fig.update_layout(height=800, title=f"Analisis financiero: {ticker}")
    fig.show()

crear_dashboard(tesla_data, tesla_revenue, "TSLA")
crear_dashboard(gme_data, gme_revenue, "GME")
```

---

## Hallazgos del proyecto

**Tesla (TSLA):**
- Revenue creciendo de forma consistente desde 2012
- El precio de la accion tuvo una explosion en 2020-2021 que supero con
  creces el crecimiento del revenue — señal de sobrevaloración especulativa
- Desde 2022 el precio se ajusto a la baja pero el revenue siguio subiendo

**GameStop (GME):**
- Revenue en declive desde 2016 (transicion del sector a digital)
- El short squeeze de enero 2021 disparo el precio de la accion hasta valores
  completamente desconectados del revenue real
- Caso de estudio clasico de como las redes sociales pueden desconectar el
  precio de una accion de sus fundamentales

---

## Lo que se aprende con este proyecto

- **yfinance** como fuente de datos financieros gratuita
- Web scraping real con `requests` + `BeautifulSoup` sobre una web con
  estructura compleja
- Limpieza de strings con `.str.replace()` y expresiones regulares
- Visualizacion con **plotly** y subplots (dos graficos en un mismo panel)
- Interpretacion de datos: precio vs fundamentales

---

## Conexion con otros cursos

- Las tecnicas de limpieza de strings usadas aqui (`.str.replace()`,
  `.astype()`) son pandas del curso 4 aplicadas en un caso real.
- plotly se usa de nuevo en el curso 8 (Data Visualization with Python)
  con mas profundidad: mapas, scatter 3D, animaciones.
- La idea de comparar precio de acciones con metricas de negocio es un
  caso de analisis financiero que podria convertirse en un proyecto
  del capstone (curso 9).
