# Apuntes — Course 7: Data Analysis with Python

**Duracion:** 15 horas
**Modulos:** 6

---

## Que cubre este curso

El curso mas tecnico del certificado hasta ahora. Cubre el flujo completo de
analisis de datos en Python: importar datos, explorar, limpiar, analizar
estadisticamente, calcular correlaciones y construir modelos de regresion
basicos. El dataset es de precios de automoviles de IBM Watson Studio.

---

## Modulo 1: Importing Datasets

**Cargar datos de distintas fuentes:**

```python
import pandas as pd
import numpy as np

# CSV
df = pd.read_csv("automoviles.csv")

# CSV sin encabezados — asignar nombres de columna
encabezados = ["simbolizacion", "perdidas", "fabricante", "combustible",
               "aspiracion", "puertas", "tipo_carroceria", "rueda_motriz",
               "ubicacion_motor", "distancia_ejes", "longitud", "anchura",
               "altura", "peso", "tipo_motor", "cilindros", "cilindrada",
               "ratio_compresion", "caballos", "rpm_max", "consumo_ciudad",
               "consumo_autopista", "precio"]
df = pd.read_csv("automoviles.csv", names=encabezados)

# Excel
df = pd.read_excel("datos.xlsx", sheet_name="Hoja1")

# JSON
df = pd.read_json("datos.json")

# Desde URL
url = "https://example.com/datos.csv"
df = pd.read_csv(url)
```

**Primera exploracion:**

```python
df.head()             # primeras 5 filas
df.tail()             # ultimas 5 filas
df.shape              # (filas, columnas)
df.dtypes             # tipo de cada columna
df.info()             # tipos + valores no nulos
df.describe()         # estadisticas de columnas numericas
df.describe(include="all")  # incluye categoricas
df.columns.tolist()   # lista de nombres de columna
df.index              # informacion del indice
```

**Valores que representan nulos:**

```python
# Reemplazar "?" por NaN al cargar
df = pd.read_csv("datos.csv", na_values=["?", "N/A", "-"])

# O despues de cargar
df.replace("?", np.nan, inplace=True)
```

---

## Modulo 2: Data Wrangling

**Detectar valores faltantes:**

```python
df.isnull()                    # DataFrame de True/False
df.isnull().sum()              # conteo por columna
df.isnull().sum() / len(df)    # porcentaje de nulos por columna
df[df["precio"].isnull()]      # filas donde precio es nulo
```

**Estrategias para valores faltantes:**

```python
# 1. Eliminar filas con nulos
df.dropna(inplace=True)

# 2. Eliminar filas donde una columna especifica es nula
df.dropna(subset=["precio"], inplace=True)

# 3. Rellenar con la media (numericas)
media = df["cilindrada"].mean()
df["cilindrada"].fillna(media, inplace=True)

# 4. Rellenar con la moda (categoricas)
moda = df["num_puertas"].value_counts().idxmax()
df["num_puertas"].fillna(moda, inplace=True)

# 5. Rellenar con un valor especifico
df["perdidas"].fillna(0, inplace=True)
```

**Corregir tipos de datos:**

```python
df.dtypes

# Convertir tipos
df["precio"] = df["precio"].astype(float)
df["cilindros"] = df["cilindros"].astype(int)

# Convertir strings de numero a numerico (tolerante a errores)
df["precio"] = pd.to_numeric(df["precio"], errors="coerce")
# errors="coerce" convierte los que no puede a NaN

# Convertir fechas
df["fecha"] = pd.to_datetime(df["fecha"])
```

**Estandarizacion de datos:**

```python
# Convertir de mpg a L/100km
df["consumo_ciudad_l100"] = 235.214583 / df["consumo_ciudad"]

# Renombrar columna
df.rename(columns={"consumo_ciudad": "mpg_ciudad"}, inplace=True)

# Normalizar strings
df["fabricante"] = df["fabricante"].str.lower().str.strip()
```

**Normalizacion (feature scaling):**

```python
# Normalizacion min-max: escala a [0, 1]
df["longitud_norm"] = (df["longitud"] - df["longitud"].min()) / \
                      (df["longitud"].max() - df["longitud"].min())

# Estandarizacion Z-score: media 0, desviacion tipica 1
df["longitud_z"] = (df["longitud"] - df["longitud"].mean()) / df["longitud"].std()
```

**Binning (discretizacion):**

