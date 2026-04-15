# Analisis de Acciones — Course 5

Proyecto practico: extraer y visualizar datos financieros de Tesla y GameStop.

## Herramientas

- `yfinance` — datos historicos de bolsa
- `requests` + `BeautifulSoup` — scraping de revenue desde Macrotrends
- `pandas` — limpieza y transformacion
- `plotly` — dashboard de visualizacion

## Ejecutar

```bash
pip install yfinance beautifulsoup4 plotly pandas requests
jupyter notebook analisis_acciones.ipynb
```

## Estructura del notebook

1. Descargar datos de acciones (TSLA, GME)
2. Extraer datos de revenue con web scraping
3. Limpiar columnas de revenue
4. Crear dashboard con subplots precio / revenue

## Notas

El notebook se generara al completar el curso. Los pasos detallados
estan documentados en `../apuntes.md`.
