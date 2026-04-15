-- Modulo 2: JOINs — Consultas sobre multiples tablas

-- ============================================================
-- INNER JOIN — solo registros con correspondencia en ambas tablas
-- ============================================================

SELECT e.nombre, e.apellido, d.nombre AS departamento, e.salario
FROM empleados e
INNER JOIN departamentos d ON e.id_dept = d.id_dept
ORDER BY e.salario DESC;

-- ============================================================
-- LEFT JOIN — todos los de la izquierda, con la derecha si existe
-- ============================================================

-- Todos los empleados, con su departamento si lo tienen
SELECT e.nombre, e.apellido, d.nombre AS departamento
FROM empleados e
LEFT JOIN departamentos d ON e.id_dept = d.id_dept;

-- Empleados sin departamento asignado
SELECT e.nombre, e.apellido
FROM empleados e
LEFT JOIN departamentos d ON e.id_dept = d.id_dept
WHERE d.id_dept IS NULL;

-- ============================================================
-- RIGHT JOIN — todos los de la derecha, con la izquierda si existe
-- ============================================================

-- Todos los departamentos, con empleados si los tienen
SELECT d.nombre AS departamento, e.nombre AS empleado
FROM empleados e
RIGHT JOIN departamentos d ON e.id_dept = d.id_dept;

-- Departamentos vacios (sin empleados)
SELECT d.nombre AS departamento
FROM empleados e
RIGHT JOIN departamentos d ON e.id_dept = d.id_dept
WHERE e.id IS NULL;

-- ============================================================
-- JOIN con filtros adicionales
-- ============================================================

-- Empleados de IT con salario > 35000
SELECT e.nombre, e.salario
FROM empleados e
INNER JOIN departamentos d ON e.id_dept = d.id_dept
WHERE d.nombre = 'IT' AND e.salario > 35000;

-- JOIN con agregacion: numero de empleados por departamento
SELECT d.nombre AS departamento,
       COUNT(e.id) AS num_empleados,
       AVG(e.salario) AS salario_medio
FROM departamentos d
LEFT JOIN empleados e ON d.id_dept = e.id_dept
GROUP BY d.nombre
ORDER BY num_empleados DESC;
