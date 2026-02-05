# Proyecto Final — Dashboard de Aviacion con Dash

**Dataset:** datos de aerolineas de Estados Unidos (retrasos de vuelos)
**Objetivo:** crear un dashboard interactivo con Dash que permita explorar
los datos de retrasos por año, aerolinea y tipo de causa

## KPIs del dashboard

- Numero total de vuelos del periodo seleccionado
- Porcentaje de vuelos con retraso
- Retraso medio en minutos

## Visualizaciones

1. Grafico de lineas: evolucion del retraso medio por año
2. Barras: causas de retraso por aerolinea (retraso en carrier, clima, seguridad, NAS)
3. Mapa de calor (heatmap): retrasos por mes y aerolinea
4. Mapa con Folium: aeropuertos con mayor tasa de retraso
5. Scatter: numero de vuelos vs retraso medio por aerolinea

## Filtros del dashboard

- Selector de año (dropdown)
- Selector de aerolinea (dropdown multiple)
- Slider de rango de retraso

## Ejecutar

```bash
pip install dash plotly pandas folium
python app.py
# Abrir http://127.0.0.1:8050 en el navegador
```

## Notas

El codigo de la app Dash se añadira al completar el curso.
La estructura del callback principal: el dropdown de año y aerolinea
activan la actualizacion de todos los graficos simultaneamente.
