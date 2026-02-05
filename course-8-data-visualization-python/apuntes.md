# Apuntes — Course 8: Data Visualization with Python

**Duracion:** 20 horas
**Modulos:** 5

---

## Que cubre este curso

Visualizacion de datos en Python con cuatro librerias complementarias:
matplotlib para control total, seaborn para graficos estadisticos rapidos,
Folium para mapas geograficos y Plotly/Dash para interactividad y dashboards.

---

## Modulo 1: Introduction to Visualization Tools — Matplotlib

**Estructura basica de un grafico matplotlib:**

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(x, y, color="steelblue", linewidth=2, label="Serie A")
ax.set_title("Titulo del grafico", fontsize=14)
ax.set_xlabel("Eje X (unidades)")
ax.set_ylabel("Eje Y (unidades)")
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("grafico.png", dpi=150, bbox_inches="tight")
plt.show()
```

**Tipos de grafico en matplotlib:**

```python
# Lineas — series temporales
ax.plot(años, ventas)
ax.plot(años, costes, linestyle="--", color="red")

# Barras verticales
ax.bar(categorias, valores, color="steelblue", edgecolor="white")

# Barras horizontales
ax.barh(categorias, valores)

# Barras agrupadas
x = np.arange(len(categorias))
width = 0.35
ax.bar(x - width/2, valores_a, width, label="Serie A")
ax.bar(x + width/2, valores_b, width, label="Serie B")
ax.set_xticks(x)
ax.set_xticklabels(categorias)

# Barras apiladas
ax.bar(categorias, valores_a, label="A")
ax.bar(categorias, valores_b, bottom=valores_a, label="B")

# Scatter (dispersion)
ax.scatter(x, y, c=colores, s=tamaños, alpha=0.6)

# Histograma
ax.hist(datos, bins=20, edgecolor="white", color="steelblue")

# Boxplot
ax.boxplot([datos_a, datos_b, datos_c], labels=["A", "B", "C"])

# Circular (pie)
ax.pie(valores, labels=etiquetas, autopct="%1.1f%%", startangle=90)
```

**Multiples subplots:**

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].plot(x, y1)
axes[0, 0].set_title("Grafico 1")

axes[0, 1].bar(cats, vals)
axes[0, 1].set_title("Grafico 2")

axes[1, 0].scatter(x, y2)
axes[1, 1].hist(datos, bins=15)

plt.tight_layout()
```

---

## Modulo 2: Basic and Specialized Visualization Tools — Seaborn

Seaborn esta construida sobre matplotlib pero con una interfaz de alto
nivel pensada para estadistica. Graficos mas bonitos con menos codigo.

```python
import seaborn as sns

sns.set_theme(style="whitegrid")  # tema global
```

**Graficos de distribucion:**

```python
# Histograma + KDE (densidad)
sns.histplot(df["precio"], bins=30, kde=True)

# KDE solo
sns.kdeplot(df["precio"], fill=True)

# Boxplot comparativo
sns.boxplot(data=df, x="fabricante", y="precio")

# Violin (distribucion + boxplot)
sns.violinplot(data=df, x="tipo_carroceria", y="precio")
```

**Graficos de relacion:**

```python
# Scatter con color por categoria
sns.scatterplot(data=df, x="cilindrada", y="precio", hue="combustible")

# Regresion lineal visualizada
sns.regplot(data=df, x="caballos", y="precio", scatter_kws={"alpha": 0.4})

# Relplot (scatter con subplots por categorias)
sns.relplot(data=df, x="cilindrada", y="precio",
            hue="combustible", col="tipo_carroceria", kind="scatter")
```

**Graficos de categoria:**

```python
# Barras con intervalos de confianza automaticos
sns.barplot(data=df, x="fabricante", y="precio", ci=95)

# Countplot — conteo de categorias
sns.countplot(data=df, x="tipo_carroceria", order=df["tipo_carroceria"].value_counts().index)

# Swarmplot — distribucion de puntos
sns.swarmplot(data=df, x="combustible", y="precio")
```

