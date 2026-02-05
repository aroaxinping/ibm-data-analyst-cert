# Apuntes — Course 1: Introduction to Data Analytics

**Duracion:** 11 horas
**Modulos:** 4

---

## Que cubre este curso

Introduccion al mundo del analisis de datos desde la perspectiva de IBM: que
hace un analista, que tipos de datos existen, que herramientas se usan en el
sector y como es el proceso de analisis de principio a fin. Sin codigo todavia,
todo conceptual.

---

## Modulo 1: What is Data Analytics?

El curso empieza definiendo el campo desde cero.

**Definicion de analisis de datos:**
Proceso de recopilar, limpiar, analizar e interpretar datos para extraer
informacion util y apoyar decisiones de negocio.

**Tipos de analisis:**

| Tipo | Pregunta que responde | Ejemplo |
|------|-----------------------|---------|
| Descriptivo | ¿Que paso? | Ventas del ultimo trimestre |
| Diagnostico | ¿Por que paso? | Por que cayeron las ventas en marzo |
| Predictivo | ¿Que va a pasar? | Demanda prevista para Q4 |
| Prescriptivo | ¿Que deberia hacer? | Que estrategia maximiza el margen |

**El rol del analista de datos:**
- Identificar preguntas de negocio que se pueden responder con datos
- Recopilar y limpiar datos de distintas fuentes
- Analizar, interpretar y comunicar hallazgos
- Colaborar con stakeholders para traducir datos en accion

**Diferencia entre roles:**

| Rol | Enfoque |
|-----|---------|
| Analista de datos | Responder preguntas con datos existentes |
| Cientifico de datos | Construir modelos predictivos y trabajar con ML |
| Ingeniero de datos | Construir y mantener la infraestructura de datos |
| Analista de negocio | Traducir necesidades de negocio en requerimientos de datos |

---

## Modulo 2: The Data Analyst Ecosystem

El ecosistema de datos: donde viven los datos, como se mueven y que
herramientas se usan en cada etapa.

**Tipos de datos:**

- **Estructurados:** organizados en filas y columnas (tablas SQL, hojas de
  calculo). Faciles de buscar y analizar.
- **Semi-estructurados:** tienen alguna estructura pero no es rigida (JSON,
  XML, correos). Requieren procesamiento adicional.
- **No estructurados:** sin formato predefinido (imagenes, audio, video, texto
  libre). Mas dificiles de analizar, pero cada vez mas importantes.

**Fuentes de datos:**

- **Internas:** bases de datos de la empresa, CRM, ERP, logs de aplicaciones
- **Externas:** APIs publicas, datasets abiertos, redes sociales, proveedores
  de datos de terceros

**El ecosistema de herramientas:**

```
Almacenamiento      ->  Procesamiento    ->  Analisis         ->  Visualizacion
Bases de datos SQL      ETL / Python        Excel / Python       Tableau
Data Warehouses         Apache Spark        SQL                  Cognos
Data Lakes              Pandas              R                    Power BI
```

**Repositorios de datos:**

| Tipo | Descripcion | Ejemplo |
|------|-------------|---------|
| Base de datos relacional | Tablas con relaciones definidas | MySQL, PostgreSQL, IBM Db2 |
| Data Warehouse | Almacen optimizado para consultas analiticas | Amazon Redshift, BigQuery |
| Data Lake | Almacenamiento de datos en bruto sin procesar | AWS S3, Azure Data Lake |
| Data Mart | Subconjunto de un DW para un departamento | Marketing DW, Finance DW |

**OLTP vs OLAP:**

- **OLTP (Online Transaction Processing):** sistemas que registran transacciones
  en tiempo real (un pedido, un pago). Priorizan velocidad de escritura.
- **OLAP (Online Analytical Processing):** sistemas diseñados para consultas
  complejas sobre grandes volumenes de datos historicos. Priorizan velocidad
  de lectura.

---

## Modulo 3: Gathering and Wrangling Data

El proceso de conseguir datos limpios y listos para analizar.

**El proceso de recopilacion de datos:**

1. Identificar que datos necesito para responder la pregunta
2. Localizar las fuentes (internas, externas, APIs)
3. Recopilar los datos (descargar, consultar, conectar via API)
4. Evaluar la calidad de los datos (ROCCC o equivalente)
5. Limpiar y transformar

**Calidad de datos — las dimensiones:**

| Dimension | Que significa |
|-----------|---------------|
| Exactitud | Los datos reflejan la realidad |
| Completitud | No faltan valores importantes |
| Consistencia | Los datos son coherentes entre fuentes |
| Oportunidad | Los datos estan actualizados |
| Credibilidad | La fuente es fiable |
| Relevancia | Los datos son pertinentes para la pregunta |

**Wrangling (limpieza y transformacion):**

Pasos tipicos:
- Detectar y tratar valores nulos (eliminar, imputar o marcar)
- Eliminar duplicados
- Corregir tipos de datos (fecha como texto, numeros como string)
- Estandarizar formatos (fechas, monedas, codigos de pais)
- Filtrar registros irrelevantes
- Normalizar escalas si se van a comparar variables distintas

**Herramientas de wrangling:**

- Excel: Power Query para transformaciones sin codigo
- Python: pandas (el estandar del sector)
- SQL: queries de limpieza directamente en la base de datos
- OpenRefine: herramienta especializada en limpieza de datos

---

