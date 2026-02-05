# Modulo 2: The Data Analyst Ecosystem

**Semana:** 1-2
**Duracion estimada:** 3 horas

---

## De que va este modulo

Explica donde viven los datos, como se mueven y que herramientas existen
en cada etapa. Es un modulo de orientacion: no se aprende a usar ninguna
herramienta todavia, pero se entiende para que sirve cada una y en que
parte del proceso encaja. Util para no perderse cuando los cursos siguientes
empiecen a nombrar cosas como ETL, data warehouse o OLAP.

---

## 1. Tipos de datos

Todo parte de entender que no todos los datos tienen la misma forma.
Esto determina que herramientas se pueden usar con ellos.

**Datos estructurados:**
- Organizados en filas y columnas, con un esquema fijo
- Cada columna tiene un tipo definido (numero, texto, fecha...)
- Ejemplos: tablas de una base de datos SQL, hojas de calculo, CSVs
- Faciles de buscar, filtrar y analizar con SQL o Excel

**Datos semi-estructurados:**
- Tienen alguna estructura pero no es rigida ni uniforme
- El esquema puede variar entre registros
- Ejemplos: JSON, XML, correos electronicos, logs de aplicaciones
- Requieren procesamiento para convertirlos en algo analizable

**Datos no estructurados:**
- Sin formato predefinido
- No tienen filas ni columnas
- Ejemplos: imagenes, audio, video, texto libre, posts de redes sociales
- Representan el 80% de los datos del mundo
- Requieren tecnicas especiales: procesamiento de lenguaje natural,
  vision por computador, etc.

**Regla practica:**

```
Estructurados   ->  SQL, Excel          (facil)
Semi-estruc.    ->  Python, ETL         (medio)
No estruc.      ->  ML, NLP, CV         (avanzado)
```

---

## 2. Fuentes de datos

**Datos internos:**
Generados dentro de la propia empresa. Son los mas faciles de acceder
y suelen ser los mas relevantes para las preguntas de negocio.

- Bases de datos de transacciones (pedidos, pagos, registros)
- CRM (datos de clientes y ventas)
- ERP (recursos empresariales: inventario, finanzas, RRHH)
- Logs de aplicaciones y web
- Encuestas internas

**Datos externos:**
Proceden de fuera de la empresa. Aportan contexto que los datos internos
no tienen (competencia, mercado, tendencias).

- APIs publicas (Twitter, Google Trends, bancos de datos gubernamentales)
- Datasets abiertos (Kaggle, UCI ML Repository, datos.gob.es)
- Proveedores de datos de terceros (Nielsen, Euromonitor...)
- Web scraping (con permiso y dentro de los terminos de uso del sitio)
- Redes sociales

---

## 3. El ecosistema de herramientas

El recorrido de un dato desde que se genera hasta que se usa en un analisis
pasa por cuatro etapas, cada una con sus herramientas:

```
ALMACENAMIENTO  ->  PROCESAMIENTO  ->  ANALISIS  ->  VISUALIZACION

Bases de datos      ETL / Python       Excel         Tableau
Data Warehouses     Apache Spark       Python        Cognos
Data Lakes          Pandas             SQL           Power BI
NoSQL               dbt                R             Looker
```

**Almacenamiento:**
Donde viven los datos. El tipo de almacenamiento depende del volumen,
la velocidad de acceso y si los datos son estructurados o no.

**Procesamiento:**
Mover, transformar y preparar datos. ETL es el proceso clasico:
Extract (extraer de la fuente), Transform (limpiar y transformar),
Load (cargar en el destino).

**Analisis:**
Las herramientas con las que el analista trabaja directamente.
SQL para consultas sobre bases de datos, Python/pandas para analisis
mas complejos, Excel para datasets pequenos y comunicacion rapida.

**Visualizacion:**
Convertir los resultados en graficos y dashboards que otros puedan entender.

---

## 4. Repositorios de datos

Distintos tipos de almacenamiento segun el proposito:

**Base de datos relacional (RDBMS):**
- Organiza los datos en tablas con relaciones entre ellas
- Se consultan con SQL
- Optimizadas para escritura y lectura de transacciones
- Ejemplos: MySQL, PostgreSQL, IBM Db2, Oracle, SQL Server

**Data Warehouse:**
- Almacen centralizado de datos historicos de toda la empresa
- Optimizado para consultas analiticas complejas, no para transacciones
- Los datos llegan ya procesados y limpios desde las fuentes
- Ejemplos: Amazon Redshift, Google BigQuery, Snowflake

