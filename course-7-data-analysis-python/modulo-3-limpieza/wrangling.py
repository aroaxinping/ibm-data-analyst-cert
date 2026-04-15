# Modulo 3: Data Wrangling — Limpieza completa del dataset de automoviles

import pandas as pd
import numpy as np

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

encabezados = [
    "simbolizacion", "perdidas_norm", "fabricante", "combustible",
    "aspiracion", "num_puertas", "tipo_carroceria", "rueda_motriz",
    "ubicacion_motor", "distancia_ejes", "longitud", "anchura", "altura",
    "peso", "tipo_motor", "num_cilindros", "cilindrada", "ratio_compresion",
    "caballos", "rpm_max", "consumo_ciudad", "consumo_autopista", "precio"
]

df = pd.read_csv(url, names=encabezados, na_values=["?"])

# ===================== TRATAR NULOS =====================

print("Nulos antes de limpieza:")
print(df.isnull().sum()[df.isnull().sum() > 0])

# Numericas: rellenar con la media
for col in ["cilindrada", "caballos", "rpm_max", "consumo_ciudad",
            "consumo_autopista", "precio", "perdidas_norm"]:
    media = df[col].mean()
    df[col].fillna(media, inplace=True)

# Categoricas: rellenar con la moda
df["num_puertas"].fillna(df["num_puertas"].value_counts().idxmax(), inplace=True)
df["num_cilindros"].fillna(df["num_cilindros"].value_counts().idxmax(), inplace=True)

print("\nNulos despues de limpieza:")
print(df.isnull().sum()[df.isnull().sum() > 0])

# ===================== CORREGIR TIPOS =====================

# Estas columnas deberian ser numericas
for col in ["caballos", "rpm_max", "precio", "cilindrada"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("\nTipos despues de correccion:")
print(df[["caballos", "rpm_max", "precio", "cilindrada"]].dtypes)

# ===================== ESTANDARIZAR =====================

# Convertir consumo de MPG a L/100km
df["consumo_ciudad_l100"] = 235.214583 / df["consumo_ciudad"]
df["consumo_autopista_l100"] = 235.214583 / df["consumo_autopista"]

# Normalizar longitud a [0, 1]
df["longitud_norm"] = (df["longitud"] - df["longitud"].min()) / \
                      (df["longitud"].max() - df["longitud"].min())

# ===================== BINNING =====================

import numpy as np
bins = np.linspace(df["caballos"].min(), df["caballos"].max(), 4)
etiquetas = ["bajo", "medio", "alto"]
df["potencia_categoria"] = pd.cut(df["caballos"], bins=bins, labels=etiquetas)

print("\nDistribucion por categoria de potencia:")
print(df["potencia_categoria"].value_counts())

# ===================== ONE-HOT ENCODING =====================

dummy_combustible = pd.get_dummies(df["combustible"], prefix="comb")
df = pd.concat([df, dummy_combustible], axis=1)
df.drop("combustible", axis=1, inplace=True)

print("\nColumnas despues de encoding:")
print([c for c in df.columns if c.startswith("comb")])

print("\nDataset limpio — forma final:", df.shape)
