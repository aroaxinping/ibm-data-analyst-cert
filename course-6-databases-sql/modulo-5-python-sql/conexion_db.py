# Modulo 5: Python + SQL — Conexion y consultas desde Python

import pandas as pd
from sqlalchemy import create_engine, text

# ===================== SQLite (pruebas locales) =====================

# Crear conexion a SQLite
engine = create_engine("sqlite:///empresa.db")

# Crear tablas e insertar datos de ejemplo
with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS departamentos (
            id_dept INTEGER PRIMARY KEY,
            nombre  TEXT NOT NULL,
            ciudad  TEXT
        )
    """))

    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS empleados (
            id         INTEGER PRIMARY KEY,
            nombre     TEXT NOT NULL,
            apellido   TEXT,
            id_dept    INTEGER REFERENCES departamentos(id_dept),
            salario    REAL,
            fecha_alta TEXT
        )
    """))

    conn.execute(text("""
        INSERT OR IGNORE INTO departamentos VALUES
            (1, 'IT', 'Barcelona'),
            (2, 'Marketing', 'Madrid'),
            (3, 'Finanzas', 'Barcelona'),
            (4, 'Datos', 'Barcelona')
    """))

    conn.execute(text("""
        INSERT OR IGNORE INTO empleados VALUES
            (1, 'Ana', 'Garcia', 1, 38000.0, '2021-03-15'),
            (2, 'Luis', 'Martinez', 2, 32000.0, '2022-01-10'),
            (3, 'Marta', 'Lopez', 1, 42000.0, '2020-09-01'),
            (4, 'Carlos', 'Ruiz', 4, 45000.0, '2019-06-20'),
            (5, 'Sara', 'Gomez', 3, 36000.0, '2023-02-28')
    """))
    conn.commit()

# ===================== Leer con pandas =====================

df_empleados = pd.read_sql("SELECT * FROM empleados", engine)
print("Todos los empleados:")
print(df_empleados)

# Query con filtro
df_it = pd.read_sql(
    "SELECT nombre, salario FROM empleados WHERE id_dept = 1 ORDER BY salario DESC",
    engine
)
print("\nEmpleados de IT:")
print(df_it)

# JOIN en Python
query_join = """
    SELECT e.nombre, e.salario, d.nombre AS departamento
    FROM empleados e
    INNER JOIN departamentos d ON e.id_dept = d.id_dept
    ORDER BY e.salario DESC
"""
df_join = pd.read_sql(query_join, engine)
print("\nJoin empleados + departamentos:")
print(df_join)

# Estadisticas por departamento
query_stats = """
    SELECT d.nombre AS departamento,
           COUNT(*) AS empleados,
           AVG(e.salario) AS salario_medio,
           MAX(e.salario) AS salario_max
    FROM empleados e
    INNER JOIN departamentos d ON e.id_dept = d.id_dept
    GROUP BY d.nombre
    ORDER BY salario_medio DESC
"""
df_stats = pd.read_sql(query_stats, engine)
print("\nEstadisticas por departamento:")
print(df_stats)

# ===================== Escribir DataFrame en DB =====================

# Crear DataFrame de nuevos empleados
nuevos = pd.DataFrame({
    "id": [6, 7],
    "nombre": ["Elena", "Marcos"],
    "apellido": ["Vidal", "Torres"],
    "id_dept": [4, 1],
    "salario": [41000.0, 39000.0],
    "fecha_alta": ["2024-01-15", "2024-03-01"]
})

# Insertar en la base de datos
nuevos.to_sql("empleados", engine, if_exists="append", index=False)
print("\nEmpleados despues de insertar nuevos:")
print(pd.read_sql("SELECT * FROM empleados", engine))
