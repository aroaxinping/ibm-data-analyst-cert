# Actividades — Modulo 2: The Data Analyst Ecosystem

---

## Actividad 1: Clasificar tipos de datos

Para cada fuente de datos, identificar si produce datos estructurados,
semi-estructurados o no estructurados. Justificar.

| Fuente de datos | Tipo | Justificacion |
|-----------------|------|---------------|
| Tabla de clientes en MySQL | Estructurado | Schema fijo: columnas definidas con tipos |
| Tweets de una cuenta de empresa | Semi-estructurado | El tweet tiene campos (id, texto, fecha, usuario) pero el contenido es texto libre |
| Grabaciones de llamadas al soporte | No estructurado | Audio sin esquema |
| Archivo JSON de respuestas de una API | Semi-estructurado | Tiene estructura pero puede variar entre registros |
| Hoja de calculo de ventas mensuales | Estructurado | Filas y columnas con schema fijo |
| Fotos de productos en un e-commerce | No estructurado | Imagenes sin esquema |
| Logs de acceso de un servidor web | Semi-estructurado | Tienen formato pero variable y dificil de consultar directamente |
| Encuesta con preguntas cerradas (si/no, 1-5) | Estructurado | Respuestas codificadas en columnas definidas |
| Encuesta con campo de texto libre | No estructurado | Texto sin esquema |

---

## Actividad 2: Disenar el ecosistema de una empresa

**Caso:** una cadena de supermercados con 200 tiendas quiere analizar
sus datos para tomar mejores decisiones de compra y stock.

Tienen:
- Sistema de caja que registra cada venta en tiempo real
- Ficheros CSV que llegan cada semana de los proveedores con precios
- App movil de clientes con historial de compras y opiniones escritas
- Datos de clima de una API externa

**Mapear cada dato al tipo y al sistema adecuado:**

| Fuente | Tipo de dato | Sistema de almacenamiento | Sistema de analisis |
|--------|-------------|--------------------------|---------------------|
| Sistema de caja (ventas en tiempo real) | Estructurado | OLTP (base de datos transaccional) | OLAP / Data Warehouse |
| CSVs de proveedores (semanal) | Estructurado | Data Warehouse (via ETL batch) | SQL / BI tool |
| Historial de compras app | Estructurado | Data Warehouse | SQL / Python |
| Opiniones escritas app | No estructurado | Data Lake | Python + NLP |
| Datos de clima (API) | Semi-estructurado | Data Warehouse (transformado) | SQL / Python |

**Flujo ETL para las ventas:**
```
Sistema de caja (OLTP)
    -> ETL nocturno (limpiar, agregar por tienda/producto)
    -> Data Warehouse
    -> Analista consulta con SQL
    -> Dashboard en BI tool
```

---

## Actividad 3: OLTP vs OLAP en la practica

Para cada consulta, decidir si deberia ejecutarse sobre el sistema OLTP
o sobre el OLAP, y por que.

| Consulta | OLTP o OLAP | Por que |
|----------|-------------|---------|
| Registrar el pago de un cliente | OLTP | Operacion individual en tiempo real |
| Ver las ventas totales de los ultimos 12 meses por categoria | OLAP | Consulta agregada sobre datos historicos |
| Consultar el stock actual de un producto | OLTP | Dato operacional que cambia en tiempo real |
| Calcular el ticket medio por tipo de cliente en 2024 | OLAP | Agregacion sobre gran volumen de datos historicos |
| Actualizar la direccion de un cliente | OLTP | Operacion individual de escritura |
| Comparar las ventas de cada tienda con el mismo periodo del año anterior | OLAP | Analisis historico comparativo |

---

## Actividad 4: Vocabulario aplicado

Completar las frases con el termino correcto del glosario.

1. El proceso de extraer datos de varias fuentes, transformarlos y cargarlos
   en el Data Warehouse se llama ___.

2. Un almacen que guarda datos en bruto de cualquier tipo, sin procesar,
   se llama ___.

3. Un sistema ___ registra cada transaccion en tiempo real y esta optimizado
   para escrituras rapidas.

4. Cuando los datos se procesan a medida que llegan, sin esperar a acumularlos,
   se llama procesamiento en ___.

5. La estructura que define las columnas, tipos y relaciones de una base de datos
   se llama ___.

**Respuestas:** ETL / Data Lake / OLTP / tiempo real (streaming) / schema