**Heatmap de correlacion:**

```python
correlaciones = df.corr(numeric_only=True)
sns.heatmap(correlaciones,
            annot=True,
            fmt=".2f",
            cmap="coolwarm",
            center=0,
            square=True,
            linewidths=0.5)
plt.title("Matriz de correlacion")
```

**Pairplot:**

```python
# Scatter de todas las variables numericas entre si
sns.pairplot(df[["precio", "caballos", "cilindrada", "peso"]],
             hue="combustible",
             diag_kind="kde")
```

---

## Modulo 3: Advanced Visualizations and Geospatial Data — Folium

Folium genera mapas interactivos basados en Leaflet.js.

```python
pip install folium
```

**Mapa basico:**

```python
import folium

# Crear mapa centrado en Barcelona
mapa = folium.Map(location=[41.3851, 2.1734], zoom_start=12)

# Guardar como HTML
mapa.save("mapa.html")
```

**Añadir marcadores:**

```python
# Marcador simple
folium.Marker(
    location=[41.3851, 2.1734],
    popup="Barcelona",
    tooltip="Haz clic",
    icon=folium.Icon(color="blue", icon="info-sign")
).add_to(mapa)

# Circulo
folium.Circle(
    location=[41.3851, 2.1734],
    radius=500,  # metros
    color="crimson",
    fill=True,
    fill_opacity=0.3
).add_to(mapa)
```

**Choropleth map (mapa de calor geografico):**

```python
folium.Choropleth(
    geo_data=geojson_paises,       # GeoJSON con los limites geograficos
    data=df,
    columns=["pais", "valor"],     # [columna ID geografico, columna metrica]
    key_on="feature.properties.name",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    legend_name="Valor por pais"
).add_to(mapa)
```

**Cluster de marcadores:**

```python
from folium.plugins import MarkerCluster

cluster = MarkerCluster().add_to(mapa)

for _, fila in df.iterrows():
    folium.Marker(
        location=[fila["lat"], fila["lon"]],
        popup=fila["nombre"]
    ).add_to(cluster)
```

---

## Modulo 4: Creating Dashboards with Plotly and Dash

**Plotly — graficos interactivos:**

```python
import plotly.express as px
import plotly.graph_objects as go

# Scatter interactivo
fig = px.scatter(df, x="cilindrada", y="precio",
                 color="combustible",
                 size="caballos",
                 hover_data=["fabricante"],
                 title="Precio vs Cilindrada")
fig.show()

# Barras
fig = px.bar(df.groupby("fabricante")["precio"].mean().reset_index(),
             x="fabricante", y="precio",
             title="Precio medio por fabricante",
             color="precio",
             color_continuous_scale="Blues")
fig.show()

# Lineas temporales
fig = px.line(df_temporal, x="fecha", y="valor",
              color="categoria",
              title="Evolucion temporal")
fig.show()

# Sunburst (jerarquico)
fig = px.sunburst(df, path=["region", "pais", "ciudad"],
                  values="poblacion")
fig.show()

# Mapa de coropletas
fig = px.choropleth(df, locations="pais",
                    color="gdp_per_capita",
                    hover_name="pais",
                    color_continuous_scale=px.colors.sequential.Plasma)
fig.show()
```

**Subplots con plotly:**

```python
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=2, cols=2,
                    subplot_titles=["Scatter", "Barras", "Lineas", "Histograma"])

fig.add_trace(go.Scatter(x=x, y=y, mode="markers"), row=1, col=1)
fig.add_trace(go.Bar(x=cats, y=vals), row=1, col=2)
fig.add_trace(go.Scatter(x=fechas, y=serie, mode="lines"), row=2, col=1)
fig.add_trace(go.Histogram(x=datos), row=2, col=2)

fig.update_layout(height=700, title="Dashboard")
fig.show()
```

**Dash — aplicacion web interactiva:**

