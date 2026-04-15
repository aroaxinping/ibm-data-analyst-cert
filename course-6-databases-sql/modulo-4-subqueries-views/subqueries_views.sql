-- Modulo 4: Subqueries, CTEs y Vistas

-- ============================================================
-- SUBQUERIES EN WHERE
-- ============================================================

-- Empleados con salario superior a la media
SELECT nombre, salario
FROM empleados
WHERE salario > (SELECT AVG(salario) FROM empleados)
ORDER BY salario DESC;

-- Empleados en departamentos de Barcelona
SELECT nombre
FROM empleados
WHERE id_dept IN (
    SELECT id_dept
    FROM departamentos
    WHERE ciudad = 'Barcelona'
);

-- Empleados que NO estan en IT
SELECT nombre
FROM empleados
WHERE id_dept NOT IN (
    SELECT id_dept FROM departamentos WHERE nombre = 'IT'
);

-- ============================================================
-- SUBQUERIES EN FROM (tabla derivada)
-- ============================================================

SELECT dept_stats.id_dept, dept_stats.media
FROM (
    SELECT id_dept, AVG(salario) AS media
    FROM empleados
    GROUP BY id_dept
) AS dept_stats
WHERE dept_stats.media > 36000;

-- ============================================================
-- CTEs — Common Table Expressions
-- ============================================================

-- CTE unica: empleados sobre la media de su departamento
WITH media_por_dept AS (
    SELECT id_dept, AVG(salario) AS media
    FROM empleados
    GROUP BY id_dept
)
SELECT e.nombre, e.salario, e.id_dept, m.media
FROM empleados e
JOIN media_por_dept m ON e.id_dept = m.id_dept
WHERE e.salario > m.media
ORDER BY e.salario DESC;

-- CTEs encadenadas
WITH antiguos AS (
    SELECT * FROM empleados
    WHERE fecha_alta < '2022-01-01'
),
antiguos_alto_salario AS (
    SELECT * FROM antiguos WHERE salario > 36000
)
SELECT nombre, salario, fecha_alta
FROM antiguos_alto_salario
ORDER BY salario DESC;

-- ============================================================
-- VISTAS
-- ============================================================

-- Crear vista de empleados senior (mas de 2 años)
CREATE VIEW empleados_senior AS
    SELECT nombre, apellido, salario, id_dept
    FROM empleados
    WHERE fecha_alta <= CURRENT_DATE - 2 YEARS;

-- Usar la vista
SELECT * FROM empleados_senior WHERE salario > 38000;

-- Vista de resumen por departamento
CREATE VIEW resumen_departamentos AS
    SELECT
        d.nombre AS departamento,
        d.ciudad,
        COUNT(e.id) AS empleados,
        AVG(e.salario) AS salario_medio
    FROM departamentos d
    LEFT JOIN empleados e ON d.id_dept = e.id_dept
    GROUP BY d.nombre, d.ciudad;

SELECT * FROM resumen_departamentos ORDER BY empleados DESC;

-- Eliminar vista
DROP VIEW empleados_senior;
DROP VIEW resumen_departamentos;
