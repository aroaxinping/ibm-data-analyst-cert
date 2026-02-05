# Modulo 1: Matplotlib — Tipos de grafico esenciales

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Dataset de ejemplo: ventas trimestrales por producto
np.random.seed(42)
trimestres = ["Q1 2023", "Q2 2023", "Q3 2023", "Q4 2023",
              "Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"]
ventas_a = [120, 145, 162, 210, 185, 230, 250, 310]
ventas_b = [95, 110, 130, 175, 160, 195, 220, 280]
datos_precio = np.random.normal(25000, 8000, 200)

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle("Tipos de grafico — Matplotlib", fontsize=16, y=1.02)

# 1. Grafico de lineas
axes[0, 0].plot(trimestres, ventas_a, marker="o", color="steelblue",
                linewidth=2, label="Producto A")
axes[0, 0].plot(trimestres, ventas_b, marker="s", color="coral",
                linewidth=2, linestyle="--", label="Producto B")
axes[0, 0].set_title("Ventas por trimestre")
axes[0, 0].set_ylabel("Unidades")
axes[0, 0].legend()
axes[0, 0].tick_params(axis="x", rotation=45)
axes[0, 0].grid(True, alpha=0.3)

# 2. Barras agrupadas
x = np.arange(len(trimestres))
width = 0.35
axes[0, 1].bar(x - width/2, ventas_a, width, label="Producto A",
               color="steelblue", edgecolor="white")
axes[0, 1].bar(x + width/2, ventas_b, width, label="Producto B",
               color="coral", edgecolor="white")
axes[0, 1].set_title("Ventas comparadas")
axes[0, 1].set_xticks(x)
axes[0, 1].set_xticklabels(trimestres, rotation=45, ha="right")
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3, axis="y")

# 3. Barras horizontales
departamentos = ["IT", "Marketing", "Datos", "Finanzas", "Ventas"]
presupuesto = [450, 280, 380, 320, 510]
colores = ["steelblue" if p == max(presupuesto) else "lightsteelblue" for p in presupuesto]
axes[0, 2].barh(departamentos, presupuesto, color=colores)
axes[0, 2].set_title("Presupuesto por departamento (k€)")
axes[0, 2].set_xlabel("Miles de euros")
for i, v in enumerate(presupuesto):
    axes[0, 2].text(v + 5, i, str(v), va="center")
axes[0, 2].grid(True, alpha=0.3, axis="x")

# 4. Histograma
axes[1, 0].hist(datos_precio, bins=25, color="steelblue",
                edgecolor="white", alpha=0.8)
axes[1, 0].axvline(np.mean(datos_precio), color="red",
                   linestyle="--", label=f"Media: {np.mean(datos_precio):.0f}")
axes[1, 0].set_title("Distribucion de precios")
axes[1, 0].set_xlabel("Precio (€)")
axes[1, 0].set_ylabel("Frecuencia")
axes[1, 0].legend()

# 5. Scatter
x_scatter = np.random.normal(150, 40, 100)
y_scatter = x_scatter * 120 + np.random.normal(0, 3000, 100)
colores_scatter = np.where(x_scatter > 150, "steelblue", "coral")
axes[1, 1].scatter(x_scatter, y_scatter, c=colores_scatter, alpha=0.6, s=50)
axes[1, 1].set_title("Caballos vs Precio")
axes[1, 1].set_xlabel("Caballos (CV)")
axes[1, 1].set_ylabel("Precio (€)")
axes[1, 1].grid(True, alpha=0.3)

# 6. Boxplot comparativo
datos_por_categoria = [
    np.random.normal(20000, 5000, 50),
    np.random.normal(35000, 8000, 50),
    np.random.normal(55000, 12000, 50)
]
bp = axes[1, 2].boxplot(datos_por_categoria, labels=["Bajo", "Medio", "Alto"],
                         patch_artist=True)
colores_box = ["lightblue", "steelblue", "darkblue"]
for patch, color in zip(bp["boxes"], colores_box):
    patch.set_facecolor(color)
axes[1, 2].set_title("Precio por segmento")
axes[1, 2].set_ylabel("Precio (€)")
axes[1, 2].grid(True, alpha=0.3, axis="y")

plt.tight_layout()
plt.savefig("tipos_graficos.png", dpi=150, bbox_inches="tight")
plt.show()
print("Grafico guardado como tipos_graficos.png")
