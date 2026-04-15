# Apuntes — Course 6: Databases and SQL for Data Science with Python

**Duracion:** 20 horas
**Modulos:** 6

---

## Que cubre este curso

SQL desde los fundamentos hasta consultas complejas, con IBM Db2 como base
de datos principal. El curso añade una capa importante respecto al SQL del
certificado de Google: funciones de ventana, procedimientos almacenados, y
conexion a la base de datos desde Python.

---

## Modulo 1: Getting Started with SQL

**DDL — Data Definition Language (estructura):**

```sql
-- Crear tabla
CREATE TABLE empleados (
    id          INT PRIMARY KEY NOT NULL,
    nombre      VARCHAR(50) NOT NULL,
    apellido    VARCHAR(50),
    departamento VARCHAR(30),
    salario     DECIMAL(10, 2),
    fecha_alta  DATE
);

-- Modificar tabla
ALTER TABLE empleados ADD COLUMN email VARCHAR(100);
ALTER TABLE empleados DROP COLUMN email;
ALTER TABLE empleados ALTER COLUMN nombre SET DATA TYPE VARCHAR(100);

-- Eliminar tabla
DROP TABLE empleados;

-- Truncar (vaciar sin borrar la estructura)
TRUNCATE TABLE empleados;
```

**DML — Data Manipulation Language (datos):**

```sql
-- Insertar
INSERT INTO empleados (id, nombre, apellido, departamento, salario)
VALUES (1, 'Ana', 'Garcia', 'IT', 35000.00);

-- Insertar multiples filas
INSERT INTO empleados VALUES
    (2, 'Luis', 'Martinez', 'Marketing', 32000.00, '2022-03-15'),
    (3, 'Marta', 'Lopez', 'IT', 38000.00, '2021-09-01');

-- Actualizar
UPDATE empleados SET salario = 40000.00 WHERE id = 1;
UPDATE empleados SET departamento = 'Datos' WHERE departamento = 'IT';

-- Eliminar
DELETE FROM empleados WHERE id = 3;
DELETE FROM empleados WHERE departamento = 'Marketing';
```

**SELECT basico:**

```sql
-- Todo
SELECT * FROM empleados;

-- Columnas especificas
SELECT nombre, apellido, salario FROM empleados;

-- Con alias
SELECT nombre AS nombre_empleado, salario AS salario_anual FROM empleados;

-- Valores distintos
SELECT DISTINCT departamento FROM empleados;

-- Limitar resultados
SELECT * FROM empleados FETCH FIRST 10 ROWS ONLY;  -- IBM Db2
SELECT * FROM empleados LIMIT 10;                  -- MySQL / PostgreSQL
```

---

## Modulo 2: Introduction to Relational Databases and Tables

**Claves:**

- **Primary Key (PK):** identifica de forma unica cada fila. No puede ser nula
  ni duplicada.
- **Foreign Key (FK):** referencia a la PK de otra tabla. Garantiza integridad
  referencial.

```sql
CREATE TABLE departamentos (
    id_dept  INT PRIMARY KEY,
    nombre   VARCHAR(50)
);

CREATE TABLE empleados (
    id        INT PRIMARY KEY,
    nombre    VARCHAR(50),
    id_dept   INT REFERENCES departamentos(id_dept)
);
```

**WHERE y operadores:**

```sql
-- Comparacion
WHERE salario > 30000
WHERE departamento = 'IT'
WHERE fecha_alta BETWEEN '2021-01-01' AND '2022-12-31'

-- Logicos
WHERE departamento = 'IT' AND salario > 35000
WHERE departamento = 'IT' OR departamento = 'Datos'
WHERE NOT departamento = 'Marketing'

-- Patrones
WHERE nombre LIKE 'A%'      -- empieza por A
WHERE nombre LIKE '%ez'     -- termina en ez
WHERE nombre LIKE '%ar%'    -- contiene "ar"
WHERE nombre NOT LIKE 'A%'

-- Conjuntos
WHERE departamento IN ('IT', 'Datos', 'Finanzas')
WHERE id NOT IN (1, 2, 3)

-- Nulos
WHERE email IS NULL
WHERE email IS NOT NULL

-- ORDER BY
ORDER BY salario DESC
ORDER BY departamento ASC, salario DESC
```

---

## Modulo 3: Intermediate SQL

**Funciones de agregacion:**

```sql
COUNT(*) -- numero de filas (incluye nulos)
COUNT(columna) -- numero de filas no nulas
SUM(salario)
AVG(salario)
MIN(salario)
MAX(salario)

-- Ejemplo
SELECT departamento,
       COUNT(*) AS num_empleados,
       AVG(salario) AS salario_medio,
       MAX(salario) AS salario_max
FROM empleados
GROUP BY departamento;
```

**GROUP BY y HAVING:**

