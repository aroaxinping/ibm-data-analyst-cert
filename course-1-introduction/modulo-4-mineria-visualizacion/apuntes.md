# Modulo 4: Mining & Visualizing Data and Communicating Results

**Semana:** 3
**Duracion estimada:** 2.5 horas

---

## De que va este modulo

El ultimo modulo del curso cubre las dos etapas finales del proceso:
extraer insights de los datos (mineria y analisis exploratorio) y
comunicarlos de forma efectiva mediante visualizaciones y presentaciones.
Es el modulo mas orientado a la comunicacion, no solo a la tecnica.

---

## 1. Analisis exploratorio de datos (EDA)

Antes de construir modelos o sacar conclusiones, se hace un EDA para
entender que tiene el dataset. Es el equivalente a leer el libro antes
de escribir el resumen.

**Que se busca en un EDA:**

- Como se distribuyen los valores de cada variable
- Si hay valores atipicos o anomalias
- Si hay relaciones entre variables
- Si hay patrones temporales o estacionales
- Si los datos tienen los problemas de calidad que se esperaban

**Estadisticas descriptivas basicas:**

| Estadistica | Para que sirve |
|-------------|----------------|
| Media | Valor central de la distribucion (sensible a outliers) |
| Mediana | Valor central real (robusta ante outliers) |
| Moda | Valor mas frecuente |
| Desviacion tipica | Dispersion respecto a la media |
| Min / Max | Rango total de los valores |
| Percentiles | Como se distribuyen los valores (P25, P75, P90...) |
| Correlacion | Relacion lineal entre dos variables (-1 a +1) |

**Cuando usar media vs mediana:**
Si la distribucion es simetrica, ambas son parecidas y cualquiera vale.
Si hay outliers o la distribucion es asimetrica (como los salarios o
los precios de pisos), la mediana representa mejor el "centro" real.

**Correlacion:**
Mide la relacion lineal entre dos variables. Va de -1 a +1:
- +1: cuando una sube, la otra sube (relacion perfecta positiva)
- 0: no hay relacion lineal
- -1: cuando una sube, la otra baja (relacion perfecta negativa)

Importante: **correlacion no implica causalidad**. Que dos variables
estean correlacionadas no significa que una cause la otra. Puede haber
una tercera variable que explique ambas, o puede ser pura coincidencia.

---

## 2. Tecnicas de mineria de datos

La mineria de datos usa algoritmos para encontrar patrones en grandes
volumenes de datos que seria imposible detectar manualmente.

| Tecnica | Que hace | Ejemplo |
|---------|----------|---------|
| **Clasificacion** | Predice a que categoria pertenece un registro | ¿Este email es spam o no? |
| **Regresion** | Predice un valor numerico | ¿Cuanto costara este piso? |
| **Clustering** | Agrupa registros similares sin categorias previas | Segmentar clientes por comportamiento |
| **Asociacion** | Encuentra items que aparecen juntos frecuentemente | "Los que compraron X tambien compraron Y" |
| **Deteccion de anomalias** | Identifica comportamientos inusuales | Detectar transacciones fraudulentas |
| **Series temporales** | Analiza patrones a lo largo del tiempo | Predecir la demanda del proximo mes |

Estas tecnicas se aprenden con mas profundidad en los cursos 7 y 8.
En este modulo solo se introduce el concepto de cada una.

---

## 3. Visualizacion de datos

La visualizacion convierte numeros en historias visuales que la gente
puede entender sin tener conocimientos tecnicos.

**El grafico correcto para cada proposito:**

| Pregunta | Tipo de grafico |
|----------|----------------|
| ¿Como ha evolucionado X a lo largo del tiempo? | Lineas |
| ¿Cuanto tiene cada categoria? | Barras verticales u horizontales |
| ¿Que proporcion representa cada parte del total? | Circular (con moderacion, max 5-6 categorias) |
| ¿Hay relacion entre X e Y? | Dispersion (scatter) |
| ¿Como se distribuyen los valores? | Histograma o boxplot |
| ¿Cuales son los extremos y la mediana? | Boxplot |
| ¿Como se distribuye algo geograficamente? | Mapa |
| ¿Como se relacionan muchas variables a la vez? | Heatmap de correlacion |

**Principios de una buena visualizacion:**

1. **Un mensaje por grafico.** El grafico debe responder una pregunta concreta,
   no mostrar todos los datos disponibles.

