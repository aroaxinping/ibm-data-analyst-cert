# Actividades — Modulo 3: Gathering and Wrangling Data

---

## Actividad 1: Evaluar la calidad de un dataset

**Dataset hipotetico:** registros de ventas de una tienda online.

| id_pedido | fecha | cliente | producto | cantidad | precio | region |
|-----------|-------|---------|----------|----------|--------|--------|
| 1001 | 15/03/2024 | Ana Garcia | Laptop | 1 | 899.99 | Madrid |
| 1001 | 15/03/2024 | Ana Garcia | Laptop | 1 | 899.99 | Madrid |
| 1002 | 2024-03-16 | | Raton | 2 | 29.99 | |
| 1003 | 17 marzo 24 | Luis Martinez | Monitor | 1 | -349.99 | Barcelona |
| 1004 | 18/03/2024 | Sara Gomez | Teclado | 0 | 59.99 | madrid |
| 1005 | 18/03/2024 | Carlos Ruiz | Webcam | 1 | 79.99 | Barcelona |

**Identificar los problemas de calidad:**

| Problema | Fila/columna afectada | Dimension de calidad | Como tratarlo |
|----------|-----------------------|----------------------|---------------|
| Registro duplicado | Fila 1 y 2 (id 1001) | Consistencia | Eliminar uno de los dos |
| Fecha en tres formatos distintos | Columna fecha | Consistencia | Estandarizar a un unico formato (ISO: YYYY-MM-DD) |
| Cliente vacio | Fila 3 (id 1002) | Completitud | Investigar si se puede recuperar; si no, marcar como nulo |
| Region vacia | Fila 3 (id 1002) | Completitud | Igual — investigar o dejar como nulo |
| Precio negativo | Fila 4 (id 1003) | Exactitud | Probablemente error de entrada — tratar como nulo o corregir |
| Cantidad = 0 | Fila 5 (id 1004) | Exactitud | Un pedido de 0 unidades no tiene sentido — investigar |
| "madrid" en minusculas | Fila 5 (id 1004) | Consistencia | Estandarizar a "Madrid" |

---

## Actividad 2: Decidir la estrategia de limpieza

Para cada caso, elegir la estrategia correcta y justificarla.

**Caso A:** Dataset de 10.000 clientes. La columna "telefono" tiene nulos
en el 3% de los registros. El analisis solo usa email y ciudad.

*Estrategia:* Dejar los nulos tal como estan. La columna telefono no se usa
en el analisis y el porcentaje es bajo. No merece la pena imputar.

---

**Caso B:** Dataset de 500 empleados. La columna "salario" tiene nulos
en el 8% de los registros. Se va a calcular el salario medio por departamento.

*Estrategia:* Imputar con la mediana del departamento correspondiente (no la
mediana global, porque los salarios varian mucho por departamento). Documentar
que el 8% de los valores fue imputado. Alternativa conservadora: excluir esos
registros del calculo de la media y documentarlo.

---

**Caso C:** Dataset de transacciones bancarias. La columna "id_cuenta" tiene
nulos en el 40% de los registros. Es la clave para unir con otra tabla.

*Estrategia:* No imputar — un id no se puede inventar. Hay dos opciones:
investigar por que el 40% esta vacio (puede haber un bug en la extraccion)
o excluir esos registros del analisis y documentar claramente la limitacion.
Un 40% de nulos en una clave es una senal de alerta grave.

---

**Caso D:** Un dataset de precios de inmuebles tiene 10 registros con
precio superior a 5 millones de euros en un dataset de 2.000 propiedades.
El analisis es sobre vivienda habitual en ciudades medias espanolas.

*Estrategia:* Excluir los 10 registros del analisis y documentarlo
explicitamente: "se excluyen propiedades con precio superior a 5M€ por estar
fuera del segmento de analisis (vivienda habitual)". No son errores — son
propiedades reales pero fuera del scope.

---

## Actividad 3: Trazar el plan de recopilacion

**Pregunta de negocio:** ¿en que ciudades y meses tiene mas cancelaciones
un hotel, y cual es la causa principal?

Completar el plan de recopilacion:

| Paso | Que haria |
|------|-----------|
| 1. Definir | ¿Que significa "cancelacion"? ¿Solo reservas canceladas o tambien no-shows? ¿Que periodo de tiempo? ¿Se incluyen todos los tipos de habitacion? |
| 2. Identificar fuentes | Sistema de reservas del hotel (interno), datos de clima por ciudad y mes (API externa), datos de eventos locales (web scraping o API), historico de precios de la competencia (fuente externa) |
| 3. Evaluar calidad | ¿El sistema de reservas distingue cancelaciones de no-shows? ¿Hay datos de los ultimos X anos o solo del reciente? ¿Los datos de clima cubren las ciudades del hotel? |
| 4. Recopilar | Exportar CSV del sistema de reservas, descargar datos de clima de una API meteorologica, obtener calendario de eventos de cada ciudad |
| 5. Limpiar | Estandarizar fechas, verificar que los tipos de cancelacion son consistentes, unir los tres datasets por ciudad y fecha, tratar nulos en la columna "motivo_cancelacion" |