```sql
-- GROUP BY agrupa; HAVING filtra sobre el resultado de la agregacion
-- (WHERE filtra antes de agrupar; HAVING filtra despues)

SELECT departamento, AVG(salario) AS media
FROM empleados
GROUP BY departamento
HAVING AVG(salario) > 35000
ORDER BY media DESC;
```

**Funciones de cadena:**

```sql
UPPER(nombre)
LOWER(nombre)
LENGTH(nombre)
TRIM(nombre)
SUBSTR(nombre, 1, 3)   -- primeros 3 caracteres
CONCAT(nombre, ' ', apellido)
REPLACE(nombre, 'viejo', 'nuevo')
```

**Funciones de fecha:**

```sql
CURRENT_DATE
CURRENT_TIMESTAMP
YEAR(fecha)
MONTH(fecha)
DAY(fecha)
DATE(fecha_timestamp)
DATEDIFF(fecha1, fecha2)        -- diferencia en dias (MySQL)
fecha1 - fecha2                 -- diferencia en dias (PostgreSQL / Db2)
```

**Funciones numericas:**

```sql
ROUND(salario, 2)
CEIL(valor)
FLOOR(valor)
ABS(valor)
MOD(10, 3)   -- modulo: 1
```

---

## Modulo 4: Accessing Multiple Tables with JOINs

**Tipos de JOIN:**

```
Tabla A    Tabla B
+---+      +---+
| 1 |      | 2 |
| 2 |      | 3 |
| 3 |      | 4 |

INNER JOIN: {2, 3}       — solo los que estan en ambas
LEFT JOIN:  {1, 2, 3}    — todos los de A, con B si existe
RIGHT JOIN: {2, 3, 4}    — todos los de B, con A si existe
FULL JOIN:  {1, 2, 3, 4} — todos, con el otro si existe
```

**Sintaxis:**

```sql
-- INNER JOIN
SELECT e.nombre, d.nombre AS departamento
FROM empleados e
INNER JOIN departamentos d ON e.id_dept = d.id_dept;

-- LEFT JOIN
SELECT e.nombre, d.nombre AS departamento
FROM empleados e
LEFT JOIN departamentos d ON e.id_dept = d.id_dept;
-- Incluye empleados sin departamento asignado (d.nombre sera NULL)

-- Multiples JOINs
SELECT e.nombre, d.nombre AS dept, p.titulo AS proyecto
FROM empleados e
INNER JOIN departamentos d ON e.id_dept = d.id_dept
INNER JOIN asignaciones a ON e.id = a.id_empleado
INNER JOIN proyectos p ON a.id_proyecto = p.id;
```

---

## Modulo 5: Sub-queries and Nested Selects

**Subqueries:**

```sql
-- En WHERE
SELECT nombre, salario
FROM empleados
WHERE salario > (SELECT AVG(salario) FROM empleados);

-- En FROM (tabla derivada)
SELECT dept_stats.departamento, dept_stats.media
FROM (
    SELECT departamento, AVG(salario) AS media
    FROM empleados
    GROUP BY departamento
) AS dept_stats
WHERE dept_stats.media > 35000;

-- Con IN
SELECT nombre FROM empleados
WHERE id_dept IN (
    SELECT id_dept FROM departamentos WHERE nombre LIKE '%Tech%'
);

-- EXISTS
SELECT nombre FROM empleados e
WHERE EXISTS (
    SELECT 1 FROM asignaciones a WHERE a.id_empleado = e.id
);
```

**CTEs (Common Table Expressions):**

```sql
WITH salarios_dept AS (
    SELECT departamento, AVG(salario) AS media_dept
    FROM empleados
    GROUP BY departamento
),
empleados_sobre_media AS (
    SELECT e.nombre, e.salario, e.departamento
    FROM empleados e
    JOIN salarios_dept sd ON e.departamento = sd.departamento
    WHERE e.salario > sd.media_dept
)
SELECT * FROM empleados_sobre_media
ORDER BY salario DESC;
```

**Vistas:**

```sql
-- Crear vista
CREATE VIEW vista_it AS
    SELECT nombre, apellido, salario
    FROM empleados
    WHERE departamento = 'IT';

-- Usar la vista como si fuera una tabla
SELECT * FROM vista_it WHERE salario > 35000;

-- Eliminar vista
DROP VIEW vista_it;
```

**Funciones de ventana:**

```sql
-- ROW_NUMBER: numero de fila dentro de cada particion
SELECT nombre, salario, departamento,
       ROW_NUMBER() OVER (PARTITION BY departamento ORDER BY salario DESC) AS ranking
FROM empleados;

-- RANK y DENSE_RANK
RANK() OVER (ORDER BY salario DESC)        -- salta numeros en empates
DENSE_RANK() OVER (ORDER BY salario DESC)  -- no salta numeros en empates

-- LAG y LEAD: valor de la fila anterior/siguiente
SELECT fecha, ventas,
       LAG(ventas, 1) OVER (ORDER BY fecha) AS ventas_dia_anterior,
       ventas - LAG(ventas, 1) OVER (ORDER BY fecha) AS variacion
FROM ventas_diarias;

-- Acumulado
SUM(ventas) OVER (ORDER BY fecha ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
```