2. **Titulo que explica el hallazgo.** No "Ventas por trimestre" sino
   "Las ventas crecieron un 23% en Q4 respecto al trimestre anterior".

3. **Etiquetar los ejes siempre**, con unidades.

4. **Menos es mas.** Eliminar todo lo que no añada informacion:
   gridlines innecesarias, colores sin significado, bordes decorativos.

5. **Consistencia en colores.** El mismo color siempre para la misma categoria.
   Paleta accesible para daltonismo (no depender solo de rojo/verde).

6. **No distorsionar.** El eje Y debe empezar en cero cuando se comparan
   magnitudes. Truncarlo exagera las diferencias visualmente.

**Herramientas de visualizacion:**

- **Excel / Google Sheets:** para graficos rapidos y comunicacion interna
- **Tableau / Power BI:** para dashboards interactivos y profesionales
- **IBM Cognos:** plataforma de BI empresarial (se usa en el curso 3)
- **Python (matplotlib, seaborn, plotly):** para graficos personalizados
  y automatizados (cursos 7 y 8)

---

## 4. Comunicar resultados

El analisis no termina cuando se hace el grafico. La comunicacion efectiva
es la ultima milla que convierte el trabajo en impacto.

**Adaptar el mensaje al publico:**

| Publico | Que quiere ver | Que evitar |
|---------|---------------|------------|
| CEO / directivo | Los 3-4 hallazgos clave y la recomendacion | Detalles tecnicos, metodologia |
| Manager de area | Hallazgos relevantes para su area con contexto | Jerga estadistica |
| Equipo tecnico | Metodologia, supuestos, limitaciones, codigo | Simplificar en exceso |

**Estructura de una buena presentacion de analisis:**

1. La pregunta — recordar que problema se estaba resolviendo
2. Los hallazgos principales — max 3-4 puntos, con soporte visual
3. La recomendacion — concreta y accionable
4. Las limitaciones — ser transparente sobre los supuestos y lo que
   los datos NO pueden responder

**Narrative analytics (contar una historia con datos):**
Los datos solos no convencen. La historia que construyes alrededor de
ellos si. El contexto, la comparativa con algo conocido, y la conexion
con una decision real son lo que hace que un analisis se convierta en accion.

---

## 5. El ciclo completo: de la pregunta a la recomendacion

```
PREGUNTA DE NEGOCIO
        |
        v
RECOPILACION DE DATOS
  (fuentes internas + externas)
        |
        v
EVALUACION DE CALIDAD
  (exactitud, completitud, consistencia...)
        |
        v
WRANGLING
  (limpiar, transformar, estandarizar)
        |
        v
EDA
  (estadisticas, distribuciones, correlaciones)
        |
        v
ANALISIS / MINERIA
  (responder la pregunta con evidencia)
        |
        v
VISUALIZACION
  (hacer los hallazgos comprensibles)
        |
        v
COMUNICACION
  (recomendacion concreta y accionable)
```

---

## Glosario del modulo

| Termino | Definicion |
|---------|------------|
| EDA | Exploratory Data Analysis — exploracion inicial de un dataset para entender su estructura y distribuciones |
| Media | Suma de todos los valores dividida entre el numero de valores |
| Mediana | Valor que divide la distribucion en dos mitades iguales |
| Desviacion tipica | Medida de la dispersion de los valores respecto a la media |
| Percentil | Valor por debajo del cual cae un porcentaje dado de los datos |
| Correlacion | Medida estadistica de la relacion lineal entre dos variables (-1 a +1) |
| Causalidad | Relacion en la que un evento produce directamente otro |
| Clasificacion | Tecnica de mineria que predice la categoria a la que pertenece un registro |
| Clustering | Tecnica que agrupa registros similares sin categorias previas definidas |
| Regresion | Tecnica que predice un valor numerico continuo |
| Narrative analytics | Presentacion de datos estructurada como una historia para facilitar su comprension |
| Dashboard | Vista consolidada de las metricas clave de un negocio en una sola pantalla |

---

## Lo mas importante de este modulo

Dos ideas clave:

1. **Correlacion no es causalidad.** Es el error estadistico mas frecuente
   y el que mas daño hace en la toma de decisiones. Siempre investigar
   si hay una explicacion alternativa antes de concluir que A causa B.

2. **El analisis no termina con los numeros.** Un hallazgo que no se
   comunica bien es un hallazgo que no genera impacto. La visualizacion
   y la narrativa son habilidades tan importantes como el analisis tecnico.
