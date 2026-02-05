# Modulo 2: Seaborn — Graficos estadisticos

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sns.set_theme(style="whitegrid", palette="muted")
np.random.seed(42)

# Dataset de ejemplo
n = 200
df = pd.DataFrame({
    "precio": np.concatenate([
        np.random.normal(25000, 5000, 80),
        np.random.normal(45000, 10000, 70),
        np.random.normal(70000, 15000, 50)
    ]),
    "caballos": np.concatenate([
        np.random.normal(100, 20, 80),
        np.random.normal(180, 35, 70),
        np.random.normal(280, 50, 50)
    ]),
    "cilindrada": np.concatenate([
        np.random.normal(1600, 200, 80),
        np.random.normal(2400, 300, 70),
        np.random.normal(3500, 500, 50)
    ]),
    "segmento": ["Compacto"] * 80 + ["Medio"] * 70 + ["Premium"] * 50,
    "combustible": np.random.choice(["gasolina", "diesel", "electrico"],
                                     n, p=[0.5, 0.35, 0.15])
})

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle("Graficos estadisticos — Seaborn", fontsize=16)

# 1. Histograma + KDE
sns.histplot(data=df, x="precio", hue="segmento", bins=20,
             kde=True, alpha=0.6, ax=axes[0, 0])
axes[0, 0].set_title("Distribucion de precios por segmento")
axes[0, 0].set_xlabel("Precio (€)")

# 2. Boxplot comparativo
sns.boxplot(data=df, x="segmento", y="precio",
            palette="muted", ax=axes[0, 1])
axes[0, 1].set_title("Precio por segmento — Boxplot")
axes[0, 1].set_ylabel("Precio (€)")

# 3. Violin plot
sns.violinplot(data=df, x="combustible", y="precio",
               palette="pastel", inner="box", ax=axes[0, 2])
axes[0, 2].set_title("Precio por combustible — Violin")

# 4. Scatter con regresion
sns.scatterplot(data=df, x="caballos", y="precio",
                hue="segmento", alpha=0.6, ax=axes[1, 0])
# Añadir linea de regresion sobre el scatter
sns.regplot(data=df, x="caballos", y="precio",
            scatter=False, color="red", ax=axes[1, 0])
axes[1, 0].set_title("Caballos vs Precio")

# 5. Barplot con CI
sns.barplot(data=df, x="segmento", y="precio",
            hue="combustible", palette="muted",
            errorbar="ci", ax=axes[1, 1])
axes[1, 1].set_title("Precio medio por segmento y combustible")
axes[1, 1].legend(title="Combustible", loc="upper left")

# 6. Heatmap de correlacion
correlaciones = df[["precio", "caballos", "cilindrada"]].corr()
sns.heatmap(correlaciones, annot=True, fmt=".2f",
            cmap="coolwarm", center=0,
            square=True, linewidths=1,
            ax=axes[1, 2])
axes[1, 2].set_title("Matriz de correlacion")

plt.tight_layout()
plt.savefig("seaborn_graficos.png", dpi=150, bbox_inches="tight")
plt.show()
print("Grafico guardado como seaborn_graficos.png")

# Pairplot (grafico separado por su tamaño)
g = sns.pairplot(df[["precio", "caballos", "cilindrada", "segmento"]],
                 hue="segmento", diag_kind="kde",
                 plot_kws={"alpha": 0.5})
g.fig.suptitle("Pairplot — relaciones entre variables", y=1.02)
plt.savefig("pairplot.png", dpi=120, bbox_inches="tight")
plt.show()