---

## Modulo 6: Working with Real-World Datasets and SQL in Python

**Conectar Python a IBM Db2:**

```python
import ibm_db

# Cadena de conexion
dsn = (
    "DRIVER={IBM DB2 ODBC DRIVER};"
    "DATABASE=BLUDB;"
    "HOSTNAME=tu_host.databases.appdomain.cloud;"
    "PORT=30376;"
    "PROTOCOL=TCPIP;"
    "UID=tu_usuario;"
    "PWD=tu_password;"
    "Security=SSL;"
)

conn = ibm_db.connect(dsn, "", "")
```

**Ejecutar queries con ibm_db:**

```python
# Query simple
query = "SELECT * FROM empleados FETCH FIRST 10 ROWS ONLY"
stmt = ibm_db.exec_immediate(conn, query)

fila = ibm_db.fetch_assoc(stmt)
while fila:
    print(fila)
    fila = ibm_db.fetch_assoc(stmt)
```

**Mas comodo con pandas + SQLAlchemy:**

```python
import pandas as pd
from sqlalchemy import create_engine

# SQLite para pruebas locales
engine = create_engine("sqlite:///datos.db")

# Cargar resultado de query directamente en DataFrame
df = pd.read_sql("SELECT * FROM empleados WHERE salario > 35000", engine)

# Insertar DataFrame en base de datos
df.to_sql("empleados_copia", engine, if_exists="replace", index=False)
```

**Usar magia SQL en Jupyter:**

```python
# Instalar: pip install ipython-sql
%load_ext sql
%sql sqlite:///datos.db

%%sql
SELECT departamento, AVG(salario)
FROM empleados
GROUP BY departamento
ORDER BY AVG(salario) DESC
```

---

## Esquema resumido del curso

```
COURSE 6: SQL
|
+-- DDL / DML
|     CREATE, ALTER, DROP, INSERT, UPDATE, DELETE
|
+-- SELECT y filtros
|     WHERE, LIKE, IN, IS NULL, ORDER BY
|
+-- Agregacion
|     GROUP BY, HAVING, COUNT, SUM, AVG, MAX, MIN
|
+-- JOINs
|     INNER, LEFT, RIGHT, FULL
|
+-- Avanzado
|     Subqueries, CTEs, Vistas, Funciones de ventana
|
+-- Python + SQL
      ibm_db, pandas read_sql, SQLAlchemy, magia %sql
```

---

## Glosario

| Termino | Definicion |
|---------|------------|
| DDL | Data Definition Language — comandos que definen la estructura (CREATE, ALTER, DROP) |
| DML | Data Manipulation Language — comandos que manipulan datos (INSERT, UPDATE, DELETE, SELECT) |
| Primary Key | Columna que identifica de forma unica cada fila de una tabla |
| Foreign Key | Columna que referencia la PK de otra tabla, estableciendo una relacion |
| JOIN | Operacion que combina filas de dos tablas basandose en una condicion |
| Subquery | Query anidada dentro de otra query |
| CTE | Common Table Expression — resultado temporal nombrado que mejora la legibilidad |
| Vista | Tabla virtual basada en una query almacenada en la base de datos |
| Funcion de ventana | Funcion que calcula un valor sobre un conjunto de filas relacionadas con la actual |
| GROUP BY | Clausula que agrupa filas con el mismo valor en una columna |
| HAVING | Clausula que filtra grupos creados por GROUP BY (equivalente a WHERE para grupos) |

---

## Errores comunes

- **Usar WHERE en vez de HAVING para filtrar agregaciones:** `WHERE COUNT(*) > 5`
  es incorrecto. `HAVING COUNT(*) > 5` es la sintaxis correcta.
- **INNER JOIN cuando se necesita LEFT JOIN:** si puede haber registros sin
  correspondencia en la tabla de la derecha, un INNER JOIN los eliminara
  silenciosamente.
- **No qualificar columnas en JOINs:** si ambas tablas tienen una columna
  `nombre`, `SELECT nombre` es ambiguo. Siempre usar `tabla.nombre`.
- **ORDER BY en subquery:** en la mayoria de bases de datos, un ORDER BY dentro
  de una subquery no garantiza el orden del resultado final. Ordenar siempre
  en la query exterior.

---

## Conexion con otros cursos

- Las funciones de agregacion y GROUP BY de este curso son el equivalente
  SQL de `.groupby()` en pandas (curso 4 y 7).
- Los CTEs y vistas son la version SQL de los DataFrames intermedios que
  se crean en pandas para analisis en varias etapas.
- En el capstone (curso 9) se usa SQL para extraer datos de bases de datos
  reales y luego Python para visualizarlos.