```python
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard de Automoviles"),

    html.Label("Seleccionar tipo de carroceria:"),
    dcc.Dropdown(
        id="dropdown-carroceria",
        options=[{"label": c, "value": c} for c in df["tipo_carroceria"].unique()],
        value=df["tipo_carroceria"].unique()[0]
    ),

    dcc.Graph(id="scatter-plot")
])

@app.callback(
    Output("scatter-plot", "figure"),
    Input("dropdown-carroceria", "value")
)
def actualizar_grafico(carroceria):
    df_filtrado = df[df["tipo_carroceria"] == carroceria]
    fig = px.scatter(df_filtrado, x="caballos", y="precio",
                     color="combustible",
                     title=f"Precio vs Caballos — {carroceria}")
    return fig

if __name__ == "__main__":
    app.run(debug=True)
```

---

## Esquema resumido del curso

```
COURSE 8: DATA VISUALIZATION WITH PYTHON
|
+-- Matplotlib
|     Lineas, barras, scatter, histograma, boxplot, subplots
|     Control total del estilo
|
+-- Seaborn
|     Histplot, kdeplot, boxplot, violin
|     Scatterplot, regplot, barplot, heatmap, pairplot
|
+-- Folium
|     Mapas interactivos, marcadores, choropleth, clusters
|
+-- Plotly + Dash
      Graficos interactivos (px.scatter, px.bar, px.line...)
      Subplots con make_subplots
      Dashboard con callbacks (Input -> Output)
```

---

## Elegir la libreria correcta

| Necesidad | Libreria |
|-----------|----------|
| Grafico estatico para informe o paper | matplotlib / seaborn |
| Grafico estadistico rapido (distribucion, correlacion) | seaborn |
| Mapa geografico | Folium |
| Grafico interactivo (web, notebook) | Plotly Express |
| Dashboard con filtros y dinamismo | Dash |
| Control fino del aspecto visual | matplotlib (con seaborn encima) |

---

## Glosario

| Termino | Definicion |
|---------|------------|
| Figure | Contenedor principal de matplotlib que puede contener uno o mas Axes |
| Axes | Un subplot individual dentro de una Figure — es donde se dibujan los datos |
| KDE | Kernel Density Estimation — estimacion suavizada de la funcion de densidad de probabilidad |
| Choropleth | Mapa en el que las areas geograficas se colorean segun una metrica |
| Dash | Framework de Python para crear aplicaciones web de visualizacion interactiva |
| Callback | Funcion que se ejecuta automaticamente cuando cambia un Input en Dash |
| Hover | Informacion que aparece al pasar el cursor sobre un elemento del grafico |
| Leaflet | Libreria JavaScript de mapas interactivos que Folium usa internamente |

---

## Errores comunes

- **Mezclar plt.plot() y ax.plot():** las dos interfaces de matplotlib son
  validas pero no deben mezclarse en el mismo grafico. Preferir siempre la
  orientada a objetos (fig, ax) para mayor control.
- **No llamar a plt.tight_layout():** sin esta llamada, los titulos y etiquetas
  de subplots se superponen.
- **Usar seaborn sin especificar el DataFrame:** seaborn acepta tanto arrays
  como DataFrames. Usar siempre `data=df, x="columna"` en vez de `x=df["columna"]`
  para que la leyenda y los ejes se generen correctamente.
- **Dashboard de Dash sin callback:** un dropdown sin callback no hace nada.
  Todo elemento interactivo necesita al menos un callback.

---

## Conexion con otros cursos

- Los graficos de EDA (heatmap de correlacion, scatter por categoria) que
  se crean aqui son los que se deberian haber hecho en el modulo 3 del
  curso 7 — ahora se tienen las herramientas para hacerlos bien.
- El dashboard de Dash tiene la misma logica que el dashboard de Cognos
  del curso 3: KPIs, filtros, graficos conectados. La diferencia es que
  Dash es codigo Python y Cognos es una interfaz grafica.
- Los mapas de Folium son utiles para el capstone si el proyecto tiene
  datos geograficos (ventas por region, crimenes por barrio, etc.).
