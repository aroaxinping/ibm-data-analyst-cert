# Quiz de Practica — Modulo 2: The Data Analyst Ecosystem

---

**1. Una empresa almacena las fotos de perfil de sus usuarios, los mensajes
de soporte al cliente y los registros de sus pedidos en el mismo sistema.
¿Que tipo de dato es cada uno?**

<details>
<summary>Respuesta</summary>

- Fotos de perfil: **no estructurados** (imagenes sin esquema)
- Mensajes de soporte: **no estructurados** (texto libre) o semi-estructurados
  si tienen metadatos como fecha, id de usuario, etc.
- Registros de pedidos: **estructurados** (filas y columnas con schema fijo:
  id, fecha, producto, cantidad, precio...)

</details>

---

**2. Un analista necesita estudiar las ventas de los ultimos 3 años por
region y categoria de producto. ¿Que tipo de sistema es mas adecuado
para hacer esa consulta: OLTP u OLAP?**

<details>
<summary>Respuesta</summary>

**OLAP.** Las consultas analiticas que agregan grandes volumenes de datos
historicos son exactamente el caso de uso de OLAP (Data Warehouse).

Un sistema OLTP almacena las transacciones individuales, pero no esta
optimizado para consultas que cruzan millones de registros. Intentar hacer
ese analisis directamente sobre una base de datos OLTP ralentizaria el
sistema y podria afectar a las operaciones.

</details>

---

**3. ¿Cual es la diferencia entre un Data Warehouse y un Data Lake?**

<details>
<summary>Respuesta</summary>

| | Data Warehouse | Data Lake |
|-|----------------|-----------|
| Datos | Procesados y limpios | En bruto, sin procesar |
| Tipos | Solo estructurados | Todos los tipos |
| Acceso | Rapido para analitica | Requiere procesamiento previo |
| Coste | Mas caro | Mas barato |
| Uso | Analitica de negocio | ML, exploración, datos no estructurados |

En la practica muchas empresas tienen ambos: el Data Lake como almacen
barato de todo, y el Data Warehouse con los datos ya procesados para
el analisis del dia a dia.

</details>

---

**4. Un startup de e-commerce quiere enviar alertas en tiempo real cuando
se detecta una transaccion potencialmente fraudulenta. ¿Que tipo de
ingestion necesita?**

<details>
<summary>Respuesta</summary>

**Streaming.** El fraude tiene que detectarse en el momento en que ocurre,
no horas despues. El procesamiento en tiempo real (streaming) permite
analizar cada transaccion a medida que llega y generar la alerta de inmediato.

Si usaran batch, el fraude ya se habria completado antes de detectarlo.

</details>

---

**5. ¿Que significa ETL y en que parte del ecosistema de datos aparece?**

<details>
<summary>Respuesta</summary>

**Extract, Transform, Load.** Es el proceso de la etapa de procesamiento:

1. **Extract:** extraer datos desde las fuentes (bases de datos, APIs, CSVs...)
2. **Transform:** limpiar, transformar y estandarizar los datos
3. **Load:** cargar los datos transformados en el destino (DW, Data Lake...)

Es el puente entre donde viven los datos y donde se analizan.

</details>

---

**6. Un equipo de marketing quiere analizar rapidamente el rendimiento
de sus campanas sin tener que consultar todo el Data Warehouse de la empresa.
¿Que solucion del ecosistema encaja mejor?**

<details>
<summary>Respuesta</summary>

**Data Mart.** Un Data Mart es un subconjunto del DW orientado a un
departamento especifico. El equipo de marketing tendria su propio Data Mart
con solo los datos que necesita — mas rapido de consultar y mas facil
de mantener que el DW completo.

</details>

---

**7. Verdadero o falso: los datos no estructurados son poco relevantes
para el analisis de datos moderno.**

<details>
<summary>Respuesta</summary>

**Falso.** Los datos no estructurados representan aproximadamente el 80%
de todos los datos que se generan en el mundo. Con el avance del
procesamiento de lenguaje natural (NLP) y la vision por computador,
son cada vez mas analizables y valiosos — analisis de sentimiento en
redes sociales, deteccion de objetos en imagenes, transcripcion de audio...

</details>

---

**8. ¿Por que una empresa tendria tanto un sistema OLTP como un sistema OLAP?**

<details>
<summary>Respuesta</summary>

Porque tienen propositos opuestos y no pueden optimizarse para ambos a la vez:

- **OLTP** necesita ser rapido en escrituras y garantizar consistencia
  para las operaciones del dia a dia (ventas, pagos, registros)
- **OLAP** necesita ser rapido en lecturas de grandes volumenes para
  el analisis

Hacer consultas analiticas pesadas sobre el sistema OLTP lo ralentizaria
y podria afectar a los clientes. La solucion tipica: copiar los datos del
OLTP al OLAP periodicamente (via ETL) y hacer el analisis ahi.

</details>
