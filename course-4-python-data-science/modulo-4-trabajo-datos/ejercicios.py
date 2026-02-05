# Modulo 4: Working with Data in Python — Ejercicios

import numpy as np
import pandas as pd

# ===================== NUMPY =====================

# Crear arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.arange(0, 10, 2)          # [0, 2, 4, 6, 8]
arr3 = np.linspace(0, 1, 5)         # [0, 0.25, 0.5, 0.75, 1.0]
matriz = np.zeros((3, 4))

print("arr1:", arr1)
print("arr2:", arr2)
print("Forma de la matriz:", matriz.shape)

# Operaciones vectorizadas
print("arr1 * 2:", arr1 * 2)
print("arr1 ** 2:", arr1 ** 2)
print("arr1 + arr2:", arr1 + arr2)

# Estadisticas
print("Media:", np.mean(arr1))
print("Mediana:", np.median(arr1))
print("Desv. tipica:", np.std(arr1))

# Boolean indexing
print("Mayores que 3:", arr1[arr1 > 3])

# ===================== PANDAS =====================

# Crear DataFrame de ejemplo
datos = {
    "producto": ["Laptop", "Raton", "Teclado", "Monitor", "Webcam"],
    "categoria": ["Ordenador", "Periferico", "Periferico", "Ordenador", "Periferico"],
    "precio": [899.99, 29.99, 59.99, 349.99, 79.99],
    "stock": [15, 200, 150, 30, None]
}

df = pd.DataFrame(datos)

# Explorar
print("\n--- Info ---")
print(df.info())
print("\n--- Describe ---")
print(df.describe())
print("\n--- Head ---")
print(df.head())

# Seleccion
print("\n--- Solo precios ---")
print(df["precio"])

print("\n--- Productos con precio > 100 ---")
print(df[df["precio"] > 100])

# Limpieza
print("\n--- Nulos ---")
print(df.isnull().sum())

df["stock"] = df["stock"].fillna(df["stock"].mean())
print("\n--- Stock rellenado ---")
print(df["stock"])

# Agrupacion
print("\n--- Precio medio por categoria ---")
print(df.groupby("categoria")["precio"].mean())

# Añadir columna calculada
df["valor_stock"] = df["precio"] * df["stock"]
print("\n--- Valor en stock ---")
print(df[["producto", "valor_stock"]])
