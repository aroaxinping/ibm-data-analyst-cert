# Modulo 3: EDA — Analisis exploratorio del dataset de la survey

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar dataset (generado en modulo 1)
try:
    df = pd.read_csv("../modulo-1-recopilacion-datos/survey_data.csv")
except FileNotFoundError:
    print("Ejecutar primero modulo-1/recopilacion.py para generar survey_data.csv")
    exit()

sns.set_theme(style="whitegrid")
print(f"Dataset cargado: {df.shape}")

# ===================== DISTRIBUCION DE VARIABLES =====================

# Compensacion
print("\n--- Compensacion total ---")
print(df["CompTotal"].describe())
print(f"Mediana: {df['CompTotal'].median():.0f}")
print(f"Outliers (>3 IQR): {((df['CompTotal'] - df['CompTotal'].median()).abs() > 3*df['CompTotal'].std()).sum()}")

# ===================== TOP LENGUAJES =====================

def top_valores_multiples(df, columna, n=10):
    """Expande columnas con valores separados por ; y devuelve el top n."""
    return (
        df[columna]
        .dropna()
        .str.split(";")
        .explode()
        .str.strip()
        .value_counts()
        .head(n)
        .reset_index()
        .rename(columns={"index": "valor", columna: "conteo"})
    )

top_usados = top_valores_multiples(df, "LanguageHaveWorkedWith")
top_deseados = top_valores_multiples(df, "LanguageWantToWorkWith")

print("\n--- Top 10 lenguajes mas usados ---")
print(top_usados.to_string(index=False))

print("\n--- Top 10 lenguajes mas deseados ---")
print(top_deseados.to_string(index=False))

# ===================== VISUALIZACIONES =====================

fig, axes = plt.subplots(1, 2, figsize=(14, 7))

sns.barplot(data=top_usados, x="conteo", y="valor",
            palette="Blues_r", ax=axes[0])
axes[0].set_title("Top 10 lenguajes MAS USADOS", fontsize=13)
axes[0].set_xlabel("Numero de desarrolladores")
axes[0].set_ylabel("")

sns.barplot(data=top_deseados, x="conteo", y="valor",
            palette="Greens_r", ax=axes[1])
axes[1].set_title("Top 10 lenguajes MAS DESEADOS", fontsize=13)
axes[1].set_xlabel("Numero de desarrolladores")
axes[1].set_ylabel("")

plt.suptitle("Stack Overflow Developer Survey — Lenguajes de programacion",
             fontsize=15, y=1.02)
plt.tight_layout()
plt.savefig("lenguajes.png", dpi=150, bbox_inches="tight")
plt.show()

# ===================== DEMOGRAFIA =====================

print("\n--- Distribucion por pais (top 10) ---")
print(df["Country"].value_counts().head(10))

print("\n--- Distribucion por nivel educativo ---")
print(df["EdLevel"].value_counts())
