# Modulo 5: Regresion lineal y evaluacion del modelo

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Dataset de automoviles (ya limpio)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
encabezados = [
    "simbolizacion", "perdidas_norm", "fabricante", "combustible",
    "aspiracion", "num_puertas", "tipo_carroceria", "rueda_motriz",
    "ubicacion_motor", "distancia_ejes", "longitud", "anchura", "altura",
    "peso", "tipo_motor", "num_cilindros", "cilindrada", "ratio_compresion",
    "caballos", "rpm_max", "consumo_ciudad", "consumo_autopista", "precio"
]

df = pd.read_csv(url, names=encabezados, na_values=["?"])
df = df[["caballos", "cilindrada", "peso", "longitud", "precio"]].dropna()
df = df.apply(pd.to_numeric, errors="coerce").dropna()

X = df[["caballos", "cilindrada", "peso", "longitud"]]
y = df["precio"]

# ===================== TRAIN/TEST SPLIT =====================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"Train: {X_train.shape[0]} filas | Test: {X_test.shape[0]} filas")

# ===================== REGRESION LINEAL MULTIPLE =====================
rl = LinearRegression()
rl.fit(X_train, y_train)
y_pred_rl = rl.predict(X_test)

print("\n--- Regresion Lineal Multiple ---")
print(f"R²: {r2_score(y_test, y_pred_rl):.4f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred_rl)):.2f}")
print(f"MAE: {mean_absolute_error(y_test, y_pred_rl):.2f}")

# ===================== REGRESION POLINOMICA =====================
pipeline_poly = Pipeline([
    ("poly", PolynomialFeatures(degree=2)),
    ("scaler", StandardScaler()),
    ("modelo", LinearRegression())
])

X_simple = df[["cilindrada"]]
y_simple = df["precio"]
X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
    X_simple, y_simple, test_size=0.2, random_state=42
)

pipeline_poly.fit(X_train_s, y_train_s)
y_pred_poly = pipeline_poly.predict(X_test_s)

print("\n--- Regresion Polinomica (grado 2) ---")
print(f"R²: {r2_score(y_test_s, y_pred_poly):.4f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test_s, y_pred_poly)):.2f}")

# ===================== CROSS-VALIDATION =====================
cv_scores = cross_val_score(rl, X, y, cv=5, scoring="r2")
print("\n--- Cross-Validation (5-fold) ---")
print(f"R² por pliegue: {cv_scores.round(4)}")
print(f"R² medio: {cv_scores.mean():.4f}")
print(f"Desviacion tipica: {cv_scores.std():.4f}")

# ===================== RIDGE REGRESSION =====================
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)
y_pred_ridge = ridge.predict(X_test)

print("\n--- Ridge Regression (alpha=1.0) ---")
print(f"R²: {r2_score(y_test, y_pred_ridge):.4f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred_ridge)):.2f}")