```python
# Dividir una variable continua en categorias
bins = np.linspace(df["caballos"].min(), df["caballos"].max(), 4)
etiquetas = ["bajo", "medio", "alto"]
df["categoria_cv"] = pd.cut(df["caballos"], bins=bins, labels=etiquetas)
```

**Variables dummy (One-Hot Encoding):**

```python
# Convertir variable categorica en columnas binarias
dummy_combustible = pd.get_dummies(df["combustible"])
df = pd.concat([df, dummy_combustible], axis=1)
df.drop("combustible", axis=1, inplace=True)

# Forma abreviada con pandas
df = pd.get_dummies(df, columns=["combustible", "tipo_carroceria"])
```

---

## Modulo 3: Exploratory Data Analysis (EDA)

**Estadisticas descriptivas:**

```python
df["precio"].describe()

# Estadisticas individuales
df["precio"].mean()
df["precio"].median()
df["precio"].std()
df["precio"].var()
df["precio"].min()
df["precio"].max()
df["precio"].quantile(0.75)  # percentil 75

# Conteo de valores (categoricas)
df["combustible"].value_counts()
df["combustible"].value_counts(normalize=True)  # proporciones
```

**Analisis de correlacion:**

```python
# Correlacion de Pearson entre dos variables
df[["caballos", "precio"]].corr()

# Matriz de correlacion de todas las variables numericas
df.corr(numeric_only=True)

# Correlacion de una variable con todas las demas (ordenada)
df.corr()["precio"].sort_values(ascending=False)
```

**Tablas de contingencia (variables categoricas):**

```python
tabla = pd.crosstab(df["combustible"], df["tipo_carroceria"])
print(tabla)
```

**GroupBy para analisis por segmentos:**

```python
# Precio medio por tipo de carroceria
df.groupby("tipo_carroceria")["precio"].mean().sort_values(ascending=False)

# Varias metricas
df.groupby("fabricante").agg(
    precio_medio=("precio", "mean"),
    precio_max=("precio", "max"),
    num_modelos=("precio", "count")
).sort_values("precio_medio", ascending=False)

# Pivot table
pd.pivot_table(df, values="precio",
               index="tipo_carroceria",
               columns="combustible",
               aggfunc="mean")
```

---

## Modulo 4: Model Development

**Regresion lineal simple:**

```python
from sklearn.linear_model import LinearRegression

X = df[["cilindrada"]]   # variable independiente (matriz, doble corchete)
y = df["precio"]          # variable dependiente (serie)

modelo = LinearRegression()
modelo.fit(X, y)

print("Intercepto:", modelo.intercept_)
print("Coeficiente:", modelo.coef_)

# Prediccion
precio_predicho = modelo.predict([[2000]])
print(f"Precio predicho para 2000cc: {precio_predicho[0]:.2f}")
```

**Regresion lineal multiple:**

```python
X = df[["caballos", "cilindrada", "peso", "longitud"]]
y = df["precio"]

modelo_multi = LinearRegression()
modelo_multi.fit(X, y)

print("Coeficientes:", modelo_multi.coef_)
# Cada coeficiente: cuanto cambia y por cada unidad de la variable,
# manteniendo las demas constantes
```

**Regresion polinomica:**

```python
from sklearn.preprocessing import PolynomialFeatures

pf = PolynomialFeatures(degree=2)
X_poly = pf.fit_transform(df[["cilindrada"]])

modelo_poly = LinearRegression()
modelo_poly.fit(X_poly, y)
```

**Pipelines:**

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("modelo", LinearRegression())
])

pipeline.fit(X_train, y_train)
predicciones = pipeline.predict(X_test)
```

---

## Modulo 5: Model Evaluation and Refinement

**Metricas de evaluacion para regresion:**

```python
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

y_pred = modelo.predict(X)

# R² (coeficiente de determinacion): 1 es perfecto, 0 es aleatorio
r2 = r2_score(y, y_pred)
print(f"R²: {r2:.4f}")

# MSE (Mean Squared Error): error cuadratico medio
mse = mean_squared_error(y, y_pred)
print(f"MSE: {mse:.2f}")

# RMSE (raiz del MSE — en las mismas unidades que y)
rmse = np.sqrt(mse)
print(f"RMSE: {rmse:.2f}")

# MAE (Mean Absolute Error): mas interpretable que MSE
mae = mean_absolute_error(y, y_pred)
print(f"MAE: {mae:.2f}")
```

**Separar datos en train y test:**

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# 80% train, 20% test, semilla fija para reproducibilidad

modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
print(f"R² en test: {r2_score(y_test, y_pred):.4f}")
```