## Modulo 4: Mining & Visualizing Data and Communicating Results

El ultimo tramo del proceso: sacar insights y comunicarlos.

**Tecnicas de analisis exploratorio (EDA):**

- **Estadisticas descriptivas basicas:**
  - Media, mediana, moda
  - Desviacion tipica, varianza
  - Min, max, rango, percentiles
- **Distribuciones:** como se distribuyen los valores de una variable
- **Correlaciones:** relacion lineal entre dos variables (-1 a +1)
- **Valores atipicos (outliers):** puntos que se alejan mucho de la media

**Tecnicas de mineria de datos:**

| Tecnica | Para que |
|---------|----------|
| Clasificacion | Predecir a que categoria pertenece un registro |
| Regresion | Predecir un valor numerico |
| Clustering | Agrupar registros similares sin etiquetas previas |
| Asociacion | Encontrar items que aparecen juntos frecuentemente |
| Deteccion de anomalias | Identificar comportamientos inusuales |

**Visualizacion — principios basicos:**

- Elegir el tipo de grafico segun el proposito:
  - Comparacion: barras
  - Evolucion en el tiempo: lineas
  - Proporcion: circular (con moderacion)
  - Relacion entre variables: dispersion (scatter)
  - Distribucion: histograma, boxplot
- Menos es mas: eliminar elementos que no añaden informacion
- Titulo claro que explique el hallazgo, no solo el contenido
- Etiquetar ejes siempre, con unidades

**Comunicar resultados:**

El analisis no termina con los graficos. La comunicacion efectiva implica:
- Adaptar el nivel de detalle al publico (tecnico vs ejecutivo)
- Contar una historia con los datos (narrative analytics)
- Responder directamente a la pregunta que origino el analisis
- Ser transparente sobre las limitaciones y supuestos

---

## Esquema resumido del curso

```
COURSE 1: INTRODUCTION
|
+-- Tipos de analisis
|     Descriptivo -> Diagnostico -> Predictivo -> Prescriptivo
|
+-- El ecosistema de datos
|     Tipos de datos (estructurado, semi, no estructurado)
|     Herramientas (almacenamiento, procesamiento, analisis, viz)
|
+-- El proceso completo
|     Recopilar -> Limpiar -> Analizar -> Visualizar -> Comunicar
|
+-- Calidad de datos
      Exactitud, completitud, consistencia, oportunidad, credibilidad
```

---

## Glosario

| Termino | Definicion |
|---------|------------|
| Analisis descriptivo | Analisis que responde "que paso" usando datos historicos |
| Analisis diagnostico | Analisis que responde "por que paso" identificando causas |
| Analisis predictivo | Uso de modelos estadisticos para anticipar resultados futuros |
| Analisis prescriptivo | Recomendaciones sobre que accion tomar basadas en datos |
| Datos estructurados | Datos organizados en formato tabular con filas y columnas |
| Datos no estructurados | Datos sin formato predefinido: imagenes, audio, texto libre |
| Data Warehouse | Repositorio centralizado de datos historicos para analisis |
| Data Lake | Almacen de datos en bruto en su formato original |
| OLTP | Sistemas diseñados para procesar transacciones en tiempo real |
| OLAP | Sistemas diseñados para consultas analiticas complejas |
| ETL | Extract, Transform, Load — proceso de mover datos entre sistemas |
| Wrangling | Proceso de limpiar y transformar datos en bruto |
| EDA | Exploratory Data Analysis — exploracion inicial de un dataset |
| Outlier | Valor atipico que se aleja significativamente del resto |
| Correlacion | Medida de la relacion lineal entre dos variables |

---

## Errores comunes

- **Confundir correlacion con causalidad:** dos variables pueden moverse juntas
  sin que una cause la otra. Siempre investigar si hay una causa comun o
  un factor de confusion.
- **Saltar directamente a las herramientas:** el analisis empieza con una
  pregunta clara. Sin pregunta, los datos no tienen contexto.
- **Ignorar la calidad de los datos:** analizar datos incorrectos o incompletos
  produce conclusiones erroneas aunque el analisis tecnico sea perfecto.
- **Visualizaciones engañosas:** truncar el eje Y, usar escalas diferentes
  en comparaciones, o elegir el tipo de grafico incorrecto distorsiona
  la percepcion de los datos.

---

## Conexion con otros cursos

- El proceso Recopilar -> Limpiar -> Analizar -> Visualizar -> Comunicar
  es la columna vertebral del certificado. Cada curso profundiza en una parte.
- Los tipos de datos (estructurado, semi, no estructurado) determinan que
  herramienta usar: SQL para estructurados (curso 6), Python para todos
  los tipos (cursos 4, 7).
- Las tecnicas de EDA introducidas aqui se implementan en Python con pandas
  y matplotlib en los cursos 7 y 8.
- El concepto de calidad de datos reaparece en los cursos 2 y 6 al trabajar
  con Excel y SQL para limpiar datasets reales.

---

## Lo mas importante de este curso

Hay cuatro tipos de analisis y cada uno responde una pregunta diferente.
La mayoria del trabajo de un analista junior es descriptivo y diagnostico.
El predictivo y prescriptivo requieren estadistica y ML.

El ecosistema de herramientas no se elige por preferencia — se elige segun
el tipo de dato, el volumen y la pregunta. Esto es lo que diferencia a un
analista que sabe usar herramientas de uno que sabe analizar.