**Data Lake:**
- Almacena datos en bruto en su formato original, sin procesar
- Admite cualquier tipo de dato: estructurado, semi y no estructurado
- Mas barato que el DW, pero requiere mas trabajo para analizar
- Ejemplos: AWS S3, Azure Data Lake, Google Cloud Storage

**Data Mart:**
- Subconjunto de un Data Warehouse orientado a un departamento concreto
- El equipo de marketing tiene su Data Mart, el de finanzas el suyo...
- Mas rapido de consultar que el DW completo porque contiene menos datos

**Big Data:**
- Datos que por su volumen, velocidad o variedad no caben en sistemas
  tradicionales
- Las 3 Vs: Volume (mucho), Velocity (rapido), Variety (variado)
- Herramientas: Hadoop, Apache Spark, sistemas distribuidos

---

## 5. OLTP vs OLAP

Distincion importante que aparece mucho en entrevistas:

**OLTP — Online Transaction Processing:**
- Sistemas que registran operaciones en tiempo real
- Cada transaccion es pequena (un pedido, un pago, un login)
- Priorizan velocidad de escritura y consistencia de los datos
- Ejemplos: el sistema de caja de un supermercado, la base de datos
  de una tienda online

**OLAP — Online Analytical Processing:**
- Sistemas diseñados para consultas analiticas complejas
- Las consultas involucran muchos registros y calculos agregados
- Priorizan velocidad de lectura
- Ejemplos: un Data Warehouse, BigQuery, Redshift

**Ejemplo practico:**

```
Cliente compra en Amazon     ->  OLTP  (registra el pedido)
Analista estudia patrones    ->  OLAP  (agrega millones de pedidos)
de compra del ultimo año
```

La misma empresa puede tener ambos sistemas: el OLTP para las operaciones
del dia a dia y el OLAP para el analisis estrategico.

---

## 6. El flujo completo de los datos

Como llegan los datos desde donde se generan hasta donde se analizan:

```
FUENTE          ->  INGESTION  ->  ALMACENAMIENTO  ->  ANALISIS

App web             API / ETL      Base de datos       SQL
App movil           Streaming      Data Warehouse      Python
Sensores IoT        Batch          Data Lake           Excel
Formularios         Web scraping   Data Mart           BI tool
Redes sociales
```

**Ingestion en tiempo real (streaming):**
Los datos se procesan a medida que llegan, sin esperar a acumularlos.
Util para alertas, deteccion de fraude, monitoreo en directo.
Herramientas: Apache Kafka, AWS Kinesis.

**Ingestion por lotes (batch):**
Los datos se acumulan durante un periodo y se procesan todos a la vez
(cada hora, cada noche, cada semana). Mas sencillo y barato.
La mayoria del analisis de negocio es batch.

---

## Glosario del modulo

| Termino | Definicion |
|---------|------------|
| Datos estructurados | Datos organizados en filas y columnas con un esquema fijo |
| Datos semi-estructurados | Datos con estructura parcial o variable (JSON, XML) |
| Datos no estructurados | Datos sin formato predefinido: imagenes, audio, texto libre |
| Base de datos relacional | Sistema que organiza datos en tablas relacionadas, consultable con SQL |
| Data Warehouse | Almacen centralizado de datos historicos optimizado para analisis |
| Data Lake | Almacen de datos en bruto en su formato original, sin procesar |
| Data Mart | Subconjunto de un DW orientado a un departamento especifico |
| ETL | Extract, Transform, Load — proceso de mover y transformar datos entre sistemas |
| OLTP | Sistemas diseñados para procesar transacciones individuales en tiempo real |
| OLAP | Sistemas diseñados para consultas analiticas agregadas sobre grandes volumenes |
| Big Data | Datos que por volumen, velocidad o variedad superan la capacidad de sistemas tradicionales |
| Streaming | Procesamiento de datos en tiempo real a medida que llegan |
| Batch | Procesamiento de datos acumulados en intervalos periodicos |
| API | Interfaz que permite a dos sistemas intercambiar datos de forma estandarizada |
| Schema | Estructura que define como se organizan los datos (columnas, tipos, relaciones) |

---

## Lo mas importante de este modulo

Dos distinciones que hay que tener claras:

1. **Estructurado / semi / no estructurado** determina que herramienta usar.
   SQL funciona perfecto con datos estructurados. Con los otros tipos se
   necesita Python u otras herramientas mas avanzadas.

2. **OLTP vs OLAP** son sistemas con propositos opuestos. Los sistemas de
   la empresa para las operaciones del dia a dia son OLTP. Los sistemas
   de analisis son OLAP. Un analista trabaja principalmente con OLAP.