**Cross-validation:**

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(modelo, X, y, cv=5, scoring="r2")
print(f"R² medio: {scores.mean():.4f}")
print(f"Desviacion tipica: {scores.std():.4f}")
# Si la desviacion es alta, el modelo es inestable
```

**Overfitting vs Underfitting:**

- **Underfitting:** R² bajo tanto en train como en test. El modelo es
  demasiado simple para capturar el patron.
- **Overfitting:** R² alto en train, bajo en test. El modelo memoriza
  los datos de entrenamiento pero no generaliza.
- **Objetivo:** R² similar en train y test, ambos razonablemente altos.

**Ridge Regression (regularizacion):**

```python
from sklearn.linear_model import Ridge

ridge = Ridge(alpha=1.0)  # alpha controla la penalizacion
ridge.fit(X_train, y_train)
# Ridge reduce el overfitting penalizando coeficientes grandes
```

---

## Esquema resumido del curso

```
COURSE 7: DATA ANALYSIS WITH PYTHON
|
+-- Importar datos
|     CSV, Excel, JSON, URL — manejo de nulos al cargar
|
+-- Wrangling
|     Nulos: eliminar, imputar con media/moda
|     Tipos: astype, to_numeric, to_datetime
|     Normalizacion: min-max, Z-score
|     Binning, One-Hot Encoding
|
+-- EDA
|     Estadisticas descriptivas, correlaciones
|     GroupBy, pivot_table, crosstab
|
+-- Modelos de regresion
|     Lineal simple y multiple, polinomica
|     Pipelines con preprocesamiento
|
+-- Evaluacion
      R², MSE, RMSE, MAE
      Train/test split, cross-validation
      Overfitting vs underfitting, Ridge
```

---

## Glosario

| Termino | Definicion |
|---------|------------|
| EDA | Exploratory Data Analysis — analisis inicial de un dataset para entender su estructura y distribuciones |
| Imputacion | Reemplazar valores faltantes con un valor estimado (media, moda, etc.) |
| One-Hot Encoding | Convertir una variable categorica en N columnas binarias |
| Normalizacion | Escalar valores a un rango estandar (tipicamente 0-1) |
| Estandarizacion | Transformar valores para que tengan media 0 y desviacion tipica 1 |
| Regresion lineal | Modelo que predice una variable continua como combinacion lineal de otras variables |
| R² | Proporcion de la varianza de y explicada por el modelo (1 = perfecto, 0 = aleatorio) |
| RMSE | Root Mean Squared Error — raiz del error cuadratico medio, en las mismas unidades que y |
| Overfitting | Modelo que funciona bien en train pero mal en datos nuevos — memoriza en vez de generalizar |
| Underfitting | Modelo demasiado simple que no captura el patron en los datos |
| Cross-validation | Tecnica de evaluacion que divide los datos en K pliegues y entrena/evalua K veces |
| Ridge | Regresion lineal con regularizacion L2 — penaliza coeficientes grandes para reducir overfitting |

---

## Errores comunes

- **Hacer EDA despues de la limpieza:** el EDA debe hacerse antes de limpiar,
  para entender que tipo de problemas tiene el dataset y tomar decisiones
  informadas sobre como tratarlos.
- **Imputar con la media en variables sesgadas:** si la distribucion es muy
  asimetrica, la media no representa bien el centro. Mejor usar la mediana.
- **No separar train/test antes de normalizar:** si se normaliza sobre todo el
  dataset (incluido test), se esta filtrando informacion del test al modelo.
  Normalizar solo sobre train, luego aplicar la misma transformacion a test.
- **Interpretar R² alto como "buen modelo":** R² alto en train puede ser
  overfitting. Siempre evaluar en test o con cross-validation.

---

## Conexion con otros cursos

- El wrangling de este curso (nulos, tipos, encoding) es la aplicacion
  practica de lo aprendido en pandas en el curso 4.
- Los modelos de regresion introducidos aqui son la puerta de entrada al
  ML — no es el objetivo del certificado, pero establece las bases.
- Las visualizaciones de EDA (histogramas, scatter plots, heatmaps de
  correlacion) se profundizan en el curso 8 con matplotlib, seaborn y plotly.
- El dataset de automoviles del proyecto final es el mismo que se uso en
  el curso 3 (visualizacion en Cognos).
