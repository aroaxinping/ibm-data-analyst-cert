# Modulo 4: Plotly — Graficos interactivos

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

np.random.seed(42)

# Dataset de ejemplo
n = 200
df = pd.DataFrame({
    "fabricante": np.random.choice(["Toyota", "BMW", "Mercedes", "Ford", "Honda"], n),
    "segmento": np.random.choice(["Compacto", "Medio", "Premium", "SUV"], n),
    "combustible": np.random.choice(["gasolina", "diesel", "electrico"], n, p=[0.5, 0.35, 0.15]),
    "precio": np.random.lognormal(10.5, 0.5, n),
    "caballos": np.random.normal(180, 60, n).clip(70, 450),
    "cilindrada": np.random.normal(2000, 600, n).clip(800, 5000),
    "año": np.random.choice(range(2015, 2025), n)
})

# ===================== PLOTLY EXPRESS =====================

# 1. Scatter interactivo
fig1 = px.scatter(df, x="caballos", y="precio",
                  color="segmento",
                  size="cilindrada",
                  hover_data=["fabricante", "combustible"],
                  title="Precio vs Potencia por segmento",
                  labels={"caballos": "Potencia (CV)", "precio": "Precio (€)"},
                  template="plotly_white")
fig1.write_html("scatter_interactivo.html")
print("scatter_interactivo.html generado")

# 2. Barras agrupadas
df_fab = df.groupby(["fabricante", "combustible"])["precio"].mean().reset_index()
fig2 = px.bar(df_fab, x="fabricante", y="precio",
              color="combustible", barmode="group",
              title="Precio medio por fabricante y combustible",
              template="plotly_white")
fig2.write_html("barras_agrupadas.html")
print("barras_agrupadas.html generado")

# 3. Box plot interactivo
fig3 = px.box(df, x="segmento", y="precio",
              color="combustible",
              title="Distribucion de precios",
              template="plotly_white")
fig3.write_html("boxplot_interactivo.html")
print("boxplot_interactivo.html generado")

# ===================== SUBPLOT CON GRAPH_OBJECTS =====================

fig_dash = make_subplots(
    rows=2, cols=2,
    subplot_titles=[
        "Precio vs Potencia",
        "Precio por segmento",
        "Evolucion por año",
        "Distribucion precio"
    ]
)

# Scatter
fig_dash.add_trace(
    go.Scatter(x=df["caballos"], y=df["precio"],
               mode="markers",
               marker=dict(color="steelblue", opacity=0.5),
               name="Precio vs CV"),
    row=1, col=1
)

# Barras
df_seg = df.groupby("segmento")["precio"].mean().reset_index()
fig_dash.add_trace(
    go.Bar(x=df_seg["segmento"], y=df_seg["precio"],
           marker_color="steelblue", name="Precio medio"),
    row=1, col=2
)

# Lineas temporales
df_año = df.groupby("año")["precio"].mean().reset_index()
fig_dash.add_trace(
    go.Scatter(x=df_año["año"], y=df_año["precio"],
               mode="lines+markers", name="Precio anual",
               line=dict(color="coral", width=2)),
    row=2, col=1
)

# Histograma
fig_dash.add_trace(
    go.Histogram(x=df["precio"], nbinsx=30,
                 marker_color="steelblue", name="Distribucion"),
    row=2, col=2
)

fig_dash.update_layout(
    height=700,
    title="Dashboard de Automoviles — Plotly",
    showlegend=False,
    template="plotly_white"
)

fig_dash.write_html("dashboard.html")
print("dashboard.html generado")
print("\nAbrir los archivos .html en el navegador para ver los graficos interactivos")
