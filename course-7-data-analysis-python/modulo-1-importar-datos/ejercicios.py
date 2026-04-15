# Modulo 1: Importar datasets y primera exploracion

import pandas as pd
import numpy as np

# Dataset de automoviles de IBM (disponible en Watson Studio o GitHub)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

encabezados = [
    "simbolizacion", "perdidas_norm", "fabricante", "combustible",
    "aspiracion", "num_puertas", "tipo_carroceria", "rueda_motriz",
    "ubicacion_motor", "distancia_ejes", "longitud", "anchura", "altura",
    "peso", "tipo_motor", "num_cilindros", "cilindrada", "ratio_compresion",
    "caballos", "rpm_max", "consumo_ciudad", "consumo_autopista", "precio"
]

# Cargar con tratamiento de nulos
df = pd.read_csv(url, names=encabezados, na_values=["?"])

print("Forma del dataset:", df.shape)
print("\nPrimeras filas:")
print(df.head())

print("\nTipos de datos:")
print(df.dtypes)

print("\nValores nulos por columna:")
print(df.isnull().sum())

print("\nEstadisticas basicas:")
print(df.describe())

print("\nEstadisticas incluyendo categoricas:")
print(df.describe(include="all"))
