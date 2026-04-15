# Proyecto Final — Analisis de Precios de Automoviles

**Dataset:** UCI Automobile Dataset (1985)
**Objetivo:** predecir el precio de un automovil a partir de sus caracteristicas

## Flujo del analisis

1. Cargar y explorar el dataset (205 automoviles, 26 variables)
2. Wrangling: tratar nulos, corregir tipos, estandarizar unidades
3. EDA: correlaciones, distribuciones, segmentacion por fabricante y carroceria
4. Modelado: regresion lineal simple, multiple y polinomica
5. Evaluacion: R², RMSE, MAE con train/test split y cross-validation

## Variables mas correlacionadas con el precio

| Variable | Correlacion con precio |
|----------|------------------------|
| Motor (caballos) | +0.81 |
| Cilindrada | +0.79 |
| Peso | +0.75 |
| Longitud | +0.69 |
| Consumo ciudad | -0.70 |

## Resultados del modelo

| Modelo | R² (test) | RMSE |
|--------|-----------|------|
| Regresion lineal simple (cilindrada) | — | — |
| Regresion lineal multiple (4 vars) | — | — |
| Regresion polinomica grado 2 | — | — |
| Ridge (alpha=1.0) | — | — |

_(completar al terminar el curso)_

## Ejecutar

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
python wrangling.py
python regresion.py
```
