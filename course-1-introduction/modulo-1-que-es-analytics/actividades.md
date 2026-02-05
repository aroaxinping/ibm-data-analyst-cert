# Actividades — Modulo 1: What is Data Analytics?

---

## Actividad 1: Clasificar tipos de analisis

El modulo propone identificar el tipo de analisis en situaciones reales.

**Instrucciones:** para cada escenario, identificar si es descriptivo,
diagnostico, predictivo o prescriptivo. Justificar la respuesta.

---

**Escenario A — E-commerce de moda:**
Un informe muestra que la tasa de devolucion de productos fue del 34% en
el ultimo trimestre, un 8% mas que el trimestre anterior.

*Mi clasificacion:* Descriptivo
*Justificacion:* Describe lo que paso (tasa de devolucion y su variacion).
No busca causas ni predice.

---

**Escenario B — Misma empresa, un mes despues:**
El equipo investiga y descubre que el 70% de las devoluciones corresponden
a productos de talla L y XL, y que las fotos de producto no mostraban el
tejido con la suficiente claridad.

*Mi clasificacion:* Diagnostico
*Justificacion:* Identifica la causa del problema detectado en el escenario A.

---

**Escenario C — Banco:**
Un modelo calcula que un cliente tiene un 78% de probabilidad de no renovar
su hipoteca el proximo año, basandose en su historial de pagos, movimientos
de cuenta y datos externos de mercado inmobiliario.

*Mi clasificacion:* Predictivo
*Justificacion:* Anticipa un resultado futuro usando un modelo estadistico.

---

**Escenario D — Misma empresa, accion derivada:**
Basandose en ese 78%, el sistema genera automaticamente una oferta
personalizada de refinanciacion para ese cliente con condiciones mas
favorables que las del mercado.

*Mi clasificacion:* Prescriptivo
*Justificacion:* Recomienda (y en este caso ejecuta automaticamente)
la accion a tomar a partir de la prediccion.

---

**Escenario E — Supermercado:**
El director de operaciones quiere saber cuales fueron los 10 productos mas
vendidos la semana pasada en cada tienda.

*Mi clasificacion:* _(completar)_
*Justificacion:* _(completar)_

---

**Escenario F — Plataforma de streaming:**
El sistema detecta que un usuario lleva 3 semanas sin abrir la app y le
envia una notificacion push con una recomendacion de serie basada en su
historial, calculando que eso aumenta en un 40% la probabilidad de reactivacion.

*Mi clasificacion:* _(completar)_
*Justificacion:* _(completar)_

---

## Actividad 2: Mapear roles a responsabilidades

El modulo presenta los cuatro roles principales del ecosistema de datos.
Esta actividad consiste en asignar cada tarea al rol correcto.

**Tareas:**

| Tarea | Rol |
|-------|-----|
| Crear un pipeline que mueve datos de la app al data warehouse cada hora | _(completar)_ |
| Analizar por que la conversion de la landing page bajo un 12% | _(completar)_ |
| Construir un modelo que predice el churn de clientes a 90 dias | _(completar)_ |
| Crear un informe semanal de ventas para el equipo comercial | _(completar)_ |
| Diseñar el schema de la base de datos del nuevo producto | _(completar)_ |
| Traducir la necesidad del director de marketing ("quiero saber si la campaña funciona") en una especificacion de datos concreta | _(completar)_ |
| Identificar que variables predicen mejor el precio de un piso en Barcelona | _(completar)_ |
| Automatizar la extraccion diaria de datos de Google Analytics a Google Sheets | _(completar)_ |

**Respuestas:**

<details>
<summary>Ver respuestas</summary>

| Tarea | Rol |
|-------|-----|
| Pipeline datos → data warehouse | Ingeniero de datos |
| Analizar caida de conversion | Analista de datos |
| Modelo de churn a 90 dias | Cientifico de datos |
| Informe semanal de ventas | Analista de datos |
| Diseñar schema de base de datos | Ingeniero de datos |
| Traducir necesidad de negocio en specs | Analista de negocio |
| Variables predictoras del precio | Cientifico de datos |
| Automatizar extraccion diaria | Ingeniero de datos (o analista con conocimientos de scripting) |

</details>

---

## Actividad 3: El proceso de analisis aplicado

El modulo introduce el framework de 6 pasos. Esta actividad lo aplica a
un caso concreto.

**Caso:** una tienda online nota que las ventas han bajado un 15% en los
ultimos dos meses. El CEO quiere entender por que y que hacer.

**Completar el framework:**

| Paso | Que haria en este caso |
|------|------------------------|
| 1. Definir | _(completar)_ |
| 2. Recopilar | _(completar)_ |
| 3. Preparar | _(completar)_ |
| 4. Analizar | _(completar)_ |
| 5. Visualizar | _(completar)_ |
| 6. Comunicar | _(completar)_ |

**Mi respuesta:**

| Paso | Que haria en este caso |
|------|------------------------|
| 1. Definir | ¿En que productos, regiones y canales se concentra la caida? ¿Coincide con algun cambio interno (precios, web) o externo (competencia, estacionalidad)? |
| 2. Recopilar | Datos de ventas por producto/region/canal de los ultimos 6 meses. Datos de trafico web. Precios de la competencia. Datos de campañas de marketing |
| 3. Preparar | Unificar fuentes, tratar nulos en columnas de ventas, estandarizar fechas, crear columna de variacion mensual |
| 4. Analizar | Comparar ventas mes a mes por segmento. Analizar si la caida es general o especifica. Buscar correlacion con cambios en trafico, conversion o precios |
| 5. Visualizar | Grafico de lineas de ventas por canal. Mapa de calor de ventas por producto y region. Comparativa antes/despues |
| 6. Comunicar | Presentar hallazgos al CEO con 3-4 bullets: donde esta la caida, la causa mas probable, y la recomendacion concreta |
